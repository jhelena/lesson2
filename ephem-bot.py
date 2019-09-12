from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import datetime
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
planets = ['Mercury','Venus', 'Mars','Jupiter','Saturn', 'Uranus', 'Neptune']

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet))
    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def planet(bot, update):
    user_text = update.message.text
    split_text = user_text.split()
    name_planet = split_text[1]
    #print(name_planet)
    name_planet = name_planet.capitalize()
    print(name_planet)
    if name_planet in planets:
        now = datetime.datetime.now()
        #print(now)
        now=str(now)
        split_now=now.split()
        #print(split_now)
        now=str(split_now[0])
        print(now)
        get_const= getattr(ephem,name_planet)
        planet = get_const(now)
        const = ephem.constellation(planet)
        print(const)
    else:
        const='Нет такой планеты!'
    update.message.reply_text(const)

main()
