import logging


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

    logger.info('return config')
    return Config(tg_bot=TgBot(token=os.getenv('TOKEN')))

if __name__ == '__main__':
    print(load_config())
