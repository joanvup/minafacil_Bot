MinaFacil Bot
===================
**MinaFacil Bot** es un simple bot para telegram que envia un mensaje cuando se descubra un bloque.

-------------
### Instalación
para la instalación, lo primero que hay que hacer es instalar la libreria **pyTelegramBotAPI**

    $ sudo pip install pyTelegramBotAPI

Lo siguiente será clonar el repositorio de Github:

    $ git clone https://github.com/joanvup/minafacil_Bot.git
    $ cd minafacil_Bot

Luego editaremos el archivo minafacilbot.py 

    $ sudo nano minafacilbot.py


 por ejemplo:

 -------------------- SETTINGS --------------------

token = "2145088618:AAGul0GOmx6XCcDzVuBwGX1us9EsDM7lkew"
id_admins = [1334636275]
pool = 0
tiempo_consulta = 30

list_pools = ["http://pool.minafacil.com/api"]
web = ["https://pool.minafacil.com"]
----------------------------------------------------

Finalmente ejecutamos el script y podemos ir a nuestro bot de Telegram e iniciarlo y esperar por e mensaje de BLOQUE CONSEGUIDO

    $ sudo python ethbot.py
