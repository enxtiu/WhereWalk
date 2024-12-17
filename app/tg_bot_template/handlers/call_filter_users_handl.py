import logging
from itertools import repeat

from aiogram import Router, types, F

from app.tg_bot_template.keyboards.callback_factory import CallbackFactory
from app.tg_bot_template.keyboards.inline_key import inline_keyboard

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
    await call_next(callback, i18n, event_from_user)

@router.callback_query(CallbackFactory.filter('random' == F.data_call))
async def call_random(callback: types.CallbackQuery) -> None:
    logger.debug('init call_random')
    await callback.answer(text='12345')