from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

star =  InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Технологии', callback_data='technology')],
    [InlineKeyboardButton(text = 'Спорт',callback_data='sports')],
    [InlineKeyboardButton(text = 'Политика',callback_data='Politics')],
    [InlineKeyboardButton(text = 'Топ',callback_data='top')],
    [InlineKeyboardButton(text = 'Бизнес',callback_data='business')],
    [InlineKeyboardButton(text = 'Наука',callback_data='science')],
])
