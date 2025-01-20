import telebot

from currency_converter import CurrencyConverter


bot = telebot.TeleBot('7718775834:AAHxC_Ie9vspc-68sCM9Tb8U30kG74_HnD8')
currncy = CurrencyConverter()




@bot.message_handler(commands=['start'])
def start(massage):
    bot.send_message(massage.chat.id, 'Привет введите сумму')









bot.polling(none_stop=True)









