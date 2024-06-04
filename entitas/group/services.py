from database.schema import GroupDB
from entitas.group import repositoriesDB

def insert_group_db(class_id, json_object={}):
    return repositoriesDB.create_group_by_class_id(class_id, json_object=json_object)

def get_group_db_with_pagination(class_id, page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination_by_class_id(
        class_id, page=page, limit=limit, filters=filters, to_model=to_model
    )

def update_group_chat_db(class_id, json_object={}):
    return repositoriesDB.update_group_chat(class_id, json_object=json_object)


def delete_group_chat_by_id(id=0, class_id=0):
    return repositoriesDB.delete_anggota_group_by_id_by_class_id(id, class_id)

