from glob import glob
from random import choice
from utils import main_keyboard
import os
from pprint import pprint

def greet_user(update,context):
    print("Бот начал работу!")
    update.message.reply_text(
        f"Здравствуй,{update.message['chat']['first_name']} {update.message['chat']['last_name']} ",
        reply_markup = main_keyboard()
                              )
    print(update.message['chat']['id'])

def talk_to_me(update,context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def send_dog_picture(update,context):
    dog_path = choice(glob('images/dog*.jp*g'))
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(dog_path,'rb'))
    
def get_photo(update,context):
    update.message.reply_text('Обрабатываем фотографию')
    os.makedirs('downloads',exist_ok=True)
    user_photo = context.bot.getFile(update.message.photo[-1].file_id)
    filename = os.path.join('downloads', f"{update.message.photo[-1].file_id}.jpg")
    user_photo.download(filename)
    update.message.reply_text('Фото сохранено на диск')
