from aiogram import Bot, Dispatcher,executor,types


bot = Bot('6421031230:AAFcDsnmxbZn62h9UOL_h605amDSwOkMRRA')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Hello')
    await message.answer('hello')

executor.start_polling(dp)




# bot.polling(non_stop=True)