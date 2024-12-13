import logging

from aiogram import Bot

logger = logging.getLogger(__name__)


async def set_command(bot: Bot):
    menu = [
        #        types.BotCommand(command='/start',
        #                        description=LEXICON_RU['start_des'])
    ]

    logger.info('Init set my command')
    await bot.set_my_commands(menu)


if __name__ == '__main__':
    pass
