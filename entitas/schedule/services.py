from entitas.schedule import repositoriesDB
from util.shorter import ServiceShorter
from config.config import SALT_SORTER
from util.other_util import raise_error
from datetime import datetime
def get_schedule_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )

def get_calendar(year='', month='', user_id=0):
    year = int(year) if year not in ['', '0'] else datetime.now().year
    month = int(month) if month not in ['', '0'] else datetime.now().month
    ids = []

    if user_id not in [None, 0]:
        from entitas.schedule_user.services import get_schedule_ids_by_user_id
        ids = get_schedule_ids_by_user_id(user_id=user_id)
    return repositoriesDB.get_all_by_time(year=year, month=month, ids=ids)

def get_calendar_instructur(year='', month='', user_id=0):
    year = int(year) if year not in ['', '0'] else datetime.now().year
    month = int(month) if month not in ['', '0'] else datetime.now().month
    ids = []

    if user_id not in [None, 0]:
        from entitas.schedule_user.services import get_schedule_ids_by_user_id
        ids = get_schedule_ids_by_user_id(user_id=user_id)
    return repositoriesDB.get_all_by_time(year=year, month=month, ids=ids)

def get_mytraining_instructur(user_id=0, page=1, limit=9, filters=[]):
    ids = []
    if user_id not in [None, 0]:
        from entitas.schedule_instructur.services import get_schedule_ids_by_user_id
        ids = get_schedule_ids_by_user_id(user_id=user_id)
    filters.append({'field': 'ids', 'value': ids})
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=False
    )

def get_mytraining_student(user_id=0, page=1, limit=9, filters=[]):
    ids = []
    if user_id not in [None, 0]:
        from entitas.schedule_user.services import get_schedule_ids_by_user_id
        ids = get_schedule_ids_by_user_id(user_id=user_id)
    filters.append({'field': 'ids', 'value': ids})
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=False
    )

def get_training_ids_by_schedule_ids(schedule_ids=[]):
    return repositoriesDB.get_training_ids_by_schedule_ids(schedule_ids=schedule_ids)

def find_schedule_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


def update_schedule_for_finish(id=0, is_finish=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        raise_error('Data not found')
    return repositoriesDB.update_is_finish(id=id, is_finish=is_finish)

def find_schedule_for_instructur_by_id(id=0, user_id=0, to_model=False):
    from entitas.schedule_user.services import is_found_user_id_and_schedule_id
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if not is_found_user_id_and_schedule_id(schedule_id=id, user_id=user_id):
        raise_error("have no access")
    if to_model:
        return result
    return result.to_response()

def update_schedule_db(json_object={}):
    schedule = repositoriesDB.find_by_id(id=json_object['id'])
    if schedule is None:
        raise_error("Schedule not found")
    if schedule.training_id != json_object['training_id']:
        from entitas.training.services import find_training_db_by_id
        training = find_training_db_by_id(id=json_object['training_id'], to_model=True)
        if training is None:
            raise_error("Training not found")
        json_object['training_name'] = training.name
        json_object['training_image_url'] = training.image_url

    return repositoriesDB.update(json_object=json_object)

def insert_schedule_db(json_object={}):
    from entitas.training.services import find_training_db_by_id
    training = find_training_db_by_id(id=json_object['training_id'], to_model=True)
    if training is None:
        raise_error("Training not found")
    json_object['training_name'] = training.name
    json_object['training_image_url'] = training.image_url
    data = repositoriesDB.insert(json_object=json_object)
    serviceShorter = ServiceShorter(salt_shorter=SALT_SORTER, url_id=data['id'])
    data['link'] = serviceShorter.encode()
    repositoriesDB.update_link(id=data['id'], link=data['link'])
    return data


def delete_schedule_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

