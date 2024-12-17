import logging

from aiogram.types import User
from aiogram.utils.keyboard import InlineKeyboardBuilder

from .callback_factory import CallbackFactory

logger = logging.getLogger(__name__)

def inline_keyboard(user: User, sizes: tuple[int, ...] = (1,), **kwargs: str) -> InlineKeyboardBuilder:

    build = InlineKeyboardBuilder()
    for key, value in kwargs.items():
        build.button(
            text=value,
            callback_data=CallbackFactory(
                user_id=user.id,
                data_call=key,
            ).pack()
        )
    build.adjust(*sizes)
    logger.info('return build')
    return build
