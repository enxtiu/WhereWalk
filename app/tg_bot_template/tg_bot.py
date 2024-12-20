import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.tg_bot_template.configs.config import load_config, Config
from app.tg_bot_template.handlers import users_handl, echo_handl, call_filter_users_handl
from app.tg_bot_template.keyboards.set_menu import set_command
from app.tg_bot_template.middlewares.i18n import TranslatorMiddleware

logger = logging.getLogger(__name__)


async def main() -> None:
    config: Config = load_config()

    logger.info('Init token bot')
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.workflow_data.update(_translation=config.translation.values, data_vid=config.data_vid)

    await set_command(bot)
    logger.info('register my command')
    dp.startup.register(set_command)

    dp.include_router(users_handl.router)
    dp.include_router(call_filter_users_handl.router)
    dp.include_router(echo_handl.router)

    dp.update.middleware(TranslatorMiddleware())

    logger.info('init workflow_data')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=[])
    logger.info('Start polling')
