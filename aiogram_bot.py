import logging

import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, executor, types

from main import Database

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    username = message.from_user.username
    print(f"{username} start bot")
    query = f"""INSERT INTO users(first_name, username) VALUES('{first_name}', '{username}')"""
    print(f"{username} {Database.connect(query, 'insert')} database")

    await message.reply(f"Hello, @{username}!")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
