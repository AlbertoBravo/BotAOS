#!/usr/bin/python

from random import randint
import constants
def sayHello(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hola! Bienvenidos a la charla de OpenShift")

def info(bot, update):

    bot.send_message(chat_id=update.message.chat_id, text="Informacion de openshift.")

def photo (bot, update):
    bot.send_photo(chat_id=update.message.chat_id, photo=constants.AOS_IMAGES[randint(0, constants.AOS_IMAGES.__len__()-1)])