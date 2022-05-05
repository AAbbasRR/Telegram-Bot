from pyrogram import Client
from pyrogram.types import BotCommand

from decouple import config

import os

plugins = dict(root='plugins')  # set plugins directory

app = Client(config("BOT_NAME"), api_id=config("API_ID", cast=int), api_hash=config("API_HASH"), bot_token=config("BOT_TOKEN"), plugins=plugins)  # config Robot Class

with app:  # Create Bot Default Commands
    if os.path.exists("users") is False:
        os.mkdir("users")        
    app.set_bot_commands(commands=[
        BotCommand("start", "Start/restart Robot"),  # receive 2 params, 1: bot command, bot description command
        BotCommand("help", "Description of the robot and how to use the robot"),
        BotCommand("generate", "Generate TD1 Code")
    ])

app.run()  # run bot sessions
