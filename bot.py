import telebot
import function
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
        telebot.types.BotCommand("/flip_coin","hej"),
        telebot.types.BotCommand("/create_pass", "gah"),
        telebot.types.BotCommand("/double_letter","ouu")
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

bot.polling()
