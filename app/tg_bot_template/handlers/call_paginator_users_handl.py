import logging

from aiogram import Router, types, F

from app.tg_bot_template.configs.config import DataVid
from app.tg_bot_template.data_base.model import list_all_table
from app.tg_bot_template.data_base.orm import update_data_base
from app.tg_bot_template.filters.filters_obj import FirstElem, FilterFlag
from app.tg_bot_template.keyboards.callback_factory import CallbackFactory
from app.tg_bot_template.keyboards.inline_key import inline_keyboard
from app.tg_bot_template.services import find_category

logger = logging.getLogger(__name__)

router: Router = Router()

@router.callback_query(CallbackFactory.filter('1' == F.data_call), FilterFlag())
async def call_next_pag(
        callback: types.CallbackQuery,
        update_base: update_data_base,
        i18n,
        event_from_user: types.User,
        data_vid: DataVid,
        flag: str
) -> None:
    logger.debug('init call_next_pag')
    try:
        test = list(data_vid.sheet_apt)[int(flag)+ 1]
    except Exception as e:
        logger.debug(f'{e}')
        await callback.answer(text=i18n.LEXICON['not_next'], show_alert=True)
    else:
        logger.debug(f'not except')
        update_base(
            'base',
            'users_page',
            'page',
            'page + 1',
            if_=f" WHERE user_id = {event_from_user.id}"
        )

        buttons = list(i18n.LEXICON.get('keyboard').get('pagination'))
        build = inline_keyboard(
            event_from_user,
            (3, 1, 1),
            **{k: i18n.LEXICON.get('keyboard').get('pagination')[k] for k in buttons}
        )


        category = find_category(list_all_table, event_from_user)
        logger.debug(f'{category}')
        match category:
            case 'all':
                await callback.message.edit_text(
                    text=i18n.widget(*list(data_vid.sheet_all)[int(flag) + 1]),
                    reply_markup=build.as_markup())
            case 'whe':
                await callback.message.edit_text(
                    text=i18n.widget(*list(data_vid.sheet_whe)[int(flag) + 1]),
                    reply_markup=build.as_markup())
            case 'apt':
                await callback.message.edit_text(
                    text=i18n.widget(*list(data_vid.sheet_apt)[int(flag) + 1]),
                    reply_markup=build.as_markup())
            case 'prod':
                await callback.message.edit_text(
                    text=i18n.widget(*list(data_vid.sheet_prod)[int(flag)+ 1]),
                    reply_markup=build.as_markup())
            case 'gost':
                await callback.message.edit_text(
                    text=i18n.widget(*list(data_vid.sheet_gost)[int(flag) + 1]),
                    reply_markup=build.as_markup())
            case 'con':
                await callback.message.edit_text(
                    text=i18n.widget(*list(data_vid.sheet_con)[int(flag) + 1]),
                    reply_markup=build.as_markup())





@router.callback_query(CallbackFactory.filter('-1' == F.data_call), FirstElem())
async def call_back_pag(
callback: types.CallbackQuery,
        update_base: update_data_base,
        i18n,
        event_from_user: types.User,
        data_vid: DataVid,
        flag: str
) -> None:
    logger.debug('init call_back_pag')
    if flag != 0:

        update_base(
            'base',
            'users_page',
            'page',
            'page - 1',
            if_= f" WHERE user_id = {event_from_user.id}"
        )

        buttons = list(i18n.LEXICON.get('keyboard').get('pagination'))
        build = inline_keyboard(
            event_from_user,
            (3, 1, 1),
            **{k: i18n.LEXICON.get('keyboard').get('pagination')[k] for k in buttons}
        )
        category = find_category(list_all_table, event_from_user)

        logger.debug(f'{category}')
        match category:
            case 'all':
                await callback.message.edit_text(
            text=i18n.widget(*list(data_vid.sheet_all)[int(flag) - 1]),
            reply_markup=build.as_markup())
            case 'whe':
                await callback.message.edit_text(
            text=i18n.widget(*list(data_vid.sheet_whe)[int(flag) - 1]),
            reply_markup=build.as_markup())
            case 'apt':
                await callback.message.edit_text(
            text=i18n.widget(*list(data_vid.sheet_apt)[int(flag) - 1]),
            reply_markup=build.as_markup())
            case 'prod':
                await callback.message.edit_text(
            text=i18n.widget(*list(data_vid.sheet_prod)[int(flag) - 1]),
            reply_markup=build.as_markup())
            case 'gost':
                await callback.message.edit_text(
            text=i18n.widget(*list(data_vid.sheet_gost)[int(flag) - 1]),
            reply_markup=build.as_markup())
            case 'con':
                await callback.message.edit_text(
            text=i18n.widget(*list(data_vid.sheet_con)[int(flag) - 1]),
            reply_markup=build.as_markup())


    else:
        await callback.answer(text=i18n.LEXICON['not_back'], show_alert=True)


