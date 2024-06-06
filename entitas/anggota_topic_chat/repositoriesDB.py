from pony.orm import *

from database.schema import AnggotaTopicChatDB


@db_session
def add_member_to_topic_chat_by_topic_chat_id_by_class_id(topic_chat_id, class_id, json_object={}, to_model=False):
    try:
        new_member = AnggotaTopicChatDB(
            topic_chat_id=topic_chat_id,
            class_id=class_id,
            user_id=json_object["user_id"],
            role=json_object["role"],
        )
        commit()
        if to_model:
            return new_member.to_model()
        else:
            return new_member.to_model().to_json()
    except Exception as e:
        print("error anggotaTopic insert: ", e)
    return None


@db_session
def get_member_by_topic_chat_id_by_class_id(topic_chat_id, class_id, page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(
            s for s in AnggotaTopicChatDB if (s.topic_chat_id == topic_chat_id) and (s.class_id == class_id)).order_by(
            desc(AnggotaTopicChatDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(id=item["value"])
            elif item["field"] == "role":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.role)

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
        print("error AnggotaChat getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def delete_member_topic_by_id_by_class_id(id=None, class_id=None):
    try:
        AnggotaTopicChatDB.get(id=id, class_id=class_id).delete()
        commit()
        return True
    except Exception as e:
        print("error Chat delete: ", e)
        return False