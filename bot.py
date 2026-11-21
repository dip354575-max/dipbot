import os
import threading
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

GROUP_LINK = "https://t.me/+8y26BPvA2XY3OWY1"
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Running!"

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        text = "GROUP ONLY FEATURE\n\nTHIS COMMAND WORKS ONLY IN THE OFFICIAL GROUP\n\nCLICK BELOW TO JOIN AND USE /pair THERE"
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Join Official Group", url=GROUP_LINK))
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Hello! Group e welcome\n/pair likho Pair Code er jonno")

@bot.message_handler(commands=['pair'])
def pair(message):
    if message.chat.type == 'private':
        text = "Ei command sudhu group e kaj korbe!"
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Join Official Group", url=GROUP_LINK))
        bot.send_message(message.chat.id, text, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Tomar number ta pathao")

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
