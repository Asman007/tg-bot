# Задача один и два

# from aiogram import Bot, executor, Dispatcher, types
# from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
# from config import TOKEN_API

# bot = Bot(TOKEN_API)
# dp = Dispatcher(bot)
# kb=ReplyKeyboardMarkup(resize_keyboard=True)
# b1=KeyboardButton('/help')
# b2=KeyboardButton('/description')
# # b3=KeyboardButton('/❤️')

# kb.add(b1,b2)


# HELP_COMMAND="""
# <b>/help</b> - <em> список команд</em>
# <b>/start</b> - <em> старт бота</em>
# <b>/description</b> - <em> описание бота</em>
# """ 


# @dp.message_handler(commands=['start'])
# async def start_command(message:types.Message):
#     await bot.send_message(chat_id=message.chat.id,
#                            text='добро пожаловать',
#                            reply_markup=kb)
#     await message.delete()
    
# @dp.message_handler(commands=['help'])
# async def help_command(message:types.Message):
#     await bot.send_message(chat_id=message.chat.id,
#                            text=HELP_COMMAND,
#                            parse_mode="HTML")
#     await message.delete()
    

# @dp.message_handler(commands=['description'])
# async def description_command(message:types.Message):
#     await bot.send_message(chat_id=message.chat.id,
#                            text='описание нашего работы')
#     await message.delete()

# @dp.message_handler()
# async def stiker_command(message:types.Message):
#     if message.text=='❤️':
#         await bot.send_sticker(chat_id=message.chat.id,sticker='CAACAgIAAxkBAAENEoZnKQimbQ3hdsKlsdKTgvuXVJ2yFQACeBQAAokOQUvMGMzwzDHFyDYE')
#         await message.delete()



# if __name__ == '__main__':
#     executor.start_polling(dp,skip_updates=True)
  




# 3 задание


from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
kb=ReplyKeyboardMarkup(resize_keyboard=True)
b1=KeyboardButton('/help')
b2=KeyboardButton('/orenge')

kb.add(b1,b2)


@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='добро пожаловать',
                           reply_markup=kb)
    await message.delete()
    
@dp.message_handler(commands=['help'])
async def help_command(message:types.Message):
    await bot.send_message(message.from_user.id)
    await message.delete()
    

@dp.message_handler(commands=['orenge'])
async def stiker_command(message:types.Message):
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker='CAACAgIAAxkBAAENEoZnKQimbQ3hdsKlsdKTgvuXVJ2yFQACeBQAAokOQUvMGMzwzDHFyDYE')
        await message.delete()



if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)