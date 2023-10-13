import os
from telebot.types import Message
from loader import bot
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()
TG = os.getenv('TG')

@bot.message_handler(commands=['marco_bay_tg'])
def bot_start(message: Message) -> None:
    bot.reply_to(message, TG)