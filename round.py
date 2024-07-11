from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from utils import choose_lvl_keyboard

def round_start(update,context):
    update.message.reply_text(
        "Выберете уровень сложности",
        reply_markup=choose_lvl_keyboard()
    )
    respon = str(update.message['text'])
    if respon == '1':
        return 'lvl_1'
    elif respon == '2':
        return 'lvl_2'
    elif respon == '3':
        return 'lvl_3'
    