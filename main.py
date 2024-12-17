from aiogram import Bot,Dispatcher
from config import load_config
import asyncio
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import keyboard
from func import *

config = load_config('.env')
bot_token = config.token
bot = Bot(token=bot_token)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Это сводка новостей📰\nПо какому разделу хочешь получить новости?',
                         reply_markup=keyboard.star)

@dp.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer('Раздел в разработке')

@dp.callback_query()
async def cmn_button(callback: CallbackQuery):
    res = func(callback.data)
    if len(res) > 5:
        res = res[:3]
    await callback.message.answer("\n===================================\n".join('\n'.join(i) for i in res))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass