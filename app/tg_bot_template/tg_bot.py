import logging

from aiogram import Bot, Dispatcher

from app.tg_bot_template.config_data.config import load_config, Config
from app.tg_bot_template.keyboards.set_menu import set_command
from app.tg_bot_template.handlers import users_handl, echo_handl

logger = logging.getLogger(__name__)


async def main() -> None:
    config: Config = load_config()

    logger.info('Init token bot')
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    await set_command(bot)
    logger.info('register my command')
    dp.startup.register(set_command)

    dp.include_router(users_handl.router)
    dp.include_router(echo_handl.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=[])
    logger.info('Start polling')
