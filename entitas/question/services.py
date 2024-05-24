from entitas.question import repositoriesDB

def insert_question_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)

def get_question_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )

def delete_question_by_id(id=0):
    return repositoriesDB.delete_by_id(id)

def update_question_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)