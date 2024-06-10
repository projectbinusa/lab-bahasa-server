from pony.orm import *

from database.schema import TopicChatDB
from util.other_util import raise_error


@db_session
def create_topic_chat_by_class_id(class_id, json_object={}, to_model=False):
    try:
        new_topic = TopicChatDB(
            class_id=class_id,
            name=json_object["name"],
            is_removed=json_object["is_removed"],
        )
        commit()
        if to_model:
            return new_topic.to_model()
        else:
            return new_topic.to_model().to_json()
    except Exception as e:
        print("error topic chat insert: ", e)
    return


@db_session
def get_all_with_pagination_by_class_id(class_id, page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in TopicChatDB if (s.class_id == class_id)).order_by(desc(TopicChatDB.id))
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
        print("error Topic Chat getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in TopicChatDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def update_topic_chat(class_id=None, json_object=None, to_model=False):
    try:
        updated_topic_chat = TopicChatDB.get(id=json_object["id"], class_id=class_id)
        if "name" in json_object:
            updated_topic_chat.name = json_object["name"]
        if "is_removed" in json_object:
            updated_topic_chat.is_removed = json_object["is_removed"]

        commit()

        if to_model:
            return updated_topic_chat.to_model()
        else:
            return updated_topic_chat.to_model().to_response()
    except Exception as e:
        print("error Topic CHat update " + str(e))
        return


@db_session
def delete_anggota_topic_by_id_by_class_id(id=None, class_id=None):
    try:
        TopicChatDB.get(id=id, class_id=class_id).delete()
        commit()
        return True
    except Exception as e:
        print("error Group delete: ", e)
        return False
