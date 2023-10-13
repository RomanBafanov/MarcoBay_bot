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
TIME_START = int(os.getenv('TIME_START'))


@bot.message_handler(commands=['start'])
def bot_start(message: Message) -> None:
    """
    Команда /start. При вызове команды запускается бот и приветствуется пользователь.
    :param message: Сообщение пользователя (ввод команды /start)
    :return: None
    """

    bot.reply_to(message, f"Добрый день {message.from_user.full_name}!\n"
                          f"👋Мы рады, что Вы выбрали наш бренд Marco bay.")

    time.sleep(TIME_START)
    bot.reply_to(message, 'Для наших покупателей мы подготовили подарок от MARCO BAY! '
                          '🎁 Его можно забрать по кнопке ниже! 👇')

    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = types.KeyboardButton('Подарок')
    item2 = types.KeyboardButton('Подписаться')
    keyboard.add(item1, item2)
    time.sleep(TIME_START)
    bot.reply_to(message, '💃А еще у нас есть ЗАКРЫТЫЙ канал бренда MARCO BAY, '
                          'где наши подписчики самыми первыми узнают о сезонных РАСПРОДАЖАХ, '
                          'получают дополнительные СКИДКИ и ПРОМОКОДЫ на товары MARCO BAY! '
                          'Подписывайся и узнавай о всех скидках ПЕРВЫМ! 🛍', reply_markup=keyboard)
