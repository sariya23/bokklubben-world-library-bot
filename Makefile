ENV ?= dev
ENV_FILE = ./config/.env.${ENV}

# usage: Нужно указать префикс env файла. То есть
# если используем local.env, то пишем make migrate ENV=local.

include ${ENV_FILE}

.PHONY: run
run:
	python3 main.py --env-path=config/.env.local

migrate:
	goose -dir src/migrations postgres \
	"postgresql://$(DB_USERNAME):$(DB_PASSWORD)\
	@$(DB_HOST):$(DB_PORT)/$(DB_NAME)\
	?sslmode=$(DB_USE_SSL)" up

infra:
	docker-compose -f src/deploy/local/docker-compose.yaml --env-file=config/.env.local up -d