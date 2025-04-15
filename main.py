from telebot import TeleBot
import os, random, memes

bot = TeleBot('7727847168:AAF8jIYtO2YX5iMjuJzWHUYtH8wXI5yPT28')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello World!')
    
@bot.message_handler(commands=['meme'])
def send_meme(message):
    file = random.choice(os.listdir('memes'))
    with open(f'memes\\{file}','rb') as f:
        bot.send_photo(message.chat.id,f)

bot.infinity_polling()
