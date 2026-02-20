ENV ?= dev
ENV_FILE = ./config/$(ENV).env

# usage: Нужно указать префикс env файла. То есть
# если используем local.env, то пишем make migrate ENV=local.

include ${ENV_FILE}

.PHONY: run
run:
	python3 main.py --env-path=config/local.env

migrate:
	goose -dir src/migrations postgres \
	"postgresql://$(DB_USERNAME):$(DB_PASSWORD)\
	@$(DB_HOST):$(DB_PORT)/$(DB_NAME)\
	?sslmode=$(DB_USE_SSL)" up

infra:
	docker-compose -f ./deploy/local/docker-compose.yaml --env-file=config/local.env up -d