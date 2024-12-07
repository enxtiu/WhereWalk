import logging

from aiogram import types, F, filters, Router

from app.tg_bot_template.keyboards.inline_key import keyboard_st, keyboard_vid
from app.tg_bot_template.lexicon_data.lexicon import LEXICON_RU

logger = logging.getLogger(__name__)

router: Router = Router()


@router.message(filters.CommandStart())
async def get_start(message: types.Message) -> None:
    await message.answer(text=LEXICON_RU['/start'], reply_markup=keyboard_st)

@router.callback_query(F.data == 'watch')
async def call_watch(callback: types.CallbackQuery) -> None:
    logger.info('Call watch')
    await callback.message.edit_text(text=LEXICON_RU['vid'], reply_markup=keyboard_vid)

@router.callback_query()
async def all_call(callback: types.CallbackQuery) -> None:
    logger.info('Call any')
    await callback.answer()

