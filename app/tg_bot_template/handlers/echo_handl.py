import logging

from aiogram import Router, types

from app.tg_bot_template.lexicon_data.lexicon import LEXICON_RU

logger = logging.getLogger(__name__)

router: Router = Router()

@router.message()
async def echo(message: types.Message) -> None:
    await message.answer(text=LEXICON_RU['echo'])