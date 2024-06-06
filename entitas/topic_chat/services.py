from entitas.topic_chat import repositoriesDB


def insert_topic_chat_db(class_id, json_object={}):
    return repositoriesDB.create_topic_chat_by_class_id(class_id, json_object=json_object)


def get_topic_chat_db_with_pagination(class_id, page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination_by_class_id(
        class_id, page=page, limit=limit, filters=filters, to_model=to_model
    )


def update_topic_chat_db(class_id, json_object={}):
    return repositoriesDB.update_topic_chat(class_id, json_object=json_object)


def delete_topic_chat_by_id(id=0, class_id=0):
    return repositoriesDB.delete_anggota_topic_by_id_by_class_id(id, class_id)
