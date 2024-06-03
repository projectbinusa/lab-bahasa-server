from pony.orm import *
from database.schema import ChatDB

@db_session
def create_chat(json_object={}, to_model=False):
    try:
        new_chat = ChatDB(
            name=json_object["name"],
            is_group=json_object["is_group"],
            users=json_object["users"],
            messages=json_object["messages"],
            class_id=json_object['class_id']
        )
        commit()
        if to_model:
            return new_chat.to_model()
        else:
            return new_chat.to_model().to_json()
    except Exception as e:
        print("error question insert: ", e)
    return

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
        if "is_group" in json_object:
            updated_chat.is_group = json_object["is_group"]
        if "content" in json_object:
            updated_chat.content = json_object["content"]
        if "sender_id" in json_object:
            updated_chat.sender_id = json_object["sender_id"]
        if "receiver_id" in json_object:
            updated_chat.receiver_id = json_object["receiver_id"]
        if "group_id" in json_object:
            updated_chat.group_id = json_object["group_id"]
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