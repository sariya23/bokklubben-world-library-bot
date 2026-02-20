FROM ubuntu:22.04 AS migrations
WORKDIR /app
ENV PATH="/usr/lib/postgresql-client/bin:${PATH}"
RUN apt-get update && \
    apt-get install -y postgresql-client git make
ADD --chmod=755 https://github.com/pressly/goose/releases/download/v3.14.0/goose_linux_x86_64 /usr/local/bin/goose
COPY src/migrations ./src/migrations
COPY Makefile ./
# config/prod.env монтируется с хоста при запуске
