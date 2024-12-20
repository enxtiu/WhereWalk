import logging

from dataclasses import dataclass

from app.tg_bot_template.services.servis import sh_all, sh_apt, sh_whe, sh_con, sh_prod, sh_gost
from ..lexicon_data import lexicon_en, lexicon_ru

logger = logging.getLogger(__name__)

@dataclass
class TgBot:
    token: str

@dataclass
class Translation[T]:
    values: dict[str, T]

@dataclass
class DataVid:
    sheet_all: tuple[tuple[str, ...], tuple[str, ...]]
    sheet_apt: tuple[tuple[str, ...], tuple[str, ...]]
    sheet_prod: tuple[tuple[str, ...], tuple[str, ...]]
    sheet_gost: tuple[tuple[str, ...], tuple[str, ...]]
    sheet_whe: tuple[tuple[str, ...], tuple[str, ...]]
    sheet_con: tuple[tuple[str, ...], tuple[str, ...]]

@dataclass
class Config:
    tg_bot: TgBot
    translation: Translation
    data_vid: DataVid

def load_config() -> Config:

    import os
    from dotenv import load_dotenv, find_dotenv

    load_dotenv(find_dotenv())
    translations = {
        'default': 'ru',
        'ru': lexicon_ru,
        'en': lexicon_en
    }

    logger.info('return config')
    return Config(
        tg_bot=TgBot(token=os.getenv('TOKEN')),
        translation=Translation(values=translations),
        data_vid=DataVid(
            sheet_all=sh_all,
            sheet_apt=sh_apt,
            sheet_prod=sh_prod,
            sheet_gost=sh_gost,
            sheet_whe=sh_whe,
            sheet_con=sh_con
        )
    )

if __name__ == '__main__':
    print(load_config())
