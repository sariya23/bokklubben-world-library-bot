import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--env-path",
        type=str,
        default=None,
        help="Путь к файлу .env (например: --env-path=config/.env.local)",
    )
    return parser.parse_args()