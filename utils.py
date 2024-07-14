from random import randint
from telegram import ReplyKeyboardMarkup


def main_keyboard():
    return ReplyKeyboardMarkup([['Фото собаки','Учить слова'],['Создать словарь', 'Мои словари', 'Добавить слово в словарь']],resize_keyboard=True)


def new_dict_keyboard():
    return ReplyKeyboardMarkup([['Добавить слово', 'Вернуться в меню']],resize_keyboard=True, one_time_keyboard=True)

def choose_lvl_keyboard():
    return ReplyKeyboardMarkup([['1','2','3']])


def generate_random_number(left, right):
    return(randint(left,right))


def append_word(update,context):
    pass

#def get_smile():
#    smile = choice(settings.SMILES)
#   return emoji.emojize(smile, use_aliases = True)