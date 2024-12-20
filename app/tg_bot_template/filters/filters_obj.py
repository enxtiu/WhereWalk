import logging

from aiogram import filters, types
from app.tg_bot_template.data_base.model import list_all_table

logger = logging.getLogger(__name__)

class FirstElem(filters.BaseFilter):

    async def __call__(self, callback: types.CallbackQuery) -> bool | dict[str, str]:

        all_table = list_all_table(
            'base',
            '*',
            'users_page',
        )

        logger.debug(f'{all_table}')
        if all_table:
            for i in all_table:
                if i[0] == callback.from_user.id:
                    if i[1] != 1:
                        return {'flag': i[1]}
                    else:
                        return {'flag': i[1]}
        else: return False

class FilterFlag(filters.BaseFilter):

    async def __call__(self, callback: types.CallbackQuery) -> bool | dict[str, str]:

        all_table = list_all_table(
            'base',
            '*',
            'users_page',
        )

        logger.debug(f'{all_table}')
        if all_table:
            for i in all_table:
                if i[0] == callback.from_user.id:
                    logger.debug(f'{i[1]}')
                    return {'flag': i[1]}
        else:
            return False
        return False