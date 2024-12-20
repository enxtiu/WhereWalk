import logging

from aiogram import Router, types, F

from app.tg_bot_template.keyboards.callback_factory import CallbackFactory
from app.tg_bot_template.keyboards.inline_key import inline_keyboard
from app.tg_bot_template.services.servis import count_info_list
from app.tg_bot_template.configs.config import DataVid
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


@router.callback_query(CallbackFactory.filter('requests_filter' == F.data_call))
async def call_requests_filter(callback: types.CallbackQuery, i18n, event_from_user: types.User) -> None:
    if callback.message.text != 'Фильтрации по виду заведения':
        logger.debug('init call requests filter')

        buttons = list(i18n.LEXICON.get('keyboard'))[7:]
        button_cancel = ''.join(list(i18n.LEXICON.get('keyboard'))[6])
        buttons += [button_cancel]

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
async def call_cancel(callback: types.CallbackQuery, i18n, event_from_user: types.User):
    if callback.message.text != 'Вернуться':
        await call_next(callback, i18n, event_from_user)
    else:
        logger.warning(
            f'Пользователь {event_from_user.first_name, event_from_user.id} нажимает множество раз подряд на {callback.message.text}'
        )
        await callback.answer(text=i18n.LEXICON['exp_buttons'], show_alert=True)

@router.callback_query(CallbackFactory.filter('random' == F.data_call))
async def call_random(callback: types.CallbackQuery, i18n, event_from_user: types.User, data_vid: DataVid) -> None:
    logger.debug('init call_random')

    buttons = list(i18n.LEXICON.get('keyboard').get('pagination'))

    build = inline_keyboard(
        event_from_user,
        (3,),
        **{k: i18n.LEXICON.get('keyboard').get('pagination')[k] for k in buttons}
    )
    await callback.message.edit_text(text=i18n.widget(*data_vid.sheet_all[0]), reply_markup=build.as_markup())
