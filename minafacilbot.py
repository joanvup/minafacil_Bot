#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import telebot
import requests
from time import sleep
from telebot import types

# -------------------- SETTINGS --------------------

# Telegram bot Token.
token = "2145088618:AAGul0GOmx6XCcDzVuBwGX1us9EsDM7lkew"

# List with the telegram id of the allowed users.
id_admins = [1334636275]

# Your Pool. 0 = Minafacil
pool = 0

# Tiempo en segundos de consulta
tiempo_consulta = 30

# --------------------------------------------------

list_pools = ["http://pool.minafacil.com/api"]
web = ["https://pool.minafacil.com"]

# View the wallet data on Ethermine.
def bloque_encontrado(id_user):
    url = list_pools[pool] + "/currencies"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            response_json = response.json()
            hash_rate = round(float(response_json["RTM"]["hashrate"]) / (10 ** 6), 2)
            workers_shared = response_json["RTM"]["workers_shared"]
            time_last_block = response_json["RTM"]["timesincelast"]
            last_block = response_json["RTM"]["lastblock"]
            last24_block = response_json["RTM"]["24h_blocks"]
            difficulty = response_json["RTM"]["difficulty"]
            reward = response_json["RTM"]["reward"]
            height = response_json["RTM"]["height"]
           
            text_send = "BLOQUE CONSEGUIDO \n\n" + "*Bloque :* ``` " + str(
                last_block) + " ```\n" + "*Dificultad :* ``` " + str(
                difficulty) + " ```\n" + "*Recompensa :* ``` " + str(
                reward) + " ```\n" + "*Altura :* ``` " + str(
                height) + " ```\n" + "*Hashrate:* ``` " + str(
                hash_rate) + " MH/s```\n" + "*Mineros Activos:* ```" + str(
                workers_shared) + "```\n" + "*# de bloques en 24h:* ```" + str(
                last24_block) + "```\n" 
            bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

        except:
            text_send = u"\u26A0 Sin respuesta de " + web[pool]
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
            url = list_pools[pool] + "/currencies"
            response = requests.get(url)
            if response.status_code == 200:
                response_json = response.json()
                last_block_ini = response_json["RTM"]["lastblock"]
                text_send = "*Iniciando busqueda de bloque* \n" + "*Ultimo Bloque :* ``` " + str(
                last_block_ini) + " ```\n" 
                bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")
                #keyboard(id_user, text_send)
            while 1:
                sleep(tiempo_consulta)
                response = requests.get(url)
                if response.status_code == 200:
                    response_json = response.json()
                    last_block = response_json["RTM"]["lastblock"]
                    if last_block != last_block_ini :
                        bloque_encontrado(id_user)
                        last_block_ini = last_block
                        
    @bot.message_handler()
    def main(message):

        id_user = message.chat.id

    bot.polling(none_stop=True)
