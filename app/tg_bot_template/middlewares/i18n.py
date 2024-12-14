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


        user_lang = user.language_code
        translation = data.get('_translation')

        i18n = translation.get(user_lang)

        if i18n is None:
            data['i18n'] = translation['default']
        else:
            data['i18n'] = i18n

        return await handler(event, data)



