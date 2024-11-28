# 1 Первое задание



# from aiogram import Bot, executor,Dispatcher,types
# from config import TOKEN_API
# import random
# import string
# bot=Bot(TOKEN_API)
# dp=Dispatcher(bot)


# @dp.message_handler()
# async def echo_random(message:types.Message):
#     await message.reply(random.choice(string.ascii_letters))


# if __name__== '__main__':
#     executor.start_polling(dp)




# 2 второе задание


# from aiogram import Bot, executor,Dispatcher,types
# from config import TOKEN_API



# OPISANIE="""
# /description-этот баг поможет вам найти квартиру или дом либо место жительства как вам угодно
# """
# bot=Bot(TOKEN_API)
# dp=Dispatcher(bot)


# @dp.message_handler(commands=['description'])
# async def echo(message:types.Message):
#     await message.reply(OPISANIE)
#     await message.delete()




# if __name__== '__main__':
#     executor.start_polling(dp)





# 3 второе задание



# from aiogram import Bot, executor,Dispatcher,types
# from config import TOKEN_API


# bot=Bot(TOKEN_API)
# dp=Dispatcher(bot)
# count_ann=0

# @dp.message_handler(commands=['Count'])
# async def echo(message:types.Message):
#     global count_ann
#     count_ann +=1
#     await message.answer(F' Count: {count_ann}')




# if __name__== '__main__':
#     executor.start_polling(dp)


# 4 второе задание



# from aiogram import Bot, executor,Dispatcher,types
# from config import TOKEN_API


# bot=Bot(TOKEN_API)
# dp=Dispatcher(bot)

# @dp.message_handler()
# async def echo(message:types.Message):
#     if "0" in message.text:
#         await message.reply('yes')
#     else:
#         await message.reply('nou')




# if __name__== '__main__':
#     executor.start_polling(dp)
