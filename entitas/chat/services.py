import uuid

from database.schema import ChatDB
from entitas.chat import repositoriesDB
from entitas.group.repositoriesDB import find_by_group_id_and_class_id
from entitas.kelas_user.repositoriesDB import find_by_id
from entitas.topic_chat.repositoriesDB import find_by_topic_chat_id_and_class_id
from entitas.user.repositoriesDB import find_by_id as find_user_by_id, find_instructur_by_class_id
from config.config import CHAT_FOLDER, DOMAIN_FILE_URL
from entitas.topic_chat import services
from entitas.user_chat.repositoriesDB import find_by_user_chat_id_and_class_id
from util.other_util import raise_error
import logging


def insert_chat_db(json_object={}):
    return repositoriesDB.create_chat(json_object=json_object)


def get_chat_db_with_pagination(class_id, page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination_by_class_id(
        class_id, page=page, limit=limit, filters=filters, to_model=to_model
    )


def get_chat_db_with_pagination_sender_id_and_receiver_id(class_id=0, receiver_id=0, sender_id=0, page=1, limit=9,
                                                          filters=[], to_model=False):
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
    return repositoriesDB.get_all_with_pagination_by_class_id_and_sender_id_receiver_id(class_id=class_id,
                                                                                        sender_id=sender_id,
                                                                                        receiver_id=receiver_id,
                                                                                        page=page, limit=limit,
                                                                                        filters=filters,
                                                                                        to_model=to_model
                                                                                        )


def update_chat_db(class_id, receiver_id=0, gambar=None, json_object={}):
    print("receiverid di services > ", receiver_id)
    kelas = find_by_id(id=class_id)
    receiver_id = repositoriesDB.get_by_receiver_id(receiver_id=receiver_id)
    if kelas is None:
        raise_error(msg="kelas not found")
    if receiver_id is None:
        raise_error(msg="receiver_id in chat not found")


def get_chat_db_with_pagination_by_topic_chat_id(class_id=0, topic_chat_id=0, page=1, limit=9, filters=[],
                                                 to_model=False):
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
        class_id=class_id, group_id=group_id, page=page, limit=limit, filters=filters, order_by="-created_date",
        to_model=to_model
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


def insert_message_service(class_id, json_object={}, gambar=None):
    try:
        kelas = find_by_id(id=class_id)
        receiver = find_instructur_by_class_id(class_id=class_id)

        if kelas is None:
            raise_error(msg="kelas not found")
        if receiver is None:
            raise_error(msg="receiver not found")

        receiver_id = receiver.id

        if gambar:
            temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
            with open(CHAT_FOLDER + temp_file_start, "wb") as f:
                f.write(gambar.file.read())
            json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start

        json_object["class_id"] = class_id
        # Tidak perlu mengatur json_object["receiver_id"] lagi

        return repositoriesDB.insert_private_chat(receiver_id=receiver_id, json_object=json_object)
    except Exception as e:
        print("error chat service insert: ", e)
    return None


def insert_message_group_service(class_id, group_id=0, json_object={}, gambar=None):
    # Print debug information
    print("receiverid di services >", group_id)

    # Find the class and group by their IDs
    kelas = find_by_id(id=class_id)
    group = find_by_group_id_and_class_id(id=group_id, class_id=class_id)

    # Error handling if class or group is not found
    if kelas is None:
        raise_error(msg="kelas not found")
    if group is None:
        raise_error(msg="group_id not found")

    group_id = group.id

    if gambar is not None:
        temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
        with open(CHAT_FOLDER + temp_file_start, "wb") as f:
            f.write(gambar.file.read())
        json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start

    json_object["class_id"] = int(class_id)

    return repositoriesDB.insert_group_chat(group_id=group_id, json_object=json_object)


def insert_message_topic_service(class_id, topic_chat_id=0, json_object={}, gambar=None):
    # Print debug information
    print("receiverid di services >", topic_chat_id)

    # Find the class and topic_chat by their IDs
    kelas = find_by_id(id=class_id)
    topic_chat = find_by_topic_chat_id_and_class_id(id=topic_chat_id, class_id=class_id)

    # Error handling if class or topic_chat is not found
    if kelas is None:
        raise_error(msg="kelas not found")
    if topic_chat is None:
        raise_error(msg="topic_chat_id not found")

    topic_chat_id = topic_chat.id

    if gambar is not None:
        temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
        with open(CHAT_FOLDER + temp_file_start, "wb") as f:
            f.write(gambar.file.read())
        json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start

    json_object["class_id"] = int(class_id)

    return repositoriesDB.insert_topic_chat(topic_chat_id=topic_chat_id, json_object=json_object)


def get_messages_for_user_service(user_id, sender_id=None):
    return repositoriesDB.get_chats_for_user(user_id, sender_id)


# services.py
def update_chat_by_group_id_and_class_id(class_id, group_id, gambar=None, json_object={}):
    try:
        if gambar:
            temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
            with open(CHAT_FOLDER + temp_file_start, "wb") as f:
                f.write(gambar.file.read())
            json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start
        else:
            json_object["gambar"] = None  # atau bisa diatur menjadi None sesuai kebutuhan
    except Exception as e:
        print("Error handling gambar:", e)

    json_object["class_id"] = class_id
    json_object["group_id"] = group_id
    # json_object["sender_id"] = user_id
    return repositoriesDB.update_chat(json_object=json_object)


def delete_chat_by_group_id_and_class_id(id=0, class_id=0, group_id=0):
    return repositoriesDB.delete_chat_by_group_id_and_class_id(id, group_id, class_id)


def get_chat_by_id_and_by_group_id_and_by_class_id(id=None, group_id=None, class_id=None):
    return repositoriesDB.get_chat_by_id_and_by_group_id_and_by_class_id(id=id, group_id=group_id, class_id=class_id)


def insert_message_group_service_by_receiver_id(class_id, receiver_id=0, json_object={}, gambar=None):
    # Print debug information
    print("receiverid di services >", receiver_id)

    # Find the class and group by their IDs
    kelas = find_by_id(id=class_id)  # Ubah nama fungsi di sini
    receiver = find_by_user_chat_id_and_class_id(id=receiver_id, class_id=class_id)  # Ubah nama fungsi di sini

    # Error handling if class or group is not found
    if kelas is None:
        raise_error(msg="kelas not found")
    if receiver is None:
        raise_error(msg="receiver not found")

    receiver_id = receiver.id

    if gambar is not None:
        temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
        with open(CHAT_FOLDER + temp_file_start, "wb") as f:
            f.write(gambar.file.read())
        json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start

    json_object["class_id"] = int(class_id)

    return repositoriesDB.insert_receiver_chat(receiver_id=receiver_id, json_object=json_object)


def update_chat_by_receiver_id_and_class_id(class_id, receiver_id, gambar=None, json_object={}):
    try:
        if gambar is not None and hasattr(gambar, 'file'):
            temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
            with open(CHAT_FOLDER + temp_file_start, "wb") as f:
                f.write(gambar.file.read())
            json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start
        else:
            json_object["gambar"] = None  # atau bisa diatur menjadi None sesuai kebutuhan
    except Exception as e:
        print("Error handling gambar:", e)

    json_object["class_id"] = class_id
    json_object["receiver_id"] = receiver_id

    # Debugging
    print("Updated json_object: ", json_object)

    return repositoriesDB.update_chat_by_receiver_id_and_class_id(json_object=json_object)


def get_chat_db_with_pagination_by_receiver_id_and_class_id(class_id=0, receiver_id=0, page=1, limit=9, filters=[],
                                                            to_model=False):
    kelas = repositoriesDB.get_by_class_id(class_id=class_id)
    user = find_by_user_chat_id_and_class_id(id=receiver_id, class_id=class_id)
    if kelas is None:
        raise_error(msg="class id not found")
    if user is None:
        raise_error(msg="receiver_id id not found")
    return repositoriesDB.get_all_with_pagination_by_class_id_and_receiver_id(
        class_id=class_id, receiver_id=receiver_id, page=page, limit=limit, filters=filters, order_by="-created_date",
        to_model=to_model
    )


def delete_chat_by_receiver_id_and_class_id(id=0, class_id=0, receiver_id=0):
    return repositoriesDB.delete_chat_by_receiver_id_and_class_id(id, receiver_id, class_id)


def update_chat_by_topic_chat_id_and_class_id(class_id, topic_chat_id, gambar=None, json_object={}):
    try:
        # Verify that the class exists
        kelas = find_by_id(id=class_id)
        if kelas is None:
            raise_error(msg="Class not found")

        # Verify that the topic chat exists within the class
        topic_chat = find_by_topic_chat_id_and_class_id(id=topic_chat_id, class_id=class_id)
        if topic_chat is None:
            raise_error(msg="Topic chat not found")

        # Handle the image (gambar) if provided
        if gambar:
            temp_file_start = str(uuid.uuid4()) + gambar.filename.replace(" ", "")
            with open(CHAT_FOLDER + temp_file_start, "wb") as f:
                f.write(gambar.file.read())
            json_object["gambar"] = DOMAIN_FILE_URL + '/files/' + temp_file_start
        else:
            json_object["gambar"] = None

        # Update chat details
        json_object["class_id"] = class_id
        json_object["topic_chat_id"] = topic_chat_id
        return repositoriesDB.update_chat(json_object=json_object)

    except Exception as e:
        logging.error(f"Error updating chat by topic chat ID and class ID: {e}")
        raise_error(msg="An error occurred while updating the chat")


def delete_chat_by_topic_chat_id_and_class_id(id=0, class_id=0, topic_chat_id=0):
    try:
        # Verify that the class exists
        kelas = find_by_id(id=class_id)
        if kelas is None:
            raise_error(msg="Class not found")

        # Verify that the topic chat exists within the class
        topic_chat = find_by_topic_chat_id_and_class_id(id=topic_chat_id, class_id=class_id)
        if topic_chat is None:
            raise_error(msg="Topic chat not found")

        # Proceed with deletion
        return repositoriesDB.delete_chat_by_topic_chat_id_and_class_id(id, topic_chat_id, class_id)

    except Exception as e:
        logging.error(f"Error deleting chat by topic chat ID and class ID: {e}")
        raise_error(msg="An error occurred while deleting the chat")
