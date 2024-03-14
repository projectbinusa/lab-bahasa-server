from entitas.schedule.services import find_schedule_db_by_id
from entitas.schedule_instructur import repositoriesDB
from util.other_util import raise_error


def get_schedule_instructur_db_with_pagination(page=1, limit=9, filters=[], to_model=False, to_response="to_response"):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model, to_response=to_response
    )


def find_schedule_instructur_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


def update_schedule_instructur_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)


def insert_schedule_instructur_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)


def delete_schedule_instructur_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)


def get_schedule_instructur_by_schedule_id(schedule_id=0, page=1, limit=9, filters=[], to_model=False,
                                           to_response="to_response"):
    schedule = find_schedule_db_by_id(id=schedule_id, to_model=True)
    if schedule is None:
        raise_error(msg="schedule not found")
    return get_schedule_instructur_db_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model, to_response=to_response
    )


def find_schedule_instructur_by_schedule_id(schedule_id=0, instructur_id=0, to_model=False):
    schedule_instructur = find_schedule_instructur_db_by_id(id=instructur_id, to_model=True)
    if schedule_instructur is None:
        raise_error(msg="schedule instructur not found")
    schedule = find_schedule_db_by_id(id=schedule_id, to_model=True)
    if schedule is None:
        raise_error(msg="Schedule not found")
    return schedule_instructur.to_response()


def update_schedule_instructur_by_schedule_id(schedule_id=0, id=0, json_object={}):
    schedule_instructur = find_schedule_instructur_db_by_id(id=id, to_model=True)
    if schedule_instructur is None:
        raise_error(msg="Schedule Instructur not found")
    json_object["id"] = schedule_instructur.id
    json_object["schedule_id"] = schedule_id
    json_object['is_deteted'] = schedule_instructur.is_deteted
    return update_schedule_instructur_db(json_object=json_object)


def delete_schedule_instructur_by_schedule_id(schedule_id=0, instructur_id=0):
    schedule_instructur = find_schedule_instructur_db_by_id(id=instructur_id, to_model=True)
    if schedule_instructur is None:
        raise_error(msg="Schedule Instructur not found")
    delete_schedule_instructur = delete_schedule_instructur_by_id(id=instructur_id)
    if delete_schedule_instructur is None:
        raise_error(msg="Failed to delete")
    return True


def insert_schedule_instructur_db_by_schedule_id(schedule_id, json_object={}):
    # schedule_instructur = find_schedule_instructur_db_by_id(id=id, to_model=True)
    json_object["schedule_id"] = schedule_id
    # json_object['is_deteted'] = schedule_instructur.is_deteted
    return insert_schedule_instructur_db(json_object=json_object)
