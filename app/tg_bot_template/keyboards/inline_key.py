import logging

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

logger = logging.getLogger(__name__)

button = [InlineKeyboardButton(
    text='Посмотреть',
    callback_data='watch'
)]
logger.info('Init keyboard_st')
keyboard_st = InlineKeyboardMarkup(inline_keyboard=[button])

buttons = [
    [
        InlineKeyboardButton(
            text='next',
            callback_data='next_vid'
        )
    ],
    [
        InlineKeyboardButton(
            text='add favourites',
            callback_data='add_vid'
        )
    ],
    [
            InlineKeyboardButton(
            text='back',
            callback_data='back_vid'
        )
    ]
]

logger.info('Init keyboard_vid')
keyboard_vid = InlineKeyboardMarkup(inline_keyboard=buttons)