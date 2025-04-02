import telebot
import random
import function, function_2,function_3

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7727847168:AAF8jIYtO2YX5iMjuJzWHUYtH8wXI5yPT28")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['create_pass'])
def send_bye(message):
    bot.reply_to(message, function.gen_pass())

@bot.message_handler(commands=['watch_movies'])
def send_bye(message):
    bot.reply_to(message, "https://www.fullhdfilmizlesene.de/")


@bot.message_handler(commands=['coin_flip'])
def send_bye(message):
    bot.reply_to(message, function_2.flip_coin())

@bot.message_handler(commands=['double-letter'])
def send_bye(message):
    bot.reply_to(message, function_3.double_letter())



'''
@bot.message_handler(commands=['watch_movies'])
def send_bye(message):
    bot.reply_to(message, random.choice([_-_,-_-]))'''


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
print('start')

bot.polling()