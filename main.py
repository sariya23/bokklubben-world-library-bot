from src.config.config import create_config
from src.parse_args import parse_args

import logging
import asyncio

logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    args = parse_args()
    config = create_config(args.env_path)
    logging.info("config load successfully")
    logging.info(f"env type: {config.env_type.env_type}")


if __name__ == "__main__":
    asyncio.run(main())