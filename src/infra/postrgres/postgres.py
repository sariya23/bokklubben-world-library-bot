import asyncio
from contextlib import contextmanager
from typing import Generator

from psycopg2 import pool
from psycopg2.extensions import connection as PgConnection, cursor as PgCursor

from src.config.config import DbConfig
from src.domain.book import Book
from src.service import error as srv_error
from psycopg2 import errors

class Postgres:
    """Слой для работы с PostgreSQL. В __init__ создаётся пул соединений."""

    def __init__(self, config: DbConfig) -> None:
        self._db_config = config
        sslmode = "require" if self._db_config.db_use_ssl == "require" else "prefer"
        self._pool = pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            host=self._db_config.db_host,
            port=self._db_config.db_port,
            dbname=self._db_config.db_name,
            user=self._db_config.db_username,
            password=self._db_config.db_password,
            sslmode=sslmode,
        )

    @contextmanager
    def _connection(self) -> Generator[PgConnection, None, None]:
        conn = self._pool.getconn()
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            self._pool.putconn(conn)

    @contextmanager
    def _cursor(self, cursor_factory=None) -> Generator[PgCursor, None, None]:
        with self._connection() as conn:
            cur = conn.cursor(cursor_factory=cursor_factory)
            try:
                yield cur
            finally:
                cur.close()

    def _get_books_sync(self) -> list[Book]:
        with self._cursor() as cur:
            cur.execute(
                "SELECT id, title, author_full_name, country, century FROM book ORDER BY title"
            )
            rows = cur.fetchall()
        return [
            Book(
                id=int(row[0]),
                title=str(row[1]),
                author=str(row[2]),
                country=str(row[3]),
                century=int(row[4]),
            )
            for row in rows
        ]

    async def get_all_books(self) -> list[Book]:
        """Асинхронно возвращает список всех книг (не блокирует event loop)."""
        return await asyncio.to_thread(self._get_books_sync)

    def _add_book_user_readed_sync(self, book_id: int, user_id: int):
        try:
            with self._cursor() as cur:
                cur.execute(
                    "insert into book_user_readed (book_id, user_id) values (%s, %s)",
                    (book_id, user_id),
                )
        except errors.UniqueViolation:
            raise srv_error.UserAlredyReadedBookError

    def _remove_book_user_readed_sync(self, book_id: int, user_id: int):
        with self._cursor() as cur:
            cur.execute(
                "delete from book_user_readed WHERE book_id = %s and user_id = %s",
                (book_id, user_id),
            )
    
    async def add_book_user_readed(self, book_id: int, user_id: int):
        return await asyncio.to_thread(self._add_book_user_readed_sync, book_id, user_id)
    
    async def remove_book_user_readed(self, book_id: int, user_id: int):
        return await asyncio.to_thread(self._remove_book_user_readed_sync, book_id, user_id)
    
        

    def close(self) -> None:
        if self._pool:
            self._pool.closeall()
            self._pool = None
