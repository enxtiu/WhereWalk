import logging

from aiogram import Router, types, Bot

logger = logging.getLogger(__name__)

router: Router = Router()

@router.message()
async def echo(message: types.Message, bot: Bot) -> None:
    logger.info('message delete')
    await bot.delete_message(message.chat.id, message.message_id)

@router.callback_query()
async def echo_call(callback: types.CallbackQuery, i18n) -> None:
    logger.critical('Inline keyboard not work')
    await callback.answer(text=i18n.LEXICON['echo_calldata'])