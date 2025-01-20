import telebot
import sqlite3
from telebot import types



bot = telebot.TeleBot('7718775834:AAHxC_Ie9vspc-68sCM9Tb8U30kG74_HnD8')
@bot.message_handler(commands=['start'])
def start(massage):
    bot.send_message(massage.chat.id, 'Привкт рад тебя ввидеть Напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()










bot.polling(none_stop=True)
