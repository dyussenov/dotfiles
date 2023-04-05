from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '5752870125:AAHNZAy0t7w84qbvuYmb3zAqmG0jboPyewk'

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print('command start activated')
    await message.reply("Привет!\nНапиши мне что-нибудь!")


executor.start_polling(dp)