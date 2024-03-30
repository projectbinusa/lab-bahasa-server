from entitas.assignment import repositoriesDB
from util.other_util import raise_error

def get_assignment_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_assignment_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()

def find_assignment_instructur_by_id(id=0, instructur_id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        raise_error('Assign not found')
    if to_model:
        return result
    if instructur_id != result.instructur_id:
        raise_error('have no access')
    return result.to_response()

def update_assignment_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)

def update_assignment_instructur(json_object={}, instructur_id=0):
    data = repositoriesDB.find_by_id(id=json_object['id'])
    if data is None:
        raise_error('data not found')
    if data.instructur_id != instructur_id:
        raise_error('have no access')
    json_object['instructur_id'] = instructur_id
    json_object["schedule_id"] = data.schedule_id
    return repositoriesDB.update(json_object=json_object)

def insert_assignment_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)

def insert_assignment_instructur(json_object={}):
    from entitas.schedule.services import find_schedule_db_by_id
    schedule = find_schedule_db_by_id(id=json_object['schedule_id'], to_model=True)
    if schedule is None:
        raise_error('data schedule not found')
    json_object['training_id'] = schedule.training_id
    return repositoriesDB.insert(json_object=json_object)


def delete_assignment_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

def delete_assignment_instructur_by_id(id=0, instructur_id=0):
    data = repositoriesDB.find_by_id(id=id)
    if data is None:
        raise_error('data not found')
    if data.instructur_id != instructur_id:
        raise_error('have no access')
    return repositoriesDB.delete_by_id(id=id)
