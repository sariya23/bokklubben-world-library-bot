from dataclasses import dataclass
from environs import Env

@dataclass
class BotConfig:
    bot_token: str

@dataclass
class DbConfig:
    db_name: str
    db_username: str
    db_password: str
    db_host: str
    db_use_ssl: bool


@dataclass
class Config:
    bot: BotConfig
    db: DbConfig


def create_config(config_path: str) -> Config:
    env = Env()
    env.read_env(config_path)

    return Config(
        bot=BotConfig(
            bot_token=env.str("BOT_TOKEN"),
        ),
        db=DbConfig(
            db_name=env.str("DB_NAME"),
            db_username=env.str("DB_USERNAME"),
            db_password=env.str("DB_PASSWORD"),
            db_host=env.str("DB_HOST"),
            db_use_ssl=env.bool("DB_USE_SSL"),
        ),
    )