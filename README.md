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


 For example:

    # -------------------- SETTINGS --------------------
    
    
    # Telegram bot Token.
    token = "378572660:AAHaLn4NylzJuv4kl4XusEtG3LeDqafjA75"
    
    # List with the telegram id of the allowed users.
    id_admins = [1334636275]
    
    # Your Pool. 0 = Minafacil
    pool = 0
    
    # Tiempo en segundos de consulta
    tiempo_consulta = 30
    
    list_pools = ["http://pool.minafacil.com/api"]
    web = ["https://pool.minafacil.com"]
    # --------------------------------------------------


Finalmente ejecutamos el script y podemos ir a nuestro bot de Telegram y ponerlo en marcha:

    $ sudo python minafacilbot.py
