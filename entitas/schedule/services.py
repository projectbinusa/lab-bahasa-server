from entitas.schedule import repositoriesDB
from util.shorter import ServiceShorter
from config.config import SALT_SORTER
from util.other_util import raise_error

def get_schedule_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_schedule_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
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

    return repositoriesDB.update(json_object=json_object)

def insert_schedule_db(json_object={}):
    from entitas.training.services import find_training_db_by_id
    training = find_training_db_by_id(id=json_object['training_id'], to_model=True)
    if training is None:
        raise_error("Training not found")
    json_object['training_name'] = training.name
    data = repositoriesDB.insert(json_object=json_object)
    serviceShorter = ServiceShorter(salt_shorter=SALT_SORTER, url_id=data['id'])
    data['link'] = serviceShorter.encode()
    repositoriesDB.update_link(id=data['id'], link=data['link'])
    return data


def delete_schedule_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

