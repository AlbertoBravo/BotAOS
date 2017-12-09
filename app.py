import telegram
import commands
import logging
from telegram.ext import (Updater, CommandHandler)

TOKEN = '487700234:AAEliQqFsDZXpcymDqCOzLQBQOdUyumCR_U'

def main():

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    t_bot = telegram.Bot(token=TOKEN)
    print (t_bot.get_me())
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    foto_handler = CommandHandler('foto', commands.photo)

    start_handler = CommandHandler('start', commands.sayHello)
    info_handler = CommandHandler('info', commands.info)



    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(info_handler)
    dispatcher.add_handler(foto_handler)


    updater.start_polling()

if __name__ == '__main__':
    main()
