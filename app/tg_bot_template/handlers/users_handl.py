import logging

from aiogram import types, F, filters, Router

from app.tg_bot_template.keyboards.inline_key import keyboard_st, keyboard_vid


logger = logging.getLogger(__name__)

router: Router = Router()


@router.message(filters.CommandStart())
async def get_start(message: types.Message, i18n) -> None:
    await message.answer(text=i18n.LEXICON['/start'], reply_markup=keyboard_st)



