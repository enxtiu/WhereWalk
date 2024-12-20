import logging

from aiogram import Router, types, F

from app.tg_bot_template.keyboards.callback_factory import CallbackFactory

logger = logging.getLogger(__name__)

router: Router = Router()

@router.callback_query(CallbackFactory.filter('1' == F.data_call))
async def call_next_pag(callback: types.CallbackQuery) -> None:
    ...

