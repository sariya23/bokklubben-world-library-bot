import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--env-path",
        type=str,
        default=None,
        help="Путь к файлу .env (например: --env-path=config/.env.local)",
    )
    args = parser.parse_args()
    if not args.env_path:
        raise SystemExit("Укажите путь к .env: --env-path=/path/to/env")
    return args