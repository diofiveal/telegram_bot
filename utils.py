from random import choice, randint
from telegram import ReplyKeyboardMarkup

def main_keyboard():
    return ReplyKeyboardMarkup([['Фото собаки','Учить слова'],['Кнопка2']])
def choose_lvl_keyboard():
    return ReplyKeyboardMarkup([['1','2','3']])
def generate_random_number(left, right):
    return(randint(left,right))

#def get_smile():
#    smile = choice(settings.SMILES)
#   return emoji.emojize(smile, use_aliases = True)