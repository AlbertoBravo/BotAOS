#!/usr/bin/python

from random import randint
import constants
def sayHello(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola! Bienvenidos a la charla de OpenShift")

def info(bot, update):
    mytext = "Red Hat OpenShift Online es el servicio público de alojamiento de la plataforma como servicio (PaaS) de Red Hat que ofrece una solución de desarrollo, creación, implementación y alojamiento de aplicaciones en nube."
    
    bot.send_message(chat_id=update.message.chat_id, text=mytext)

def photo (bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo=constants.AOS_IMAGES[randint(0, constants.AOS_IMAGES.__len__()-1)])
