import telebot
import os
from telebot import types

TOKEN = os.getenv("8593772515:AAGQyWkY35f4SKJsHLlDxY5_CYb_2sN8NL4")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Утро 8:00", "Вечер 17:00", "Сейчас")

    bot.send_message(
        message.chat.id,
        "🚦 Дороги Омска\nВыберите режим:",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda message: True)
def handle(message):
    if message.text == "Утро 8:00":
        bot.send_message(message.chat.id, "Сбор информации по состоянию на 8:00")
    elif message.text == "Вечер 17:00":
        bot.send_message(message.chat.id, "Сбор информации по состоянию на 17:00")
    elif message.text == "Сейчас":
        bot.send_message(message.chat.id, "Сбор информации на текущий момент")
    else:
        bot.send_message(message.chat.id, "Выберите кнопку")

bot.infinity_polling()


