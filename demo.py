import telebot
import webbrowser

bot = telebot.TeleBot('7718775834:AAHxC_Ie9vspc-68sCM9Tb8U30kG74_HnD8')

@bot.message_handler(commands=['site', 'website'])
def site (message):
    webbrowser.open('https://open-college.ru/')


@bot.message_handler(commands=['start', 'hello1'])
def main(message):
    bot.send_message(message.chat.id ,f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id ,'<b>Help</b> <em><u>tminfo</u></em>',parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower()== 'привет':
         bot.send_message(message.chat.id ,f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID {message.from_user.id}')


bot.polling(none_stop=True)
