import logging

from typing import Callable
from dataclasses import dataclass

from ..lexicon_data import lexicon_en, lexicon_ru

logger = logging.getLogger(__name__)

@dataclass
class TgBot:
    token: str


@dataclass
class Translation[T]:
    values: dict[str, T]

@dataclass
class Config:
    tg_bot: TgBot
    translation: Translation

def load_config() -> Config:

    import os
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    translations = {
        'default': 'ru',
        'ru': lexicon_ru,
        'en': lexicon_en
    }

    from app.tg_bot_template.data_base.engin import start_data_base, create_data_base
    from app.tg_bot_template.data_base.model import favourites_places, users_page

    start_data_base('base', favourites_places, users_page, create_data_base)

    logger.info('return config')
    return Config(tg_bot=TgBot(token=os.getenv('TOKEN')), translation=Translation(values=translations))

if __name__ == '__main__':
    print(load_config())
