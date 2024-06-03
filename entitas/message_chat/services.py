from database.schema import MessageChatDB
from entitas.chat.repositoriesDB import get_chat
from entitas.message_chat import repositoriesDB
from entitas.user.repositoriesDB import get_user


def insert_message_chat_db(json_object={}):
    return repositoriesDB.create_message(json_object=json_object)

def get_message_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )

def update_message_chat_db(json_object={}):
    return repositoriesDB.update_message_chat(json_object=json_object)

def delete_message_chat_by_id(id=0):
    return repositoriesDB.delete_message_chat_by_id(id)

def send_message(json_object={}, sender_id=0, chat_id=0):
    # Pastikan pengguna ada
    sender = get_user(sender_id)
    if not sender:
        raise ValueError("User not found.")

    # Pastikan chat ada
    chat = get_chat(chat_id)
    if not chat:
        raise ValueError("Chat not found.")

    # Buat dan simpan pesan
    message = repositoriesDB.create_message(sender_id, chat_id, json_object=json_object)
    return message

def get_chat_messages(chat_id):
    # Pastikan chat ada
    chat = get_chat(chat_id)
    if not chat:
        raise ValueError("Chat not found.")

    # Ambil pesan dari chat
    messages = get_chat_messages(chat_id)
    return messages