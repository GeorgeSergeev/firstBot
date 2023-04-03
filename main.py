from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = 'DDDDDDDD:CCCCCCCCCCCCCCCCCCCCCCCCC' #В одинарных кавычках размещаем токен, полученный от @BotFather
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) #Явно указываем в декораторе, на какую команду реагируем. 
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ ваш папа-бот и расскажу что будет на ужин") #Так как код работает асинхронно, то обязательно пишем await.


@dp.message_handler() #Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def echo(message: types.Message): #Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
   await message.answer('Я не умею готовить '+message.text)   

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)   