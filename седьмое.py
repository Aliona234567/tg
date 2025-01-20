from aiogram import Bot, Dispatcher, types, executor

bot = Bot('7718775834:AAHxCIe9vspc-68sCM9Tb8U30kG74HnD8')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Hello')

# Запуск бота с использованием executor
executor.start_polling(dp, skip_updates=True)