import logging

from aiogram import Router, types, F

from app.tg_bot_template.data_base import list_all_table
from app.tg_bot_template.keyboards.callback_factory import CallbackFactory
from app.tg_bot_template.keyboards.inline_key import inline_keyboard
from app.tg_bot_template.configs.config import DataVid
from app.tg_bot_template.data_base.orm import insert_data_base, delete_data_base_filed
logger = logging.getLogger(__name__)

router: Router = Router()


@router.callback_query(CallbackFactory.filter('next' == F.data_call))
async def call_next(callback: types.CallbackQuery, i18n, event_from_user: types.User) -> None:
    logger.debug('init call_next')
    buttons = list(i18n.LEXICON.get('keyboard'))[2:5]
    build = inline_keyboard(
        event_from_user,
        (1, 1, 1),
        **{k: i18n.LEXICON.get('keyboard')[k] for k in buttons}
    )
    await callback.message.edit_text(text=i18n.LEXICON['call_next'], reply_markup=build.as_markup())

@router.callback_query(CallbackFactory.filter('next_web' == F.data_call))
async def call_requests_detailed_filter(callback: types.CallbackQuery, event_from_user, i18n):
    if callback.message.text != '❌ Продолжить в веб.версии':
        await callback.answer(text=i18n.LEXICON['not_func'], show_alert=True)
    else:
        logger.warning(
            f'Пользователь {event_from_user.first_name, event_from_user.id} нажимает множество раз подряд на {callback.message.text}'
        )
        await callback.answer(text=i18n.LEXICON['exp_buttons'], show_alert=True)

@router.callback_query(CallbackFactory.filter('detailed_filter' == F.data_call))
async def call_requests_detailed_filter(callback: types.CallbackQuery, event_from_user, i18n):
    if callback.message.text != '❌ Подробная фильтрации':
        await callback.answer(text=i18n.LEXICON['not_func'], show_alert=True)
    else:
        logger.warning(
            f'Пользователь {event_from_user.first_name, event_from_user.id} нажимает множество раз подряд на {callback.message.text}'
        )
        await callback.answer(text=i18n.LEXICON['exp_buttons'], show_alert=True)


@router.callback_query(CallbackFactory.filter('requests_filter' == F.data_call))
async def call_requests_filter(callback: types.CallbackQuery, i18n, event_from_user: types.User) -> None:
    if callback.message.text != 'Фильтрации по виду заведения':
        logger.debug('init call requests filter')

        buttons = list(i18n.LEXICON.get('keyboard'))[7:12]
        button_cancel = ''.join(list(i18n.LEXICON.get('keyboard'))[6])
        buttons += [button_cancel]
        logger.debug('init buttons')

        build = inline_keyboard(
            event_from_user,
            sizes=(1,),
            **{k: i18n.LEXICON.get('keyboard')[k] for k in buttons}
        )
        await callback.message.edit_text(text=i18n.LEXICON['call_req_fil'], reply_markup=build.as_markup())
    else:
        logger.warning(
            f'Пользователь {event_from_user.first_name, event_from_user.id} нажимает множество раз подряд на {callback.message.text}'
        )
        await callback.answer(text=i18n.LEXICON['exp_buttons'], show_alert=True)

@router.callback_query(CallbackFactory.filter('cancel' == F.data_call))
async def call_cancel(callback: types.CallbackQuery, i18n, event_from_user: types.User, delete_base: delete_data_base_filed):
    if callback.message.text != 'Вернуться':

        delete_base('base', 'users_page', if_= f" WHERE user_id = {event_from_user.id}")
        await call_next(callback, i18n, event_from_user)
    else:
        logger.warning(
            f'Пользователь {event_from_user.first_name, event_from_user.id} нажимает множество раз подряд на {callback.message.text}'
        )
        await callback.answer(text=i18n.LEXICON['exp_buttons'], show_alert=True)


@router.callback_query(CallbackFactory.filter('random' == F.data_call))
async def call_random(
        callback: types.CallbackQuery,
        i18n,
        event_from_user: types.User,
        data_vid: DataVid,
        insert_base: insert_data_base
) -> None:
    logger.debug('init call_random')

    insert_base('base', "users_page (user_id, page) VALUES (?, ?)", int(event_from_user.id), 1)
    logger.debug(f'{list_all_table('base', '*', 'users_page')}')

    buttons = list(i18n.LEXICON.get('keyboard').get('pagination'))
    build = inline_keyboard(
        event_from_user,
        (3, 1, 1),
        **{k: i18n.LEXICON.get('keyboard').get('pagination')[k] for k in buttons}
    )
    await callback.message.edit_text(text=i18n.widget(*list(data_vid.sheet_all)[0]), reply_markup=build.as_markup())


