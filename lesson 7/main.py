# from aiogram import Bot, Dispatcher, executor,types
# from config import TOKEN_API 
# bot = Bot(TOKEN_API)
# dp= Dispatcher(bot)

# HELP_COMMAND="""
# <b>/start</b>-начать пиздить деньги
# <b>/help</b>-продолжить пиздить деньги
# <b>/картинка</b>-фото zhakupa
# <b>/lokation</b>-моё местоположение
# """
# @dp.message_handler(commands=['help'])
# async def help_command(message:types.Message):
#     # await massage.answer(text=massage.text)
#     # await bot.send_message(chat_id=message.chat.id,
#     #                        text='Helloy Zhakup idi naxui')
#     await bot.send_message(chat_id=message.chat.id,
#                            text=HELP_COMMAND,
#                            parse_mode='HTML')
#     await message.delete()


# @dp.message_handler(commands=['картинка'])
# async def send_image(message:types.Message):
#     await message.reply(text='вот так выглядит Zhakupbai'+'❤️' )
#     await bot.send_photo(chat_id=message.chat.id,
#                            photo="https://img.freepik.com/premium-photo/monkey-riding-bicycle-tennis-court_846485-36549.jpg")
#     await message.delete()



# @dp.message_handler(commands=['lokation'])
# async def send_point(message:types.Message):
#     await message.reply(text='вот здесь ты находишься'+'❤️' )
#     await bot.send_location(chat_id=message.chat.id,
#                          latitude=42.81836613263204, 
#                          longitude=74.61589705720965)
#     await message.delete()


# if __name__ == '__main__':
#     executor.start_polling(dp,skip_updates=True)
  

