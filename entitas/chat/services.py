from database.schema import ChatDB
from entitas.chat import repositoriesDB

def insert_chat_db(json_object={}):
    return repositoriesDB.create_chat(json_object=json_object)

def get_chat_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )

def update_chat_db(json_object={}):
    return repositoriesDB.update_chat(json_object=json_object)

def delete_chat_by_id(id=0):
    return repositoriesDB.delete_chat_by_id(id)