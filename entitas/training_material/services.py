from entitas.training_material import repositoriesDB

def get_training_material_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )

def get_training_material_by_training_id_with_pagination(page=1, limit=9, filters=[], training_id=0, to_model=False):
    return repositoriesDB.find_by_training_id_with_pagination(
        page=page, limit=limit, filters=filters, training_id=training_id, to_model=to_model
    )

def find_training_material_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()



def update_training_material_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)

def insert_training_material_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)


def delete_training_material_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

