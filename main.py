import telebot
from telebot import types

bot = telebot.TeleBot('7718775834:AAHxC_Ie9vspc-68sCM9Tb8U30kG74_HnD8')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1= types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 =types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    # в третьем видио расказываеться как отпровлять пользователю фото видио стикиры и прочее
    bot.send_message(message.chat.id, 'Приыет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Site open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'фОТО УДАЛЕНРО')

@bot.message_handler(content_types=['photo','audio'])
def get_photo (message):
    markup = types.InlineKeyboardMarkup()
    btn1= types.InlineKeyboardButton('Перейти на сайт', url='https://open-college.ru')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 =types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)

    bot.reply_to(message, 'Красатища какая', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id , callback.message.message_id - 1)
    elif callback.data =='edit':
        bot.edit_message_text('Edyt text', callback.message.chat.id , callback.message.message_id)



bot.polling(none_stop=True)
