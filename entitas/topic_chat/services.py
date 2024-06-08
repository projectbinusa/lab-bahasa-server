from entitas.kelas_user import services
from entitas.topic_chat import repositoriesDB
from util.other_util import raise_error


def insert_topic_chat_db(class_id, json_object={}):
    if not services.find_kelas_user_db_by_id(class_id):
        return {"class id not found"}
    return repositoriesDB.create_topic_chat_by_class_id(class_id, json_object=json_object)


def get_topic_chat_db_with_pagination(class_id, page=1, limit=9, filters=[], to_model=False):
    if not services.find_kelas_user_db_by_id(class_id):
        return {"class id not found"}
    return repositoriesDB.get_all_with_pagination_by_class_id(
        class_id, page=page, limit=limit, filters=filters, to_model=to_model
    )


def update_topic_chat_db(class_id, json_object={}):
    if not services.find_kelas_user_db_by_id(class_id):
        return {"class id not found"}
    return repositoriesDB.update_topic_chat(class_id, json_object=json_object)


def delete_topic_chat_by_id(id=0, class_id=0):
    if not services.find_kelas_user_db_by_id(class_id):
        return {"class id not found"}
    return repositoriesDB.delete_anggota_topic_by_id_by_class_id(id, class_id)


def find_topic_chat_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        raise_error('topic chat id not found')
    if to_model:
        return result
    return result.to_response()
