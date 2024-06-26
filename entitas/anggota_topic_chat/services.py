from entitas.anggota_topic_chat import repositoriesDB
from entitas.anggota_topic_chat.repositoriesDB import *


def create_member_db(topic_chat_id, class_id, json_object={}):
    return repositoriesDB.add_member_to_topic_chat_by_topic_chat_id_by_class_id(topic_chat_id, class_id,
                                                                                json_object=json_object)


def get_member_by_topic_id_with_pagination(topic_chat_id, class_id, page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_member_by_topic_chat_id_by_class_id(
        topic_chat_id, class_id, page=page, limit=limit, filters=filters, to_model=to_model
    )


def delete_anggota_topic_chat_by_id(id=0, class_id=0):
    return repositoriesDB.delete_member_topic_by_id_by_class_id(id, class_id)


def delete_topic_chat_by_anggota_topic_chat_id_and_class_id(topic_chat_id, class_id, anggota_topic_chat_id):
    if not find_by_anggota_topic_chat_id_and_topic_chat_id(anggota_topic_chat_id, topic_chat_id):
        raise ValueError("Anggota is not authorized to delete this group.")
    return delete_topic_chat_by_topic_chat_id_and_class_id(topic_chat_id, class_id, anggota_topic_chat_id)
