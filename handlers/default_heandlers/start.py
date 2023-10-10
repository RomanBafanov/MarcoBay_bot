import os
import time
import urllib

from loader import bot
from telebot import types
from telebot.types import Message, InputMediaPhoto, InputMediaVideo


@bot.message_handler(commands=['start'])
def bot_start(message: Message) -> None:
    """
    Команда /start. При вызове команды запускается бот и приветствуется пользователь.
    :param message: сообщение пользователя (ввод команды /start)
    :return: None
    """


    bot.reply_to(message, f"Добрый день {message.from_user.full_name}!\n"
                          f"👋Мы рады, что Вы выбрали наш бренд Marco bay.")
    time.sleep(3)
    bot.reply_to(message, 'https://www.youtube.com/shorts/LQxjq23ryPs')
    time.sleep(5)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton(text='Marco bay в ВК', url='https://vk.com/marcobay')
    item2 = types.InlineKeyboardButton(text='Marco bay в ТГ', url='https://t.me/marcobay')
    keyboard.add(item1, item2)
    bot.reply_to(message, 'Вы можете подписаться на нас 👇 👇 👇', reply_markup=keyboard)
