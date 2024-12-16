import logging

from aiogram import Bot, types

from app.tg_bot_template.lexicon_data.lexicon_ru import LEXICON

logger = logging.getLogger(__name__)


async def set_command(bot: Bot):
    menu = [
        types.BotCommand(command=k, description=v) for k, v in LEXICON.get('menu_des').items()
    ]

    logger.info('Init set my command')
    await bot.set_my_commands(menu)


if __name__ == '__main__':
    pass
