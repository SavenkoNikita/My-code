#!/usr/bin/env python3

import telegram
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from datetime import datetime, timezone
import os

# токен бота
TOKEN = '1013175932:AAGIDc3GACkwXPGK8XRLfJkNQhO_J4xtflw'

# создаем бота, для отправки сообщений
bot = telegram.Bot(token=TOKEN)
# print(bot.get_me())
# создаем апдейтер для получения сообщений
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# список пользователей
Nik = int(368861606)
# Dima = int(463376780)
# Pavel = int(762058672)
# Alex = int(1350324635)
# Chat = int(-1001332331366) #группа IT_info
# Chat = int(-1001450700256) #раскоментить для тестов в GateKeepers
Chat = int(368861606)

# замеряем начальное время
time_start = datetime.now(tz=timezone.utc)

# список опрашиваемых пользователей
users = {
    Nik: {
        'name': 'Никита @savenko_nikita',
        'answer': None,
    },
    #    Dima: {
    #        'name':'Дима @L7kestyle',
    #        'answer' : None,
    #    },
    #    Alex: {
    #        'name':'Алексей',
    #        'answer' : None,
    #    },
    #    Pavel: {
    #        'name':'Павел @Van_leff',
    #        'answer' : None,
    #    },
}

# что спрашивает бот
IS_YOU_TEXT = 'Ты дежурный?'
question2 = 'Уверен?'

# Отправка users вопроса IS_YOU_TEXT
for user_id, user_data in users.items():
    # print(time_start)
    # bot.send_message(chat_id = user_id, text=IS_YOU_TEXT)
    custom_keyboard = [['Да', 'Нет']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True, one_time_keyboard=True)

    bot.send_message(chat_id=user_id,
                     text=IS_YOU_TEXT,
                     reply_markup=reply_markup)


def is_you(update, context):
    # print(update.message.date)
    if update.message.date > time_start:
        if update.effective_chat.id in users:
            users[update.effective_chat.id]['answer'] = update.message.text.lower()
            if users[update.effective_chat.id]['answer'] == 'да' or 'нет':
                for user_id, user_data in users.items():
                    # print(time_start)
                    # bot.send_message(chat_id = user_id, text=question2)
                    custom_keyboard2 = [['Стопудово!', 'Надо уточнить']]
                    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True,
                                                                one_time_keyboard=True)

                    bot.send_message(chat_id=user_id,
                                     text=IS_YOU_TEXT,
                                     reply_markup=reply_markup)

                def is_you(update, context):
                    # print(update.message.date)
                    if update.message.date > time_start:
                        if update.effective_chat.id in users:
                            users[update.effective_chat.id]['answer'] = update.message.text.lower()
                            if users[update.effective_chat.id]['answer'] == 'да':
                                context.bot.send_message(chat_id=update.effective_chat.id,
                                                         text='Красава ;)')  # Если приходит ответ "нет", то в ответ бот присылает это сообщение
                                bot.send_message(chat_id=Chat, text='В эти выходные дежурит ' + users.get(
                                    update.effective_chat.id).get('name'))
                                os.kill(os.getpid(), 9)
                            elif users[update.effective_chat.id]['answer'] == 'нет':
                                context.bot.send_message(chat_id=update.effective_chat.id,
                                                         text='Везёт')  # Если приходит ответ "да", то в ответ бот присылает это сообщение
                                pass
                            else:
                                pass

                # Если приходит ответ "нет", то в ответ бот присылает это сообщение
                bot.send_message(chat_id=Chat,
                                 text='В эти выходные дежурит ' + users.get(update.effective_chat.id).get('name'))
                os.kill(os.getpid(), 9)
            elif users[update.effective_chat.id]['answer'] == 'нет':
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='Везёт')  # Если приходит ответ "да", то в ответ бот присылает это сообщение
                pass
            else:
                pass


# Отправка users вопроса question2
for user_id, user_data in users.items():
    # print(time_start)
    # bot.send_message(chat_id = user_id, text=question2)
    custom_keyboard = [['Стопудово!', 'Надо уточнить']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True, one_time_keyboard=True)

    bot.send_message(chat_id=user_id,
                     text=IS_YOU_TEXT,
                     reply_markup=reply_markup)


def is_you(update, context):
    # print(update.message.date)
    if update.message.date > time_start:
        if update.effective_chat.id in users:
            users[update.effective_chat.id]['answer'] = update.message.text.lower()
            if users[update.effective_chat.id]['answer'] == 'да':
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='Красава ;)')  # Если приходит ответ "нет", то в ответ бот присылает это сообщение
                bot.send_message(chat_id=Chat,
                                 text='В эти выходные дежурит ' + users.get(update.effective_chat.id).get('name'))
                os.kill(os.getpid(), 9)
            elif users[update.effective_chat.id]['answer'] == 'нет':
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='Везёт')  # Если приходит ответ "да", то в ответ бот присылает это сообщение
                pass
            else:
                pass

            # проверка на то, что все ответили "Нет", если так, то "никто не дежурит"
            i = 0
            for user_id, user_data in users.items():
                if user_data['answer'] == 'нет':
                    i += 1
            if i == len(users):
                # context.bot.send_message(chat_id=update.effective_chat.id, text = 'DEFAULT_USER')
                bot.send_message(chat_id=Chat, text='В эти выходные никто не дежурит')
                os.kill(os.getpid(), 9)
    else:
        pass


is_you_handler = MessageHandler(Filters.text & (~Filters.command), is_you)
dispatcher.add_handler(is_you_handler)
updater.start_polling()
updater.idle()
sys.exit(0)
