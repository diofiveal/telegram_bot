
from telegram.ext import Updater, CommandHandler,ConversationHandler, MessageHandler, Filters
import settings, logging
from handlers import greet_user, send_dog_picture, get_photo, talk_to_me
from utils import generate_random_number
from round import round_start
logging.basicConfig(filename='bot.log',level=logging.INFO)

def main():
    mybot = Updater(token=settings.TOKEN,use_context=True)
    
    round = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^(Учить слова)$'),round_start)],
        states={},
        fallbacks=[]
    )
    dp = mybot.dispatcher
    dp.add_handler(round)
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(CommandHandler("dog",send_dog_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Фото собаки)$'),send_dog_picture))
    dp.add_handler(MessageHandler(Filters.photo, get_photo))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))
    
    logging.info("Бот стартовал!")
    
    mybot.start_polling()
    mybot.idle()
    
if __name__ == '__main__':
    main()