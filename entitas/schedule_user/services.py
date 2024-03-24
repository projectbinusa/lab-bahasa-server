from entitas.schedule_user import repositoriesDB
from util.other_util import raise_error

def get_schedule_user_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )

def find_schedule_user_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()

def get_schedule_ids_by_user_id(user_id=0):
    return repositoriesDB.get_schedule_ids_by_user_id(user_id=user_id)

def update_schedule_user_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)

def insert_schedule_user_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)


def delete_schedule_user_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

def update_schedule_user_for_instructur(schedule_id=0, schedule_user_id=0, instructur_id=0, score=0):
    if not repositoriesDB.is_found_user_id_and_schedule_id(user_id=instructur_id, schedule_id=schedule_id):
        raise_error("Have no access")
    schedule_user = repositoriesDB.find_by_id(id=schedule_user_id)
    if schedule_user is None:
        raise_error("Data not found")
    if schedule_user.schedule_id != schedule_id:
        raise_error("Data not match")
    return repositoriesDB.update_score(id=schedule_user_id, score=score)

def schedule_user_generate_certificate(filters=[]):
    from util.image_util import ImageUtil
    datas ,_ = repositoriesDB.get_all_with_pagination(page=1, limit=0, filters=filters)
    imageUtil = ImageUtil()
    for data in datas:
        repositoriesDB.update_certificate(id=data['id'], certificate_url=imageUtil.write(text=data['user_name']))
    return True

