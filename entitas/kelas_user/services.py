from entitas.kelas_user import repositoriesDB
from entitas.user.services import find_user_db_by_id
from util.other_util import raise_error

def get_kelas_user_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )

def find_kelas_user_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()

def find_kelas_user_for_student_by_id(id=0, user_id=0, to_model=False):
    result = repositoriesDB.find_by_kelas_user_id_and_user_id(id=id, user_id=user_id)
    if result is None:
        raise_error('data not found')
    if to_model:
        return result
    if result.user_id != user_id:
        raise_error('have no access')
    return result.to_response()

def get_kelas_user_ids_by_user_id(user_id=0):
    return repositoriesDB.get_kelas_user_ids_by_user_id(user_id=user_id)

def update_kelas_user_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)

def kelas_user_active_db(json_object={}):
    return repositoriesDB.class_active(json_object=json_object)

def insert_kelas_user_db(json_object={}, user_id=0):
    return repositoriesDB.insert(json_object=json_object)

def delete_kelas_user_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)
