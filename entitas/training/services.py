from entitas.training import repositoriesDB
from util.other_util import raise_error

def get_training_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )

def get_training_for_instructur(page=1, limit=9, filters=[], user_id=0, to_model=False):
    from entitas.schedule_user.services import get_schedule_ids_by_user_id
    from entitas.schedule.services import get_training_ids_by_schedule_ids
    schedule_ids = get_schedule_ids_by_user_id(user_id=user_id)
    training_ids = get_training_ids_by_schedule_ids(schedule_ids=schedule_ids)
    filters.append({'field': 'training_ids', 'value': training_ids})

    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )

def instructur_preview_training_db_by_id(id=0, user_id=0, to_model=False):
    from entitas.schedule_user.services import get_schedule_ids_by_user_id
    from entitas.schedule.services import get_training_ids_by_schedule_ids
    schedule_ids = get_schedule_ids_by_user_id(user_id=user_id)
    training_ids = get_training_ids_by_schedule_ids(schedule_ids=schedule_ids)
    if id not in training_ids:
        raise_error("have no access")

    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()

def find_training_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


def update_training_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)


def insert_training_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)


def delete_training_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)
