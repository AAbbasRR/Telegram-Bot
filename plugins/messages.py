from data import QUESTIONS, BUTTONS, ERRORS

from pyrogram import Client, filters

import datetime
import json
import redis


@Client.on_message(filters.private & filters.text)  # this function run when user send any message text to bot in private(PV)
async def message_question(client, message):
    await client.send_chat_action(message.chat.id, "typing")  # Show the user that the robot is typing
    rds_cache = redis.StrictRedis(decode_responses=True)  # config redis cache
    try:
        user_answers = json.loads(rds_cache.get(f"{message.from_user.id}_generate"))  # get user questions and answers in cache memory
        if user_answers['question'] in [0, 5]:  # if user in country questions
            if len(message.text) < 3:  # if length of user message less than 3 character, send error Message
                await message.reply(text=ERRORS['invalid_country_name'], quote=True)
                return None
            else:
                user_answers[str(user_answers['question'])] = message.text.upper() if len(message.text) == 3 else message.text.capitalize()  # set user answer in memory cache
                user_answers['question'] += 1  # In the cache, find out which user is in the next question
        elif user_answers['question'] in [2, 4]:  # if user in date questions
            if len(message.text) != 6:  # if length of user message less than 6 or more than 6 character, send error Message
                await message.reply(text=ERRORS['invalid_date_format'], quote=True)
                return None
            else:
                try:
                    datetime.datetime.strptime(message.text, "%y%m%d")  # check if invalid date format, send error
                    user_answers[str(user_answers['question'])] = message.text  # set user answer in memory cache
                    user_answers['question'] += 1  # In the cache, find out which user is in the next question
                except ValueError:
                    await message.reply(text=ERRORS['invalid_date_format'], quote=True)
                    return None
        elif user_answers['question'] == 3:  # if user in sex question send message, return error message
            await message.reply(text=ERRORS['select_button'], quote=True)
            return None
        else:
            user_answers[str(user_answers['question'])] = message.text
            user_answers['question'] += 1
        rds_cache.set(f"{message.from_user.id}_generate", json.dumps(user_answers))  # update user answers in cache
        if user_answers['question'] > 8:  # If the user has a complete answer to all the questions, show all his answers and get the answer confirmation command
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
            await message.reply(text=text, reply_markup=BUTTONS['submit_answers'])
            return None
        else:  # send new question
            await message.reply(text=QUESTIONS[user_answers['question']]['text'], reply_markup=QUESTIONS[user_answers['question']]['button'])
            return None
    except TypeError:  # if user dones not question and answer key in redis, send error message to the user
        await message.reply(text=ERRORS['invalid_message'], reply_markup=BUTTONS['generate_code'], quote=True)
