-- +goose Up
-- +goose StatementBegin
create table if not exists book_user_readed (
    id serial primary key,
    book_id int references book(id) on delete cascade not null,
    user_id int not null
);
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
drop table if exists book_user_readed;
-- +goose StatementEnd
