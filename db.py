from pymongo import MongoClient
import settings


client = MongoClient(settings.URL_CONNECT)


db = client[settings.MONGO_DB]


def get_or_create_user(db, effective_user, chat_id):
    user = db.users.find_one({"user_id": effective_user.id})
    if not user:
        user = {
            "user_id": effective_user.id,
            "first_name": effective_user.first_name,
            "last_name": effective_user.last_name,
            "username": effective_user.username,
            "chat_id": chat_id,
        }
        db.users.insert_one(user)
    return user


def create_dict_in_mongo(db, effective_user, dict_name=''):
    new_dict = {
        "user_id": effective_user.id,
        "dict_name": dict_name,
        "dictionary": {},
        "array_keys": []
    }
    db.dictionaries.insert_one(new_dict)