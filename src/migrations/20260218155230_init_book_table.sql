-- +goose Up
-- +goose StatementBegin
create table if not exists book (
    id int generated always as identity primary key,
    title varchar not null,
    author_full_name varchar not null,
    country varchar not null,
    century int not null,
    image_key varchar not null
);
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
drop table if exists book;
-- +goose StatementEnd
