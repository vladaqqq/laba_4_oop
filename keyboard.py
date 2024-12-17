from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

star =  InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'IT', callback_data='IT')],
    [InlineKeyboardButton(text = 'Музыка',callback_data='Music')],
    [InlineKeyboardButton(text = 'Искусство',callback_data='Art')],
    [InlineKeyboardButton(text = 'Политика',callback_data='Politics')]
])