import logging

from typing import Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import User, TelegramObject

logger = logging.getLogger(__name__)

class TranslatorMiddleware[T](BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, T]], Awaitable[T]],
            event: TelegramObject,
            data: dict[str, T]
    ) -> T:

        user: User = data.get('event_from_user')

        if user is None:
            return await handler(event, data)


