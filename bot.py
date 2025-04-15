import telebot
import function, traslator_and_caliculator, get_duvk_image, random
#import time, threading, schedule
import requests
from telebot import TeleBot
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7727847168:AAF8jIYtO2YX5iMjuJzWHUYtH8wXI5yPT28")

    
    
@bot.message_handler(commands=['duck'])
def send_duck(message):
    bot.send_photo(message.chat.id, get_duvk_image.get_duck_image_url())




# Список мемов с указанием их редкости
memes = [
    {"file_id": "mem.jbg", "rarity": 70},  # Более распространенный
    {"file_id": "meme2.jbg", "rarity": 20},  # Редкий
    {"file_id": "meme3.jbg", "rarity": 10},  # Очень редкийw3
]

def get_random_meme():
    # Создаем расширенный список для учета редкости
    extended_list = []
    for meme in memes:
        extended_list.extend([meme["file_id"]] * meme["rarity"])
    # Возвращаем случайный мем
    return random.choice(extended_list)

# Команда для получения мемов
@bot.message_handler(commands=['ran_meme'])
def send_animal_meme(message):
    meme_file_id = get_random_meme()
    with open(meme_file_id, 'rb') as meme_file:
        bot.send_photo(message.chat.id, meme_file)

# Запуск бота




@bot.message_handler(commands=['cal_add'])
def send_hello(message):
    try:
        ab = message.text.split()
        #bc = message.text.split(',')
        print(ab)
        bot.reply_to(message, traslator_and_caliculator.calculator_add(ab[1], ab[2]))
        
    except:
        bot.reply_to(message, 'введите /cal_add число a и число b через пробел1')



@bot.message_handler(commands=['cal_sub'])
def send_hello(message):
    try:
        cd = message.text.split()  
        #bc = message.text.split(',')
        print(cd)
        bot.reply_to(message, traslator_and_caliculator.calculator_subtract(cd[1], cd[2]))
        
    except:
        bot.reply_to(message, 'введите /cal_sub число a и число b через пробел2')


@bot.message_handler(commands=['cal_mult'])
def send_hello(message):
    try:
        ef = message.text.split()  
        #bc = message.text.split(',')
        print(ef)
        bot.reply_to(message, traslator_and_caliculator.calculator_multiply(ef[1], ef[2]))
        
    except:
        bot.reply_to(message, 'введите /cal_mult число a и число b через пробел3')


@bot.message_handler(commands=['cal_div'])
def send_hello(message):
    try:
        gh = message.text.split()  
        #bc = message.text.split(',')
        print(gh)
        bot.reply_to(message, traslator_and_caliculator.calculator_divide(gh[1], gh[2]))
        
    except:
        bot.reply_to(message, 'введите /cal_div число a и число b через пробел4')

#advanced
'''@bot.message_handler(commands=['cal_div'])
def send_hello(message):
    try:
        gh = message.text.split()
        if len(gh) != 3:
            bot.reply_to(message, "Please provide two numbers separated by space after /cal_div.")
            return

        num1 = float(gh[1])
        num2 = float(gh[2])
        result = traslator_and_caliculator.calculator_divide(num1, num2)
        bot.reply_to(message, result)
    except ValueError:
        bot.reply_to(message, "Invalid numbers provided! Please ensure you're using numerical values.")
    except ZeroDivisionError:
        bot.reply_to(message, "Division by zero is not allowed!")
    except:
        bot.reply_to(message, "Please use /cal_div followed by two numbers separated by space.")'''






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



@bot.message_handler(commands=['flip_coin'])
def send_bye(message):
    bot.reply_to(message, function.flip_coin())

@bot.message_handler(commands=['double_letter'])
def send_bye(message):
    bot.reply_to(message, function.double_letter(message.text))




# use in for delete with the necessary scope and language_code if necessary
bot.delete_my_commands(scope=None, language_code=None)

bot.set_my_commands(
    commands= [
        telebot.types.BotCommand("/flip_coin","non"),
        telebot.types.BotCommand("/create_pass", "non"),
        telebot.types.BotCommand("/double_letter","non"),
        telebot.types.BotCommand("/watch_movies","non"),
       # telebot.types.BotCommand("/caliculator","non")
        telebot.types.BotCommand("/cal_add","non"),
        telebot.types.BotCommand("/cal_sub","non"),
        telebot.types.BotCommand("cal_mult","non"),
        telebot.types.BotCommand("/cal_div","non"),
            ],
    # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command for users
    # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
)

# check command
cmd = bot.get_my_commands(scope=None, language_code=None)
print([c.to_json() for c in cmd])



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
print('start')


'''@bot.message_handler(commands=['tanslate'])
def send_bye(message):
    try:
        mes = message.text.split()
        if mes[1] == 'eng' and mes[2] == 'hola':
            return 'hello'
    except:
        return 'didnt work'''



bot.polling()
