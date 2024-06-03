from pony.orm import *
from database.schema import ChatDB, UserDB, MessageChatDB


# @db_session
# def create_chat(json_object={}, to_model=False):
#     try:
#         new_chat = ChatDB(
#             name=json_object["name"],
#             is_group=json_object["is_group"],
#             users=','.join(json_object['users']),
#             # users=json_object["users"],
#             # messages=json_object["messages"],
#             # class_id=json_object['class_id']
#         )
#         commit()
#         if to_model:
#             return new_chat.to_model()
#         else:
#             return new_chat.to_model().to_json()
#     except Exception as e:
#         print("error question insert: ", e)
#     return

@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in ChatDB).order_by(desc(ChatDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(id=item["value"])
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.name)

        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error Chat getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def update_chat(json_object=None, to_model=False):
    try:
        updated_chat = ChatDB[json_object["id"]]
        if "name" in json_object:
            updated_chat.name = json_object["name"]
        if "is_group" in json_object:
            updated_chat.is_group = json_object["is_group"]
        if "users" in json_object:
            updated_chat.users = json_object["users"]
        if "messages" in json_object:
            updated_chat.messages = json_object["messages"]
        if "class_id" in json_object:
            updated_chat.class_id = json_object["class_id"]

        commit()

        if to_model:
            return updated_chat.to_model()
        else:
            return updated_chat.to_model().to_response()
    except Exception as e:
        print("error chatDb update_chat " + str(e))
        return


@db_session
def delete_chat_by_id(id=None):
    try:
        ChatDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Chat delete: ", e)
    return

# @db_session
# def create_chat(name, is_group):
#     chat = ChatDB(name=name, is_group=is_group)
#     commit()
#     return chat

# @db_session
# def create_chat(json_object={}, to_model=False):
#     try:
#         new_chat = ChatDB(
#             name=json_object["name"],
#             is_group=json_object["is_group"]
#             # users=json_object["users"],
#             # messages=json_object["messages"],
#             # class_id=json_object['class_id']
#         )
#         commit()
#         if to_model:
#             return new_chat.to_model()
#         else:
#             return new_chat.to_model().to_json()
#     except Exception as e:
#         print("error chat insert: ", e)
#     return


# @db_session
# def add_user_to_chat(json_object={}, to_model=False):
#     try:
#         chat_id = json_object["chat_id"]
#         user_id = json_object["user_id"]
#
#         chat = ChatDB.get(id=chat_id)
#         user = UserDB.get(id=user_id)
#
#         if not chat:
#             raise ValueError("Chat not found")
#         if not user:
#             raise ValueError("User not found")
#
#         print("ini chat id di repo => ", chat_id)
#         print("ini user id di repo => ", user_id)
#
#         chat.users.add(user)
#         commit()
#
#         if to_model:
#             return chat.to_model()
#         else:
#             return chat.to_model().to_json()
#     except Exception as e:
#         print("error adding user to chat: ", e)
#         return None

# @db_session
# def create_chat(json_object={}):
#     try:
#         new_chat = ChatDB(
#             name=json_object.get("name", ""),
#             is_group=json_object.get("is_group", False)
#         )
#         commit()
#         return new_chat
#     except Exception as e:
#         print("Error creating chat: ", e)
#         return None
#
#
# @db_session
# def add_user_to_chat(json_object={}):
#     try:
#         chat = ChatDB.get(id=json_object["chat_id"])
#         user_ids = json_object.get("user_ids", [])
#         print("user_ids di repo => ", user_ids)
#         if not isinstance(user_ids, list):
#             user_ids = [user_ids]
#         for user_id in user_ids:
#             user = UserDB.get(id=user_id)
#             if user:
#                 chat.users.add(user)
#         commit()
#         return chat
#     except Exception as e:
#         print("Error adding user to chat: ", e)
#         return None

@db_session
def insert_private_chat(json_object={}, to_model=False):
    try:
        new_chat = ChatDB(
            sender_id=json_object["sender_id"],
            receiver_id=json_object["receiver_id"],
            content=json_object["content"],
            is_group=json_object["is_group"]
        )
        commit()
        if to_model:
            return new_chat.to_model()
        else:
            return new_chat.to_model().to_response()
    except Exception as e:
        print("error Message insert: ", e)
    return None

@db_session
def get_chats_for_user(user_id, sender_id=None):
    try:
        if sender_id:
            chats = select(m for m in ChatDB if (m.receiver_id == user_id and m.sender_id == sender_id) or
                                                        (m.receiver_id == sender_id and m.sender_id == user_id))
        else:
            chats = select(m for m in ChatDB if m.receiver_id == user_id or m.sender_id == user_id)
        return [m.to_model() for m in chats]
    except Exception as e:
        print("error getting chats for user: ", e)
        return []




# @db_session
# def add_user_to_chat(chat_id, user_id):
#     chat = ChatDB.get(id=chat_id)
#     user = UserDB.get(id=user_id)
#     chat.users.add(user)
#     commit()


# @db_session
# def create_message(sender_id, chat_id, content):
#     message = MessageChatDB.get(sender_id=sender_id, chat_id=chat_id, content=content)
#     commit()
#     return message


# @db_session
# def create_chat(name, is_group):
#     return ChatDB(name=name, is_group=is_group)

# @db_session
# def add_user_to_chat(chat_id, user_id):
#     chat = ChatDB.get(id=chat_id)
#     user = UserDB.get(id=user_id)
#     chat.users.add(user)

# @db_session
# def
@db_session
def get_chat(chat_id):
    return ChatDB.get(id=chat_id)

@db_session
def get_user_chats(user_id):
    user = UserDB.get(id=user_id)
    return user.private_chats + user.group_chats


@db_session
def find_by_chat_by_message_id(chat=None, user_id=0):
    data_in_db = select(s for s in ChatDB if s.chat == chat and s.user_id == user_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in ChatDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()