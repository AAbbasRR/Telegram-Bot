from pyrogram import Client, filters

from .data import BUTTONS, QUESTIONS, MESSAGES

import json


@Client.on_message(filters.private & filters.command("start"))  # this function run when user send /start command to bot in private(PV)
async def start(client, message):
    await message.reply(text=MESSAGES['start'], reply_markup=BUTTONS['generate_code'], quote=True)  # send to user a message (quote It means to reply to the message sent by the user)


@Client.on_message(filters.private & filters.command("help"))  # this function run when user send /help command to bot in private(PV)
async def help(client, message):
    await client.send_chat_action(message.chat.id, "typing")  # Show the user that the robot is typing
    await message.reply(text=MESSAGES['help'], reply_markup=BUTTONS['generate_code'], quote=True)  # send to user a message (quote It means to reply to the message sent by the user)


@Client.on_message(filters.private & filters.command("generate"))  # this function run when user send /generate command to bot in private(PV)
async def generate(client, message):
    await client.send_chat_action(message.chat.id, "typing")  # Show the user that the robot is typing
    with open(f"users/{message.from_user.id}ـgenerate.txt", "w") as file_write:
        file_write.write(json.dumps({"question": 0})) # set user questions and answers in file
    await message.reply(text=QUESTIONS[0]['text'], reply_markup=QUESTIONS[0]['button'], quote=True)  # send to user a message (quote It means to reply to the message sent by the user)
