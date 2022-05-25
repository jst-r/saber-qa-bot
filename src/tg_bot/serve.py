import logging

from aiogram import Bot, Dispatcher, executor, types
from calculator.calculator import eval_str

from tg_bot.auth import authorize, is_authorized
from tg_bot.text import AUTH_FAIL, AUTH_SUCCESS

# I really shouldn't be publishing a private key to a pulic repo. But this bot is only for demonstarion, and I want it to be as easy as possible to run this.
API_TOKEN = '5391576696:AAFTV7sqVHXhp7VmYUgdkJAP8WaGsPvrQw0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['login'])
async def auth(message: types.Message):
    password = message.get_args()

    if authorize(message.from_user.id, password):
        await message.answer(AUTH_SUCCESS)
    else:
        await message.answer(AUTH_FAIL)

@dp.message_handler(lambda msg: is_authorized(msg.from_user.id))
async def auth(message: types.Message):
    try:
        expr = message.text
        res = eval_str(expr)
        await message.answer(f"{expr} = {res}")
    except:
        await message.answer("Что-то пошло не так...")
    

@dp.message_handler()
async def auth(message: types.Message):
    await message.answer("Войдите в бота с помощью команды /login <пароль>")


def main():
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    main()
