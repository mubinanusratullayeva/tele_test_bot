import os
import telebot
from dotenv import load_dotenv
data = load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f"{message.from_user.first_name}")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, f"{message}")

if __name__ == "__main__":
    bot.infinity_polling()
