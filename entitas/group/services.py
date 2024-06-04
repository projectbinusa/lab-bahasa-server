from database.schema import GroupDB
from entitas.group import repositoriesDB

def insert_group_db(json_object={}):
    return repositoriesDB.create_group(json_object=json_object)

def get_group_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )

def update_group_chat_db(json_object={}):
    return repositoriesDB.update_group_chat(json_object=json_object)

def delete_group_chat_by_id(id=0):
    return repositoriesDB.delete_group_by_id(id)