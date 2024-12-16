import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.tg_bot_template.configs.config import load_config, Config
from app.tg_bot_template.keyboards.set_menu import set_command
from app.tg_bot_template.handlers import users_handl, echo_handl
from app.tg_bot_template.middlewares.i18n import TranslatorMiddleware
from app.tg_bot_template.lexicon_data import lexicon_en, lexicon_ru

logger = logging.getLogger(__name__)

translations = {
    'default': 'ru',
    'ru': lexicon_ru,
    'en': lexicon_en
}

async def main() -> None:
    config: Config = load_config()

    logger.info('Init token bot')
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    await set_command(bot)
    logger.info('register my command')
    dp.startup.register(set_command)

    dp.include_router(users_handl.router)
    dp.include_router(echo_handl.router)

    dp.update.middleware(TranslatorMiddleware())

    dp.workflow_data.update(_translation=translations)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=[])
    logger.info('Start polling')
