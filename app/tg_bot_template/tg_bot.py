import logging

from aiogram import Bot, Dispatcher

from app.tg_bot_template.config_data.config import load_config, Config

logger = logging.getLogger(__name__)


async def main() -> None:
    config: Config = load_config()

    logger.info('Init token bot')
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=[])
    logger.info('Start polling')
