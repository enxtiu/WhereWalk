import logging

from aiogram.filters.callback_data import CallbackData

logger = logging.getLogger(__name__)

class CallbackFactory(CallbackData, prefix='call'):
    user_id: int
    data: str
