import uuid

from database.schema import ChatDB
from entitas.chat import repositoriesDB
from entitas.kelas_user.repositoriesDB import find_by_id
from entitas.message_chat.repositoriesDB import create_message, get_chat_messagess, \
    find_by_message_by_user_id_and_chat_id, update_delete_by_id
from entitas.user.repositoriesDB import get_user
from config.config import CHAT_FOLDER, DOMAIN_FILE_URL
from util.other_util import raise_error


def insert_chat_db(json_object={}):
    return repositoriesDB.create_chat(json_object=json_object)

def get_chat_db_with_pagination(class_id, page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination_by_class_id(
        class_id, page=page, limit=limit, filters=filters, to_model=to_model
    )

def get_chat_db_with_pagination_sender_id_and_receiver_id(class_id, sender_id, receiver_id, page=1, limit=9, filters=[], to_model=False):
    kelas = find_by_id(id=class_id)
    receiver_id = repositoriesDB.get_by_receiver_id(receiver_id=receiver_id)
    if kelas is None:
        raise_error(msg="kelas not found")
    if receiver_id is None:
        raise_error(msg="receiver_id in chat not found")
    return repositoriesDB.get_all_with_pagination_by_class_id_and_sender_id_receiver_id(
        class_id, sender_id, receiver_id, page=page, limit=limit, filters=filters, to_model=to_model
    )

def update_chat_db(class_id, gambar=None, json_object={}):
    temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
    with open(CHAT_FOLDER + temp_file_start, "wb") as f:
        f.write(gambar.file.read())
    json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start
    return repositoriesDB.update_chat(class_id, json_object=json_object)

def delete_chat_by_id(id=0, class_id=0):
    return repositoriesDB.delete_chat_by_id_and_by_class_id(id, class_id)


def insert_message_service(class_id, json_object={}, gambar=None):
    temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
    with open(CHAT_FOLDER + temp_file_start, "wb") as f:
        f.write(gambar.file.read())
    json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start
    return repositoriesDB.insert_private_chat(class_id, json_object=json_object)

def get_messages_for_user_service(user_id, sender_id=None):
    return repositoriesDB.get_chats_for_user(user_id, sender_id)
