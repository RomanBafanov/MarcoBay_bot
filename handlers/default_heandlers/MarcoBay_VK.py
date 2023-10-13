import os
from telebot.types import Message
from loader import bot
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()
VK = os.getenv('VK')


@bot.message_handler(commands=['marco_bay_vk'])
def bot_start(message: Message) -> None:
    bot.reply_to(message, VK)