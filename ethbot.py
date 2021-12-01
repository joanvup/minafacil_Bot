#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import telebot
import requests
from telebot import types

# -------------------- SETTINGS --------------------
# Your Raptoreum wallet.
wallet = "RTVPRSvDcM1R8Xqf7Gn6XNNDzRiGkboBCG"

# Telegram bot Token.
token = "2145088618:AAGul0GOmx6XCcDzVuBwGX1us9EsDM7lkew"

# List with the telegram id of the allowed users.
id_admins = [1334636275]

# Your Pool. 0 = Minafacil
pool = 0
# --------------------------------------------------

list_pools = ["http://pool.minafacil.com/site/api"]
web = ["https://pool.minafacil.com"]

# View the wallet data on Ethermine.
def minafacil(id_user):
    url = list_pools[pool] + "/currencies"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            response_json = response.json()
            hash_rate = round(float(response_json["data"]["hashrate"]) / (10 ** 6), 2)
            workers_shared = response_json["data"]["workers_shared"]
            time_last_block = response_json["data"]["timesincelast"]
            last_block = response_json["data"]["lastblock"]
            last24_block = response_json["data"]["24h_blocks"]
            difficulty = response_json["data"]["difficulty"]
            reward = response_json["data"]["reward"]
            height = response_json["data"]["height"]
           
            text_send = "BLOQUE BLOQUE BLOQUE \n\n" +
            "*Bloque :* ``` " + str(last_block) + " ```\n" + 
            "*Dificultad :* ``` " + str(difficulty) + " ```\n" + 
            "*Recompensa :* ``` " + str(reward) + " ```\n" +
            "*Altura :* ``` " + str(height) + " ```\n" +
            "*Hashrate:* ``` " + str(hash_rate) + " MH/s```\n" + 
            "*Mineros Activos:* ```" + str(workers_shared) + "```\n" + 
            "*# de bloques en 24h:* ```" + str(last24_block) + "```\n" + 
            bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

        except:
            text_send = u"\u26A0 The wallet does not exist on " + web[pool]
            bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

# We check if the user has permission.
def check_admin(id_user):
    check = id_user in id_admins
    return check

# Keyboard Telegram Bot
def keyboard(chat_id, textoEnvio):
    r1 = ["Mined"]
    keyboard = [r1]
    news_keyboard = {'keyboard': keyboard, 'resize_keyboard': True}
    bot.send_message(chat_id, textoEnvio, None, None, json.dumps(news_keyboard))


if __name__ == "__main__":
    bot = telebot.TeleBot(token)

    # Welcome message.
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        id_user = message.chat.id
        permitted = check_admin(id_user)

        if (permitted == True):
            name = message.chat.first_name
            text_send = "Welcome " + name + "!!"
            keyboard(id_user, text_send)

    # Other messages.
    @bot.message_handler()
    def main(message):

        id_user = message.chat.id
        permitted = check_admin(id_user)

        if (permitted == True):
            text = message.text
            # Mine button.
            if text == "Mined":
                minafacil(id_user)

    bot.polling(none_stop=True)
