from entitas.absent import repositoriesDB
from util.other_util import raise_error
import datetime

def get_absent_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_absent_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()

def update_absent_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)

def insert_absent_db(json_object={}):
    from entitas.schedule.services import find_schedule_db_by_id
    from entitas.user.services import find_user_db_by_id
    schedule = find_schedule_db_by_id(id=json_object['schedule_id'], to_model=True)
    if schedule is None:
        raise_error("schedule not found")
    json_object['training_id'] = schedule.training_id
    json_object['training_name'] = schedule.training_name
    json_object['absent_date'] = datetime.datetime.now()

    user = find_user_db_by_id(id=json_object['user_id'], to_model=True)
    if user is None:
        raise_error("user not found")
    json_object['user_name'] = user.name
    return repositoriesDB.insert(json_object=json_object)


def delete_absent_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)