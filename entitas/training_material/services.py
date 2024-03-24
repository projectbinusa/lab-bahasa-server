from entitas.training_material import repositoriesDB
from util.other_util import raise_error

def get_training_material_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )

def get_training_material_by_training_id_with_pagination(page=1, limit=9, filters=[], training_id=0, to_model=False):
    return repositoriesDB.find_by_training_id_with_pagination(
        page=page, limit=limit, filters=filters, training_id=training_id, to_model=to_model
    )

def get_training_material_by_training_id_for_instructur(page=1, limit=9, filters=[], training_id=0, user_id=0, to_model=False):
    from entitas.schedule_user.services import get_schedule_ids_by_user_id
    from entitas.schedule.services import get_training_ids_by_schedule_ids
    schedule_ids = get_schedule_ids_by_user_id(user_id=user_id)
    training_ids = get_training_ids_by_schedule_ids(schedule_ids=schedule_ids)
    # print('user_id ',user_id ,' schedule_ids ',schedule_ids ,' training_ids',training_ids, 'training_id ',training_id)
    if training_id not in training_ids:
        raise_error("have no access")

    return repositoriesDB.find_by_training_id_with_pagination(
        page=page, limit=limit, filters=filters, training_id=training_id, to_model=to_model
    )

def find_training_material_by_training_id_and_material_id(training_id=0, material_id=0):
    return repositoriesDB.find_by_training_id_and_material_id(training_id=training_id, material_id=material_id)

def get_material_ids_by_training_id(training_id=0):
    return repositoriesDB.get_material_ids_by_training_id(training_id=training_id)

def delete_training_material_by_material_id(material_id=0):
    return repositoriesDB.delete_by_material_id(material_id=material_id)

def update_training_materia_for_material_name_by_material_id(material_id=0, material_name=''):
    return repositoriesDB.update_material_name_by_material_id(material_id=material_id, material_name=material_name)

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

