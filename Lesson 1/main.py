from aiogram import Bot, Dispatcher, executor,types

TOKEN_API="7907045825:AAEpBxDO9XcoXvWJY0IiKpPi-BbC6xd47Sg" 
bot = Bot(TOKEN_API)
dp= Dispatcher(bot)


@dp.message_handler( )
async def echo(massage:types.Message):
    await massage.answer(text=massage.text)



if __name__ == '__main__':
    executor.start_polling(dp)
  


