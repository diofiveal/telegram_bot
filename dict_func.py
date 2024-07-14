from telegram import ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from datetime import datetime
from db import db, create_dict_in_mongo
from utils import main_keyboard, new_dict_keyboard
from pytz import timezone

def create_new_dict_start(update,context):
    update.message.reply_text('Введите название словаря: ',
                              reply_markup=ReplyKeyboardRemove())
    return "dict_name"


def dict_name(update,context):
    text = update.message.text
    create_dict_in_mongo(db, update.effective_user, text)
    dict_keyboard = new_dict_keyboard()
    update.message.reply_text(f'Вы успешно создали словарь {text}. Желаете добавить новое слово в словарь?', reply_markup = dict_keyboard)
    return "add_word"


def back_to_menu(update, context):
    main_key = main_keyboard()
    update.message.reply_text('Возвращаюсь в меню...', reply_markup = main_key)
    return ConversationHandler.END

def write_new_word(update, context):
    update.message.reply_text('Введите новое слово и его перевод через пробел: ',
                              reply_markup=ReplyKeyboardRemove())
    return "save_word"


def save_new_word(update, context):
    new_word = update.message.text.lower().split(' ')
    user_id = update.message['chat']['id']
    dictionary = db.dictionaries.find_one({"user_id": user_id})
    created_time = datetime.now()
    if not 'word' in dictionary:
        db.dictionaries.update_one(
            {'_id': dictionary['_id']},
            {
                '$set': {
                    f'dictionary.{new_word[0]}': {
                        'translation': f'{new_word[1]}',
                        'created_time': created_time,
                        'points': 0
                    }
                }
            }
        )
        array = dictionary['array_keys']
        db.dictionaries.update_one(
             {'_id': dictionary['_id']},
             {
                 '$set': {"array_keys": array.append(new_word[0])}
             }
        )
    dict_keyboard = new_dict_keyboard()
    update.message.reply_text(f'Вы успешно добавили слово {new_word[0]} в словарь. Желаете добавить новое слово в словарь?', reply_markup=dict_keyboard)
    return "add_word"

def write_my_dict(update, context):
    user_id = update.message['chat']['id']
    dictionary = db.dictionaries.find_one({"user_id": user_id})
    for word in dictionary['dictionary']:
        print(word)
    pass
    

    
    