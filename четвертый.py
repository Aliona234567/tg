import telebot
import sqlite3
from telebot import types



bot = telebot.TeleBot('7718775834:AAHxC_Ie9vspc-68sCM9Tb8U30kG74_HnD8')
name= ''

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass TEXT)')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет! Сейчас тебя зарегистрируем. Введите ваше имя:')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
   
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегестрирован!!!!!', reply_markup=markup)
    # bot.register_next_step_handler(message, user_pass)


@bot.callback_query_handler(funk=lambda call: True)
def callback(call):
    conn = sqlite3.connect('itproger.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info =''
    for el in users:
        info += f'Имя: {el[1]}, пароль:{el[2]}\n'



    cur.close()
    conn.close()

    bot.send_message(call.massage.chat.id, info)



bot.polling(none_stop=True)
