from pyrogram import Client
from mrz.generator.td1 import TD1CodeGenerator
from mrz.base.errors import CountryError

from .data import MESSAGES, QUESTIONS, ERRORS, BUTTONS

import json
import os


@Client.on_callback_query()  # this function run when user clicked inline buttons
async def CallBackQueryGenerateCode(client, callback_query):
    if callback_query.data == "Generate":  # if clicked generate button
        await client.send_chat_action(callback_query.from_user.id, "typing")  # Show the user that the robot is typing
        with open(f"users/{callback_query.from_user.id}ـgenerate.txt", "w") as file_write:
            file_write.write(json.dumps({"question": 0})) # set user questions and answers in file
        await client.send_message(chat_id=callback_query.from_user.id, text=QUESTIONS[0]['text'], reply_markup=QUESTIONS[0]['button'])
        return None
    elif callback_query.data in ["M", "F", "X"]:  # if clicked any sex question button
        try:
            with open(f"users/{callback_query.from_user.id}ـgenerate.txt", "r") as file_read:
                user_answers = json.loads(file_read.read())  # get user questions and answers in file
                if user_answers['question'] == 3:  # if user in the sex question
                    await client.send_chat_action(callback_query.from_user.id, "typing")  # Show the user that the robot is typing
                    user_answers[str(user_answers['question'])] = callback_query.data  # set user answer in file
                    user_answers['question'] += 1  # In the file, find out which user is in the next question
                    await client.send_message(chat_id=callback_query.from_user.id, text=QUESTIONS[user_answers['question']]['text'], reply_markup=QUESTIONS[user_answers['question']]['button'])  # send new question
                    with open(f"users/{callback_query.from_user.id}ـgenerate.txt", "w") as file_write:
                        file_write.write(json.dumps(user_answers))  # update user answers in file
                    return None
        except FileNotFoundError:  # if user dones not question and answer key in redis, send error message to the user
            await client.send_message(chat_id=callback_query.from_user.id, text=ERRORS['invalid_message'], reply_markup=BUTTONS['generate_code'])
    elif callback_query.data == "Ignore":  # if user click ignore button in option data question
        try:
            with open(f"users/{callback_query.from_user.id}ـgenerate.txt", "r") as file_read:
                user_answers = json.loads(file_read.read())  # get user questions and answers in file
                if user_answers['question'] == 8:  # if user in the option data question
                    await client.send_chat_action(callback_query.from_user.id, "typing")  # Show the user that the robot is typing
                    user_answers[str(user_answers['question'])] = ""
                    user_answers['question'] += 1
                    text = f"""Your Answers:
            
1️⃣ - country_code: {user_answers['0']}

2️⃣ - document_number: {user_answers['1']}

3️⃣ - birth_date: {user_answers['2']}

4️⃣ - sex: {user_answers['3']}

5️⃣ - expiry_date: {user_answers['4']}

6️⃣ - nationality: {user_answers['5']}

7️⃣ - surname: {user_answers['6']}

8️⃣ - given_names: {user_answers['7']}

9️⃣ - optional_data: {"Ignored" if user_answers['8'] == "" else user_answers['8']}

DO You Accept This Answers?"""
                    await client.send_message(chat_id=callback_query.from_user.id, text=text, reply_markup=BUTTONS['submit_answers'])  # show all his answers and get the answer confirmation command
                    with open(f"users/{callback_query.from_user.id}ـgenerate.txt", "w") as file_write:
                        file_write.write(json.dumps(user_answers))  # update user answers in file
                    return None
        except FileNotFoundError:  # if user dones not question and answer key in redis, send error message to the user
            await client.send_message(chat_id=callback_query.from_user.id, text=ERRORS['invalid_message'], reply_markup=BUTTONS['generate_code'])
    elif callback_query.data in ["submit", "cancel"]:  # if user clicked submit or cancel button
        try:
            with open(f"users/{callback_query.from_user.id}ـgenerate.txt", "r") as file_read:
                user_answers = json.loads(file_read.read())  # get user questions and answers in file
                if user_answers['question'] > 8:  # If the user has a complete answer to all the questions
                    await client.send_chat_action(callback_query.from_user.id, "typing")  # Show the user that the robot is typing
                    if callback_query.data == "submit":  # if clicked submit button
                        os.remove(f"users/{callback_query.from_user.id}ـgenerate.txt")  # delete answers
                        try:  # set user answers in mrz package and return response
                            await client.send_message(chat_id=callback_query.from_user.id, text=TD1CodeGenerator(
                                "ID",
                                user_answers['0'],
                                user_answers['1'],
                                user_answers['2'],
                                user_answers['3'],
                                user_answers['4'],
                                user_answers['5'],
                                user_answers['6'],
                                user_answers['7'],
                                user_answers['8'],
                            ))
                        except CountryError as Error:
                            await client.send_message(chat_id=callback_query.from_user.id, text=f"""❌ {Error} ❌
please try again, to Generate the TD code, send the /generate command or use the «generate code» button""", reply_markup=BUTTONS['generate_code'])
                    else:  # if clicked cancel button, delete answers and send message
                        os.remove(f"users/{callback_query.from_user.id}ـgenerate.txt")  # delete answers
                        await client.send_message(chat_id=callback_query.from_user.id, text=MESSAGES['cancel'], reply_markup=BUTTONS['generate_code'])
        except FileNotFoundError:  # if user dones not question and answer key in redis, send error message to the user
            await client.send_message(chat_id=callback_query.from_user.id, text=ERRORS['invalid_message'], reply_markup=BUTTONS['generate_code'])
