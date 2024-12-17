import logging

from aiogram.types import User
from aiogram.utils.keyboard import InlineKeyboardBuilder

from callback_factory import CallbackFactory

logger = logging.getLogger(__name__)

def inline_keyboard(user: User, time: int, *args: str, sizes: tuple[int, ...] = (1,)) -> InlineKeyboardBuilder:

    build = InlineKeyboardBuilder()
    for item in args:
        build.button(
            text=item,
            callback_data=CallbackFactory(
                user_id=user.id,
                data=item,
                timestamp=time
            )
        )

    build.adjust(*sizes)
    return build
