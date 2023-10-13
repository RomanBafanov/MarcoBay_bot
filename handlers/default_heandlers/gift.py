import os
import time
from loader import bot
from telebot import types
from telebot.types import Message
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()
TG = os.getenv('TG')
URL = os.getenv('URL')
TIME_REMINBER = int(os.getenv('TIME_REMINBER'))


@bot.message_handler(func=lambda message: message.text == 'Подарок')
def bot_start(message: Message) -> None:
    """
    Команда Подарок. При вызове команды бот отправляет подарок пользователю и
    через определённое время напоминает о возможности подписаться на ТГ канал.
    :param message: Сообщение пользователя (ввод команды Подарок)
    :return: None
    """

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = types.KeyboardButton('Подписаться')
    keyboard.add(item1)

    bot.reply_to(message, URL, reply_markup=keyboard)

    time.sleep(TIME_REMINBER)

    hideBoard = types.ReplyKeyboardRemove()

    bot.reply_to(message, '❗️❗️❗️Чтобы не пропустить супер СКИДКИ и СПЕЦ РАСПРОДАЖИ MARCO BAY '
                          'подпишись на закрытый канал! 👇' + TG, reply_markup=hideBoard)