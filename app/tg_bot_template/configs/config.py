import logging

from typing import Callable
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot

def load_config() -> Config:

    import os
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())

    from app.tg_bot_template.data_base.engin import start_data_base, create_data_base
    from app.tg_bot_template.data_base.model import favourites_places, users_page

    start_data_base('base', favourites_places, users_page, create_data_base)

    logger.info('return config')
    return Config(tg_bot=TgBot(token=os.getenv('TOKEN')))

if __name__ == '__main__':
    print(load_config())
