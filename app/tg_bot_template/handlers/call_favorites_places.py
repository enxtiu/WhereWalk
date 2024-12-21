import logging

from aiogram import Router, types, F

from app.tg_bot_template.configs.config import DataVid

from app.tg_bot_template.filters.filters_obj import FilterUsersFavorites

from app.tg_bot_template.keyboards.callback_factory import CallbackFactory
from app.tg_bot_template.keyboards.inline_key import inline_keyboard

from app.tg_bot_template.data_base.orm import insert_data_base, delete_data_base_filed
from app.tg_bot_template.data_base.model import list_all_table

from app.tg_bot_template.services.servis import find_category, find_page


logger = logging.getLogger(__name__)
router: Router = Router()

@router.callback_query(CallbackFactory.filter('add_place' == F.data_call))
async def call_add_favorites(
        callback: types.CallbackQuery,
        insert_base: insert_data_base,
        i18n,
        data_vid: DataVid,
        event_from_user: types.User
) -> None:
    logger.debug('init call add favorites')

    category = find_category(list_all_table, event_from_user)

    logger.debug(f'{category}')
    match category:
        case 'all':
            insert_base(
                'base',
                "favourites_places (name_place, info, user_id) VALUES (?, ?, ?)",
                list(data_vid.sheet_all)[find_page(list_all_table, event_from_user)][0],
                '_'.join(list(data_vid.sheet_all)[find_page(list_all_table, event_from_user)]),
                int(event_from_user.id)
            )
        case 'whe':
            insert_base(
                'base',
                "favourites_places (name_place, info, user_id) VALUES (?, ?, ?)",
                list(data_vid.sheet_whe)[find_page(list_all_table, event_from_user)][0],
                '_'.join(list(data_vid.sheet_whe)[find_page(list_all_table, event_from_user)]),
                int(event_from_user.id)
            )
        case 'apt':
            insert_base(
                'base',
                "favourites_places (name_place, info, user_id) VALUES (?, ?, ?)",
                list(data_vid.sheet_apt)[find_page(list_all_table, event_from_user)][0],
                '_'.join(list(data_vid.sheet_apt)[find_page(list_all_table, event_from_user)]),
                int(event_from_user.id)
            )
        case 'prod':
            insert_base(
                'base',
                "favourites_places (name_place, info, user_id) VALUES (?, ?, ?)",
                list(data_vid.sheet_prod)[find_page(list_all_table, event_from_user)][0],
                '_'.join(list(data_vid.sheet_prod)[find_page(list_all_table, event_from_user)]),
                int(event_from_user.id)
            )
        case 'gost':
            insert_base(
                'base',
                "favourites_places (name_place, info, user_id) VALUES (?, ?, ?)",
                list(data_vid.sheet_gost)[find_page(list_all_table, event_from_user)][0],
                '_'.join(list(data_vid.sheet_gost)[find_page(list_all_table, event_from_user)]),
                int(event_from_user.id)
            )

        case 'con':
            insert_base(
                'base',
                "favourites_places (name_place, info, user_id) VALUES (?, ?, ?)",
                list(data_vid.sheet_con)[find_page(list_all_table, event_from_user)][0],
                '_'.join(list(data_vid.sheet_con)[find_page(list_all_table, event_from_user)]),
                int(event_from_user.id)
            )
    logger.debug('favorites place added')

    await callback.answer(i18n.LEXICON['add_f'], show_alert=True)



@router.callback_query(CallbackFactory.filter('favorites' == F.data_call), FilterUsersFavorites())
async def call_watch_favorites(
        callback: types.CallbackQuery,
        flag,
        i18n,
        event_from_user: types.User
) -> None:
    logger.debug(f'init call watch favorites')

    if flag:
        build = dict()
        build_2 = {'edit': 'Редактировать', 'cancel': 'Вернуться',}
        all_table = list_all_table(
            'base',
            '*',
            'favourites_places',
        )
        key = str(event_from_user.id)+'_fav_'
        count = 0
        for item in all_table:
            if item[2] == event_from_user.id:
                count += 1
                build[key+str(count)] = item[0]
        logger.debug(f'build create {all_table}')
        logger.debug(f'{build}')
        build = inline_keyboard(
            event_from_user,
            (1,) * count,
            **build
        )
        build_2 = inline_keyboard(
                event_from_user,
                (2,),
                **build_2
            )
        build.attach(build_2)
        await callback.message.edit_text(
            text=i18n.LEXICON['nots'],
            reply_markup=build.as_markup()
        )
    else:
        await callback.answer(text=i18n.LEXICON['not_fav'], show_alert=True)


@router.callback_query(CallbackFactory.filter('edit' == F.data_call))
async def call_edit_fav(
        callback: types.CallbackQuery,
        i18n,
        event_from_user: types.User
) -> None:
    build = dict()
    build_2 = {'cancel': 'Вернуться'}
    all_table = list_all_table(
        'base',
        '*',
        'favourites_places',
    )
    key = str(event_from_user.id) + '_edit_'
    count = 0
    for item in all_table:
        if item[2] == event_from_user.id:
            count += 1
            build[key + str(count)] = '❌ '+item[0]
    logger.debug(f'build create {all_table}')
    logger.debug(f'{build}')
    build = inline_keyboard(
        event_from_user,
        (1,) * count,
        **build
    )
    build_2 = inline_keyboard(
        event_from_user,
        (1,),
        **build_2
    )
    build.attach(build_2)
    await callback.message.edit_text(
        text=i18n.LEXICON['del_nots'],
        reply_markup=build.as_markup())

@router.callback_query(
    CallbackFactory.filter(F.user_id == F.data_call.split('_')[0]&F.data_call.split('_')[1] == 'edit'))
async def del_fav_place(
        callback: types.CallbackQuery,
        i18n,
        event_from_user: types.User,
        delete_base: delete_data_base_filed
) -> None:
    logger.debug('init del fav place')
    for item in callback.message.reply_markup.inline_keyboard:
        for i in item:
            if i.callback_data == callback.data:
                text = ' '.join(i.text.split(' ')[1:])
                logger.debug(f'{text}')
                delete_base(
                    'base',
                    'favourites_places',
                    f" WHERE user_id = {event_from_user.id} AND name_place = '{text}'"
                )
                await call_edit_fav(callback, i18n, event_from_user)
                return
    await callback.answer(text=i18n.LEXICON['er_del'])

@router.callback_query(CallbackFactory.filter(F.user_id == F.data_call.split('_')[0]))
async def call_watch_widget(
        callback: types.CallbackQuery,
        i18n,
        event_from_user: types.User
) -> None:
    all_table = list_all_table(
        'base',
        '*',
        'favourites_places',
    )
    build = inline_keyboard(
        event_from_user,
        (2,),
        **{'cancel': 'Вернуться'}
    )
    text = ''
    for item in callback.message.reply_markup.inline_keyboard:
        for i in item:
            if i.callback_data == callback.data:
                text = i.text
                break
    logger.debug(f'{all_table}')
    for item in all_table:
        if item[2] == event_from_user.id and item[0] == text:
            logger.debug('if True')
            info = item[1].split('_')
            await callback.message.edit_text(
                text=i18n.widget(*info), reply_markup=build.as_markup())
            return

    await callback.answer(text='Виджет не найден')
