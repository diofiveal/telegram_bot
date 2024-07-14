from dict_func import create_new_dict_start, dict_name, back_to_menu, write_new_word, save_new_word
from telegram.ext import Updater, CommandHandler,ConversationHandler, MessageHandler, Filters
import settings, logging
from handlers import greet_user, send_dog_picture, get_photo, talk_to_me
from round import round_start, choose_lvl


logging.basicConfig(filename='bot.log',level=logging.INFO)


def main():
    mybot = Updater(token=settings.TOKEN,use_context=True)
    
    round = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^(Учить слова)$'), round_start)],
        states={
                "choose_lvl": [MessageHandler(Filters.text, choose_lvl)],
                "lvl_1": [],
                "lvl_2": [],
                "lvl_3": []
            },
        fallbacks=[]
    )
    new_dict = ConversationHandler(
        entry_points=[
                MessageHandler(Filters.regex("^(Создать словарь)$"), create_new_dict_start),
                MessageHandler(Filters.regex('^(Добавить слово в словарь)$'), write_new_word)
            ],
        states={
            "dict_name": [MessageHandler(Filters.text, dict_name)],
            "add_word": [
                    MessageHandler(Filters.regex('^(Добавить слово)$'), write_new_word),
                    MessageHandler(Filters.regex('^(Вернуться в меню)$'), back_to_menu)
                ],
            "back_menu": [MessageHandler(Filters.text, back_to_menu)],
            "save_word": [MessageHandler(Filters.text, save_new_word)]
        },
        fallbacks=[]
    )
    dp = mybot.dispatcher
    dp.add_handler(round)
    dp.add_handler(new_dict)
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("dog", send_dog_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Фото собаки)$'), send_dog_picture))
    dp.add_handler(MessageHandler(Filters.photo, get_photo))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот стартовал!")
    
    mybot.start_polling()
    mybot.idle()
    
if __name__ == '__main__':
    main()