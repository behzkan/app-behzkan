from asyncio import sleep
from random import choice, randint

from aiogram import Bot, Dispatcher, executor, types

bot = Bot('5547260249:AAFLD_t5bA5hn5QU8XXfnqSDrFZo_VhWJTk')
dp = Dispatcher(bot)


async def on_startup(_):
    print('bot started')


from handlers.user import text

text.register_msg_handler(dp)

@dp.message_handler(commands='start')
async def cmd_start(msg: types.Message):
    await msg.answer(f"Вам доступно 1 функция {msg.from_user.first_name} \n @behzkan  /compli")
    await bot.send_message(1010023968, msg)
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