@router.callback_query(CallbackFactory.filter('ch_food' == F.data_call))
async def call_whe(
        callback: types.CallbackQuery,
        i18n,
        event_from_user: types.User,
        data_vid: DataVid,
        insert_base: insert_data_base
) -> None:
    logger.debug('init_call_whe')

    insert_base('base', "users_page (user_id, page) VALUES (?, ?)", int(event_from_user.id), 1)
    logger.debug(f'{list_all_table('base', '*', 'users_page')}')

    buttons = list(i18n.LEXICON.get('keyboard').get('pagination'))
    build = inline_keyboard(
        event_from_user,
        (3, 1, 1),
        **{k: i18n.LEXICON.get('keyboard').get('pagination')[k] for k in buttons}
    )

    await callback.message.edit_text(text=i18n.widget(*list(data_vid.sheet_whe)[0]), reply_markup=build.as_markup())



@router.callback_query(CallbackFactory.filter('sail' == F.data_call))
async def call_prod(
        callback: types.CallbackQuery,
        i18n,
        event_from_user: types.User,
        data_vid: DataVid,
        insert_base: insert_data_base
) -> None:
    logger.debug('init_call_prod')

    insert_base('base', "users_page (user_id, page) VALUES (?, ?)", int(event_from_user.id), 1)
    logger.debug(f'{list_all_table('base', '*', 'users_page')}')

    buttons = list(i18n.LEXICON.get('keyboard').get('pagination'))
    build = inline_keyboard(
        event_from_user,
        (3, 1, 1),
        **{k: i18n.LEXICON.get('keyboard').get('pagination')[k] for k in buttons}
    )

    await callback.message.edit_text(text=i18n.widget(*list(data_vid.sheet_prod)[0]), reply_markup=build.as_markup())


@router.callback_query(CallbackFactory.filter('apt' == F.data_call))
async def call_apt(
        callback: types.CallbackQuery,
        i18n,
        event_from_user: types.User,
        data_vid: DataVid,
        insert_base: insert_data_base
) -> None:
    logger.debug('init_call_apt')

    insert_base('base', "users_page (user_id, page) VALUES (?, ?)", int(event_from_user.id), 1)
    logger.debug(f'{list_all_table('base', '*', 'users_page')}')

    buttons = list(i18n.LEXICON.get('keyboard').get('pagination'))
    build = inline_keyboard(
        event_from_user,
        (3, 1, 1),
        **{k: i18n.LEXICON.get('keyboard').get('pagination')[k] for k in buttons}
    )

    await callback.message.edit_text(text=i18n.widget(*list(data_vid.sheet_apt)[0]), reply_markup=build.as_markup())


@router.callback_query(CallbackFactory.filter('con' == F.data_call))
async def call_con(
        callback: types.CallbackQuery,
        i18n,
        event_from_user: types.User,
        data_vid: DataVid,
        insert_base: insert_data_base
) -> None:
    logger.debug('init_call_con')

    insert_base('base', "users_page (user_id, page) VALUES (?, ?)", int(event_from_user.id), 1)
    logger.debug(f'{list_all_table('base', '*', 'users_page')}')

    buttons = list(i18n.LEXICON.get('keyboard').get('pagination'))
    build = inline_keyboard(
        event_from_user,
        (3, 1, 1),
        **{k: i18n.LEXICON.get('keyboard').get('pagination')[k] for k in buttons}
    )

    await callback.message.edit_text(text=i18n.widget(*list(data_vid.sheet_con)[0]), reply_markup=build.as_markup())

@router.callback_query(CallbackFactory.filter('gost' == F.data_call))
async def call_gost(
        callback: types.CallbackQuery,
        i18n,
        event_from_user: types.User,
        data_vid: DataVid,
        insert_base: insert_data_base
) -> None:
    logger.debug('init_call_gost')

    insert_base('base', "users_page (user_id, page) VALUES (?, ?)", int(event_from_user.id), 1)
    logger.debug(f'{list_all_table('base', '*', 'users_page')}')

    buttons = list(i18n.LEXICON.get('keyboard').get('pagination'))
    build = inline_keyboard(
        event_from_user,
        (3, 1, 1),
        **{k: i18n.LEXICON.get('keyboard').get('pagination')[k] for k in buttons}
    )

    await callback.message.edit_text(text=i18n.widget(*list(data_vid.sheet_gost)[0]), reply_markup=build.as_markup())
