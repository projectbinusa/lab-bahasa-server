from pony.orm import *
from database.schema import MessageChatDB

@db_session
def create_message_chat(json_object={}, to_model=False):
    try:
        new_message = MessageChatDB(
            chat=json_object["chat"],
            content=json_object["content"],
            sender=json_object["sender"],
            class_id=json_object["class_id"]
        )
        commit()
        if to_model:
            return new_message.to_model()
        else:
            return new_message.to_model().to_json()
    except Exception as e:
        print("error question insert: ", e)
    return

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