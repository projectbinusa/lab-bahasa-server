from database.schema import ChatDB
from entitas.chat import repositoriesDB
from entitas.message_chat.repositoriesDB import create_message, get_chat_messagess, \
    find_by_message_by_user_id_and_chat_id, update_delete_by_id
from entitas.user.repositoriesDB import get_user


def insert_chat_db(json_object={}):
    return repositoriesDB.create_chat(json_object=json_object)

def get_chat_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )

def update_chat_db(json_object={}):
    return repositoriesDB.update_chat(json_object=json_object)

def delete_chat_by_id(id=0):
    return repositoriesDB.delete_chat_by_id(id)


def insert_message_service(json_object={}):
    return repositoriesDB.insert_private_chat(json_object=json_object)

def get_messages_for_user_service(user_id, sender_id=None):
    return repositoriesDB.get_chats_for_user(user_id, sender_id)

# def start_private_chat(user_ids, json_object={}):
#     print("Ini users id di service ==> ", user_ids)
#     print("Ini json_object di service ==> ", json_object)
#     if len(user_ids) != 2:
#         raise ValueError("Exactly two users are required for a private chat.")
#     chat = repositoriesDB.create_chat(json_object=json_object)
#     if chat is None:
#         raise ValueError("Failed to create chat.")
#     for user_id in user_ids:
#         add_user_json = {
#             "chat_id": chat.id,
#             "user_ids": user_id
#         }
#         repositoriesDB.add_user_to_chat(json_object=add_user_json)
#     return chat
#
#
# def start_group_chat(user_ids, json_object={}):
#     print("Ini users id di service ==> ", user_ids)
#     print("Ini json_object di service ==> ", json_object)
#     if not user_ids:
#         raise ValueError("At least one user is required for a group chat.")
#     chat = repositoriesDB.create_chat(json_object=json_object)
#     if chat is None:
#         raise ValueError("Failed to create chat.")
#     for user_id in user_ids:
#         repositoriesDB.add_user_to_chat(chat.id, user_id)
#     return chat


# def start_group_chat(user_ids, name):
#     if not name:
#         raise ValueError("Group chat must have a name.")
#     chat = repositoriesDB.create_chat(name=name, is_group=True)
#     for user_id in user_ids:
#         repositoriesDB.add_user_to_chat(chat.id, user_id)
#     return chat




# def send_message(sender_id, chat_id, content):
#     message = create_message(sender_id=sender_id, chat_id=chat_id, content=content)
#     return message


# def send_message(sender_id, chat_id, content):
#     return create_message(sender_id, chat_id, content)

# def get_chat_messages(chat_id):
#     return get_chat_messagess(chat_id)


# def get_user_chats(user_id):
#     user = get_user(user_id)
#     if not user:
#         raise ValueError("User not found.")
#
#     chats = repositoriesDB.get_user_chats(user_id)
#     for chat in chats:
#         chat.last_message = get_last_message(chat.id)
#     return chats