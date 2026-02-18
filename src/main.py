from config.config import create_config
from parse_args import parse_args

def main():
    args = parse_args()
    if not args.env_path:
        raise SystemExit("Укажите путь к .env: --env-path=/path/to/env")
    config = create_config(args.env_path)
    print(config)


if __name__ == "__main__":
    main()