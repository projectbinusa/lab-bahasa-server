from pony.orm import *
from database.schema import MessageChatDB, ChatDB, UserDB


# @db_session
# def create_message(json_object={}, to_model=False):
#     try:
#         new_message = MessageChatDB(
#             chat=json_object["chat"],
#             content=json_object["content"],
#             sender=json_object["sender"],
#             class_id=json_object["class_id"]
#         )
#         commit()
#         if to_model:
#             return new_message.to_model()
#         else:
#             return new_message.to_model().to_json()
#     except Exception as e:
#         print("error question insert: ", e)
#     return

@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in MessageChatDB).order_by(desc(MessageChatDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(id=item["value"])
            elif item["field"] == "content":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.content)

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
        print("error Message getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def update_message_chat(json_object=None, to_model=False):
    try:
        updated_message_chat = MessageChatDB[json_object["id"]]
        if "chat" in json_object:
            updated_message_chat.chat = json_object["chat"]
        if "content" in json_object:
            updated_message_chat.content = json_object["content"]
        if "sender" in json_object:
            updated_message_chat.sender = json_object["sender"]
        if "class_id" in json_object:
            updated_message_chat.class_id = json_object["class_id"]

        commit()

        if to_model:
            return updated_message_chat.to_model()
        else:
            return updated_message_chat.to_model().to_response()
    except Exception as e:
        print("error MessageChatDB update_chat " + str(e))
        return

@db_session
def delete_message_chat_by_id(id=None):
    try:
        MessageChatDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Chat delete: ", e)
    return


@db_session
def create_message(sender_id, chat_id, content):
    sender = UserDB.get(id=sender_id)
    chat = ChatDB.get(id=chat_id)
    return MessageChatDB(sender=sender, chat=chat, content=content)


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in MessageChatDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def get_chat_messagess(chat_id):
    chat = ChatDB.get(id=chat_id)
    return chat.messages

@db_session
def get_last_message(chat_id):
    try:
        last_message = select(m for m in MessageChatDB if m.chat_id == chat_id).order_by(desc(MessageChatDB.created_date)).first()
        if last_message:
            return last_message.to_model()
        else:
            return None
    except Exception as e:
        print("Error in get_last_message: ", e)
        return None


@db_session
def find_by_message_by_user_id_and_chat_id(chat_id=None, user_id=0):
    data_in_db = select(s for s in MessageChatDB if s.chat_id == chat_id and s.user_id == user_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def update_delete_by_id(id=None, is_deleted=False):
    try:
        MessageChatDB[id].is_deleted = is_deleted
        commit()
        return True
    except Exception as e:
        print("error Room delete: ", e)
    return