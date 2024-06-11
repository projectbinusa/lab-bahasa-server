import uuid

from database.schema import ChatDB
from entitas.chat import repositoriesDB
from entitas.kelas_user.repositoriesDB import find_by_id
from entitas.user.repositoriesDB import find_by_id as find_user_by_id, find_by_user_id_and_class_id
from config.config import CHAT_FOLDER, DOMAIN_FILE_URL
from entitas.topic_chat import services
from util.other_util import raise_error
import logging


def insert_chat_db(json_object={}):
    return repositoriesDB.create_chat(json_object=json_object)

def get_chat_db_with_pagination(class_id, page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination_by_class_id(
        class_id, page=page, limit=limit, filters=filters, to_model=to_model
    )

def get_chat_db_with_pagination_sender_id_and_receiver_id(class_id=0, receiver_id=0, sender_id=0, page=1, limit=9, filters=[], to_model=False):
    print("class_id in service ==> ", class_id)
    print("sender_id in service ==> ", sender_id)
    print("receiver_id in service ==> ", receiver_id)
    kelas = find_by_id(id=class_id)
    receiver = repositoriesDB.get_by_receiver_id(receiver_id=receiver_id)
    sender = repositoriesDB.get_by_sender_id(sender_id=sender_id)
    if kelas is None:
        raise_error(msg="kelas not found")
    if receiver is None:
        raise_error(msg="receiver_id in chat not found")
    if sender is None:
        raise_error(msg="sender_id in chat not found")
    return repositoriesDB.get_all_with_pagination_by_class_id_and_sender_id_receiver_id(class_id=class_id, sender_id=sender_id, receiver_id=receiver_id, page=page, limit=limit, filters=filters, to_model=to_model
    )

def update_chat_db(class_id, receiver_id=0, gambar=None, json_object={}):
    print("receiverid di services > ", receiver_id)
    kelas = find_by_id(id=class_id)
    receiver_id = repositoriesDB.get_by_receiver_id(receiver_id=receiver_id)
    if kelas is None:
        raise_error(msg="kelas not found")
    if receiver_id is None:
        raise_error(msg="receiver_id in chat not found")

def get_chat_db_with_pagination_by_topic_chat_id(class_id=0, topic_chat_id=0, page=1, limit=9, filters=[], to_model=False):
    kelas = repositoriesDB.get_by_class_id(class_id=class_id)
    topic_chat = repositoriesDB.get_by_topic_chat_id(topic_chat_id=topic_chat_id)
    if kelas is None:
        raise_error(msg="class id not found")
    if topic_chat is None:
        raise_error(msg="topic chat id not found")
    return repositoriesDB.get_all_with_pagination_by_class_id_and_topic_chat_id(
        class_id, topic_chat_id, page=page, limit=limit, filters=filters, to_model=to_model
    )


def get_chat_db_with_pagination_by_group_id(class_id=0, group_id=0, page=1, limit=9, filters=[], to_model=False):
    kelas = repositoriesDB.get_by_class_id(class_id=class_id)
    group = repositoriesDB.get_by_group_id(group_id=group_id)
    if kelas is None:
        raise_error(msg="class id not found")
    if group is None:
        raise_error(msg="group id not found")
    return repositoriesDB.get_all_with_pagination_by_class_id_and_group_id(
        class_id=class_id, group_id=group_id, page=page, limit=limit, filters=filters, to_model=to_model
    )



def update_chat_db(class_id, sender_id=0, receiver_id=0, gambar=None, json_object={}):
    # print("receiverid di services > ", receiver_id)
    kelas = find_by_id(id=class_id)
    sender = repositoriesDB.get_by_sender_id(sender_id=sender_id)
    receiver = repositoriesDB.get_by_receiver_id(receiver_id=receiver_id)
    if kelas is None:
        raise_error(msg="kelas not found")
    if sender is None:
        raise_error(msg="sender_id not found")
    if receiver is None:
        raise_error(msg="receiver_id in chat not found")
    else:
        receiver_id = receiver.id
    temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
    with open(CHAT_FOLDER + temp_file_start, "wb") as f:
        f.write(gambar.file.read())
    json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start
    json_object["class_id"] = class_id
    # json_object["receiver_id"] = receiver_id
    json_object["sender_id"] = sender_id
    return repositoriesDB.update_chat(receiver_id=receiver_id, json_object=json_object)


def delete_chat_by_id(id=0, class_id=0, receiver_id=0):
    print("kelas service > ", class_id)
    print("receiverid di services > ", receiver_id)

    # Pastikan receiver_id sudah dalam format yang benar sebelumnya
    if receiver_id is None:
        raise_error(msg="receiver_id is not valid")

    # Cek apakah class_id valid
    kelas = find_by_id(id=class_id)
    if kelas is None:
        raise_error(msg="kelas not found")

    # Cek apakah receiver_id valid dari tabel user
    receiver = find_user_by_id(id=receiver_id)
    if receiver is None:
        raise_error(msg="receiver_id in chat not found")

    # Melanjutkan dengan penghapusan chat
    return repositoriesDB.delete_chat_by_id_and_by_class_id(id, class_id)


def insert_message_service(class_id, receiver_id=0, json_object={}, gambar=None):
    # print("json_object i service >>> ", json_object)
    print("receiverid di services > ", receiver_id)
    kelas = find_by_id(id=class_id)
    receiver = find_by_user_id_and_class_id(id=receiver_id)
    if kelas is None:
        raise_error(msg="kelas not found")
    if receiver is None:
        raise_error(msg="receiver_id not found")
    else:
        receiver_id = receiver.id

    temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
    with open(CHAT_FOLDER + temp_file_start, "wb") as f:
        f.write(gambar.file.read())
    json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start
    json_object["class_id"] = class_id
    # json_object["receiver_id"] = receiver_id
    return repositoriesDB.insert_private_chat(receiver_id=receiver_id, json_object=json_object)


def insert_message_group_service(class_id, group_id=0, json_object={}, gambar=None):
    # print("json_object i service >>> ", json_object)
    print("receiverid di services > ", group_id)
    kelas = find_by_id(id=class_id)
    group = repositoriesDB.get_by_group_id(group_id=group_id)
    if kelas is None:
        raise_error(msg="kelas not found")
    if group is None:
        raise_error(msg="group_id not found")
    else:
        group_id = group.id
    temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
    with open(CHAT_FOLDER + temp_file_start, "wb") as f:
        f.write(gambar.file.read())
    json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start
    json_object["class_id"] = int(class_id)
    # json_object["group_id"] = group_id
    return repositoriesDB.insert_group_chat(group_id=group_id, json_object=json_object)

def insert_message_topic_service(class_id, topic_chat_id=0, json_object={}, gambar=None):
    # print("json_object i service >>> ", json_object)
    print("receiverid di services > ", topic_chat_id)
    kelas = find_by_id(id=class_id)
    topic = repositoriesDB.get_by_topic_chat_id(topic_chat_id=topic_chat_id)
    if kelas is None:
        raise_error(msg="kelas not found")
    if topic is None:
        raise_error(msg="topic_chat_id not found")
    else:
        topic_chat_id = topic.id
    temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
    with open(CHAT_FOLDER + temp_file_start, "wb") as f:
        f.write(gambar.file.read())
    json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start
    json_object["class_id"] = int(class_id)
    # json_object["topic_chat_id"] = topic_chat_id
    return repositoriesDB.insert_group_chat(topic_chat_id=topic_chat_id, json_object=json_object)

def get_messages_for_user_service(user_id, sender_id=None):
    return repositoriesDB.get_chats_for_user(user_id, sender_id)

# services.py
def update_chat_by_group_id_and_class_id(class_id, group_id, gambar=None, json_object={}):
    temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
    with open(CHAT_FOLDER + temp_file_start, "wb") as f:
        f.write(gambar.file.read())
    json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start
    json_object["class_id"] = class_id
    json_object["group_id"] = group_id
    receiver_id = json_object["receiver_id"]
    return repositoriesDB.update_chat(receiver_id=receiver_id, json_object=json_object)

def delete_chat_by_group_id_and_class_id(id=0, class_id=0, group_id=0):
    return repositoriesDB.delete_chat_by_group_id_and_class_id(id, group_id, class_id)

def get_chat_by_id_and_by_group_id_and_by_class_id(id=None, group_id=None, class_id=None):
    return repositoriesDB.get_chat_by_id_and_by_group_id_and_by_class_id(id=id, group_id=group_id, class_id=class_id)
