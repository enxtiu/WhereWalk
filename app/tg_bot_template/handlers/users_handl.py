import logging
from datetime import datetime

from aiogram import types, filters, Router
from app.tg_bot_template.keyboards.inline_key import inline_keyboard

logger = logging.getLogger(__name__)

router: Router = Router()


@router.message(filters.CommandStart())
async def get_start(message: types.Message, i18n, event_from_user: types.User) -> None:
    buttons = list(i18n.LEXICON.get('keyboard').keys())[:2]
    build = inline_keyboard(
        event_from_user,
        (1, 1),
        **{k: i18n.LEXICON.get('keyboard')[k] for k in buttons}
    )
    await message.answer(text=i18n.LEXICON['/start'], reply_markup=build.as_markup())


