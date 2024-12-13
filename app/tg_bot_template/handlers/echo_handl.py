import logging

from aiogram import Router, types



logger = logging.getLogger(__name__)

router: Router = Router()

@router.message()
async def echo(message: types.Message) -> None:
    await message.answer(text=...)