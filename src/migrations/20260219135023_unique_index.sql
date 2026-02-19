-- +goose Up
-- +goose StatementBegin
create unique index if not exists idx_book_user_readed_book_id_user_id on book_user_readed (book_id, user_id);
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
drop index if exists idx_book_user_readed_book_id_user_id;
-- +goose StatementEnd
