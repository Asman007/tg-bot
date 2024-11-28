from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API

bot=Bot(TOKEN_API)
dp= Dispatcher(bot)

@dp.message_handler()
async def acho_upper(message: types.Message):
    if message.text.count(' ')>=1:
        await message.answer(text=message.text.upper())

    else:
        await message.answer(text='idi naxui')
    

if __name__ == '__main__':
    executor.start_polling(dp)