# Telegram-Bot

a telegram Robot, Using [Pyrogram](https://docs.pyrogram.org/) Library
### Creator: Abbas Rahimzadeh
* [Github](https://github.com/AAbbasRR)
* [Telegram](https://t.me/AAbbasRR)

## how to run:
install packages:

    1- create Virtualenv Environment Variable with command [python3 -m venv {virtual name}]
    2- active Virtualenv Environment Variable with command:
        windows: {virtual name}\Source\activate
        linux: source {virtual name}/bin/activate
    3- get project directory and install requirements packages with command [pip3 install -r requirements.txt

receive Telegram API Code and Hash: 
    
    1- Visit https://my.telegram.org/apps and log in with your Telegram Account
    2- Fill out the form with your details and register a new Telegram application
    3- Done. The API key consists of two parts: api_id and api_hash. Keep it secret

Create a Bot in Telegram

    1- Open Telegram and start https://t.me/botfather Robot
    2- Send /newbot Command
    3- send and choose a name for your bot
    4- send and choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot
    5- Done. The Bot Token contains of on part of the HTTP API that the BotFather sent to you, example: 191977208:AAFR6LckL1gPrTj68lsVdFULtekzqSa1pH0. Keep it secret

Config .env file

    1- Create a file with name ".env" In the project directory, next to the file "main.py"
    2- Create 3 Variables:
        API_ID      -> int: api_id received from https://my.telegram.org/apps
        API_HASH    -> str: api_hash received from https://my.telegram.org/apps
        BOT_TOKEN   -> str: HTTP API that the BotFather sent to you
        BOT_NAME    -> str: Choose A Name for Your Robot

run project

    run main.py file with command [python3 main.py]