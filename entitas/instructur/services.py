from entitas.instructur import repositoriesDB

def get_instructur_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)

def find_instructur_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to.response()

def update_instructur_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)

def insert_instructur_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)

def delete_instructur_db(id=0):
    return repositoriesDB.delete_by_id(id=id)