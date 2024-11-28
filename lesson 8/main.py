from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb=ReplyKeyboardMarkup(resize_keyboard=True,
                       one_time_keyboard=True )
b1=KeyboardButton('/help')
b2=KeyboardButton('/description')
b3=KeyboardButton('/photo')
kb.add(b1).insert(b2).add(b3)

async def on_startup(_):
    print('Я запустился')  


HELP_COMMAND="""
<b>/help</b> - <em> список команд</em>
<b>/start</b> - <em> старт бота</em>
<b>/description</b> - <em> описание бота</em>
<b>/photo</b> - <em> отправка фото</em>  """ 

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=HELP_COMMAND,
                           parse_mode='HTML')
    await message.delete()
    

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='добро пожаловать',
                           parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()
    

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='описание нашего работы',
                           parse_mode='HTML')
    await message.delete()
    

@dp.message_handler(commands=['photo'])
async def photo_command(message: types.Message):
    await bot.send_message(message.chat.id,
                           text='вот так выглядит Zhakup',)
    await bot.send_photo(message.chat.id,
                           photo='https://img.freepik.com/premium-photo/monkey-riding-bicycle-tennis-court_846485-36549.jpg')
    await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp,on_startup=on_startup, skip_updates=True)
