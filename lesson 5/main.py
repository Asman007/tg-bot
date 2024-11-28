from aiogram import Dispatcher, executor, Bot, types
from config import TOKEN_API


bot=Bot(TOKEN_API)
dp=Dispatcher(bot)

async def on_startup(_):
    print('болт успешно запущен!')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('<b>добро пожаловать бот по поиску жилья</b>',parse_mode='HTML') 



@dp.message_handler(commands=['stiker'])
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAENEoZnKQimbQ3hdsKlsdKTgvuXVJ2yFQACeBQAAokOQUvMGMzwzDHFyDYE')
    await message.delete()


@dp.message_handler()
async def start_command(message: types.Message):
    await message.reply(text='Я тоже вас люблю'+'❤️') 
    


if __name__== '__main__':
    executor.start_polling(dp, on_startup=on_startup)
