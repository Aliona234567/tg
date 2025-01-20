import telebot
import pandas as pd
import datetime

# Инициализация бота с токеном
bot = telebot.TeleBot('7718775834:AAHxC_Ie9vspc-68sCM9Tb8U30kG74_HnD8')

# Загрузка расписания из Excel
df = pd.read_excel('schedule.xlsx')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Введите номер группы и дату в формате Группа ГГГГ-ММ-ДД (например, 101 2023-10-15).")

# Обработчик ввода группы и даты
@bot.message_handler(func=lambda message: True)
def send_schedule(message):
    try:
        # Разделение ввода на группу и дату
        group, date = message.text.split()
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

        # Поиск расписания по группе и дате
        schedule = df[(df['Группа'] == int(group)) & (df['Дата'] == pd.to_datetime(date))]

        if not schedule.empty:
            bot.reply_to(message, schedule.to_string(index=False))
        else:
            bot.reply_to(message, "Расписание не найдено.")
    except Exception as e:
        bot.reply_to(message, "Ошибка ввода. Пожалуйста, введите данные в формате: Группа ГГГГ-ММ-ДД.")

# Запуск бота
bot.polling()