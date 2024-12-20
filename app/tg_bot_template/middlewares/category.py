import logging

from aiogram import BaseMiddleware, types

from typing import Callable, Awaitable

from app.tg_bot_template.data_base.model import list_all_table

logger = logging.getLogger(__name__)

class InfoCategory[T](BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[types.TelegramObject, dict[str, T]], Awaitable[T]],
            event: types.TelegramObject,
            data: dict[str, T]
    ) -> T:

        result = await handler(event, data)

        all_table = list_all_table(
            'base',
            '*',
            'users_page',
        )
        user: types.User = data['event_from_user']

        logger.debug(f'{all_table}')
        for i in all_table:
            logger.debug(f'{user.id}')
            if user.id == i[0]:
                logger.debug(f'{i, i[2]}')
                data['category'] = i[2]

        return result
