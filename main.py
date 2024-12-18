from aiogram import Bot,Dispatcher
from config import load_config
import asyncio
from aiogram.types import Message, CallbackQuery, BotCommand
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
    await callback.message.answer("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n".join('\n'.join(i) for i in res))

@dp.message(Command('news'))
async def cmn_again(message: Message):
    await message.answer('По какому разделу хочешь получить новости?', reply_markup=keyboard.star)

async def set_main_menu():
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/news',
                   description='Посмотреть другие новости'),
        BotCommand(command='/start',
                   description='Запустить бота'),
    ]

    await bot.set_my_commands(main_menu_commands)


dp.startup.register(set_main_menu)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass