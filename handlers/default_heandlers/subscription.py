import os
from loader import bot
from telebot import types
from telebot.types import Message
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()
TG = os.getenv('TG')


@bot.message_handler(state=None, func=lambda message: message.text == 'Подписаться')
def bot_start(message: Message) -> None:
    """
        Команда Подписаться. При вызове команды бот отправляет сообщение с кнопкой подписки на ТГ канал.
        :param message: Сообщение пользователя (ввод команды Подписаться)
        :return: None
        """

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton(text='Marco bay в ТГ', url=TG)
    keyboard.add(item1)
    bot.reply_to(message, 'Вы можете подписаться на нас 👇 👇 👇', reply_markup=keyboard)