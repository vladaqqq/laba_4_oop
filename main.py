from aiogram import Bot,Dispatcher
from config import load_config


config = load_config('.env')
bot_token = config.token
bot = Bot(token=bot_token)
dp = Dispatcher()