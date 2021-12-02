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

def estado_wallet(id_user, wallet):
    url = list_pools[pool] + "/wallet?address=" + wallet
    response = requests.get(url)

    if response.status_code == 200:
        try:
            response_json = response.json()
            currency = response_json["currency"]
            unsold = round(float(response_json["unsold"]), 4)
            balance = round(float(response_json["balance"]) , 4)
            unpaid = round(float(response_json["unpaid"]) , 4)
            paid24h = round(float(response_json["paid24h"]), 4)
            total = round(float(response_json["total"]) , 4)
            
            text_send = "ESTADO WALLET (ult 24h) \n\n" + "*Wallet :* ``` " + str(
                wallet) + " ```\n" + "*Moneda :* ``` " + str(
                currency) + " ```\n" + "*Inmaduro :* ``` " + str(
                unsold) + " ```\n" + "*Balance :* ``` " + str(
                balance) + " ```\n" + "*Sin pagar :* ``` " + str(
                unpaid) + "```\n" + "*Pagado 24h :* ```" + str(
                paid24h) + "```\n" + "*Total 24h :* ```" + str(
                total) + "```\n" 
            bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

        except:
            text_send = u"\u26A0 Sin respuesta de " + web[pool]
            bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

# muestra los datos del estado de la pool
def estado_pool(id_user):
    url = list_pools[pool] + "/status"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            response_json = response.json()
            port = response_json["gr"]["port"]
            fees = response_json["gr"]["fees"]
            fees_solo = response_json["gr"]["fees_solo"]
            hash_rate = round(float(response_json["gr"]["hashrate"]) / (10 ** 6), 2)
            workers = response_json["gr"]["workers"]
            workers_shared = response_json["gr"]["workers_shared"]
            workers_solo = response_json["gr"]["workers_solo"]
            hashrate_last24h = round(float(response_json["gr"]["hashrate_last24h"]) / (10 ** 6), 2)
            
            text_send = "ESTADO DE LA POOL \n\n" + "*Url :* ``` " + str(
                web) + " ```\n" + "*Puerto :* ``` " + str(
                port) + " ```\n" + "*Fees :* ``` " + str(
                fees) + "% ```\n" + "*Fees solo :* ``` " + str(
                fees_solo) + "% ```\n" + "*Hashrate:* ``` " + str(
                hash_rate) + " MH/s```\n" + "*Mineros :* ```" + str(
                workers) + "```\n" + "*Mineros activos:* ```" + str(
                workers_shared) + "```\n" + "*Mineros solo:* ```" + str(
                workers_solo) + "```\n" + "*Hashrate 24h:* ``` " + str(
                hashrate_last24h) + " MH/s```\n"
            bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

        except:
            text_send = u"\u26A0 Sin respuesta de " + web[pool]
            bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

def bloque_info(id_user):
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
            timesincelast = round(float(response_json["RTM"]["timesincelast"]) / 60, 2)
           
            text_send = "INFO ULTIMO BLOQUE \n\n" + "*Bloque :* ``` " + str(
                last_block) + " ```\n" + "*Dificultad :* ``` " + str(
                difficulty) + " ```\n" + "*Recompensa :* ``` " + str(
                reward) + " ```\n" + "*Altura :* ``` " + str(
                height) + " ```\n" + "*Hashrate:* ``` " + str(
                hash_rate) + " MH/s```\n" + "*Mineros Activos:* ```" + str(
                workers_shared) + "```\n" + "*# de bloques en 24h:* ```" + str(
                last24_block) + "```\n"  + "*Ult. bloque hace :* ```" + str(
                timesincelast) + "```\n" 
            bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

        except:
            text_send = u"\u26A0 Sin respuesta de " + web[pool]
            bot.send_message(chat_id=id_user, text=text_send, parse_mode="Markdown")

# muestra datos del bloque encontrado
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
    r1 = ["Pool", "Bloque"]
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
                #text_send = ''
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
        id_chat_group = id_user
        permitted = check_admin(id_user)

        if (permitted == True):
            text = message.text
            if text.find('=') > 0 :
                text1 = text.split('=')
                comando = text1[0]
                parametro1 = text1[1]
            else:
                comando = text
                parametro1 = ""
            # Mine button.
            if comando == "Pool":
                estado_pool(id_user)

            if comando == "Wallet":
                estado_wallet(id_user, parametro1)

            if comando == "Bloque":
                bloque_info(id_user)

    bot.polling(none_stop=True)
