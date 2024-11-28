# 1 Задание

# from aiogram import Bot,executor,Dispatcher,types
# from config import TOKEN_API

# bot=Bot(TOKEN_API)
# dp=Dispatcher(bot)


# @dp.message_handler(commands=['give'])
# async def stikert_look(message:types.Message):
#     await message.reply(text='смотри какой котик'+'❤️' )
#     await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAENEoZnKQimbQ3hdsKlsdKTgvuXVJ2yFQACeBQAAokOQUvMGMzwzDHFyDYE')
#     await message.delete()



# if __name__=='__main__':
#     executor.start_polling(dp)



# # 2 Задание

# from aiogram import Bot,executor,Dispatcher,types
# from config import TOKEN_API

# bot=Bot(TOKEN_API)
# dp=Dispatcher(bot)


# @dp.message_handler()
# async def stikert_look(message:types.Message):
#     if message.text=='❤️':
#         await message.answer(text="🖤")
#         await message.delete()    



# if __name__=='__main__':
#     executor.start_polling(dp)



# 3 Задание

# from aiogram import Bot,executor,Dispatcher,types
# from config import TOKEN_API

# bot=Bot(TOKEN_API)
# dp=Dispatcher(bot)


# @dp.message_handler()
# async def count(message:types.Message):
#         await message.reply(text=str(message.text.count('☑️')))
        
 



# if __name__=='__main__':
#     executor.start_polling(dp)




# 4 Задание



# from aiogram import Bot, executor, Dispatcher, types
# from config import TOKEN_API

# bot = Bot(TOKEN_API)
# dp = Dispatcher(bot)
# async def on_startup(_):
#     print('Я запустился')


# # Инициализация счетчика вызовов команды /Count
# count_ann = 0


# @dp.message_handler(commands=['help'])
# async def help_command(message: types.Message):
#     await message.reply("Список доступных команд:'/help - список команд<br>''/START - начать работу с ботом<br>''/Count - подсчет вызовов команды<br>''/description - этот баг поможет вам найти квартиру или дом либо место жительства как вам угодно<br>''/stiker - может отправить вам милого котёнка'",parse_mode='HTML')

# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await message.answer(text='Добро пожаловать в наш Telegram бот!')
#     await message.delete()

# @dp.message_handler(commands=['Count'])
# async def count_command(message: types.Message):
#     global count_ann
#     count_ann += 1
#     await message.answer(f'Count: {count_ann}')

# @dp.message_handler(commands=['stiker'])
# async def sticker_command(message: types.Message):
#     await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAENEoZnKQimbQ3hdsKlsdKTgvuXVJ2yFQACeBQAAokOQUvMGMzwzDHFyDYE')
#     await message.delete()

# @dp.message_handler(commands=['description'])
# async def echo(message:types.Message):
#     await message.reply('этот баг поможет вам найти квартиру или дом либо место жительства как вам угодно')
#     await message.delete()


# if __name__ == '__main__':
#     executor.start_polling(dp,on_startup=on_startup)



# 5 Задание



from aiogram import Bot, executor, Dispatcher, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
async def on_startup(_):
    print('Я запустился')


@dp.message_handler(content_types=['sticker'])
async def stiker_id(message: types.Message):
    await message.reply(message.sticker.file_id)


if __name__ == '__main__':
    executor.start_polling(dp,on_startup=on_startup)
