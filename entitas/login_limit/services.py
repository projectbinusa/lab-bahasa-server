import uuid

from entitas.kelas_user.services import find_kelas_user_db_by_id
from entitas.login_limit import repositoriesDB
# from entitas.login_limit.services import find_kelas_user_db_by_id
from entitas.user.repositoriesDB import find_by_id
from util.other_util import raise_error
from config.config import LOG_BOOK_FOLDER, DOMAIN_FILE_URL

def get_login_limits_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_login_limits_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


def get_login_limits_by_class_id(class_id=0, page=1, limit=9, filters=[], to_model=False):
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    print("ini class id =====>")
    if kelas is None:
        raise_error(msg="class not found")
    return repositoriesDB.get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)


def update_login_limits_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)


def insert_login_limits_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)


def insert_login_limits_db_by_class_id(class_id=0, json_object={}):
    kelas_user = repositoriesDB.find_by_login_limits_id_and_class_id(class_id=class_id)
    # user_name = find_by_id(id=json_object['user_id'])
    print("class_id ====>" ,class_id, "data ==>", json_object)
    if kelas_user is not None:
        repositoriesDB.update_delete_by_id(id=kelas_user.id, is_deleted=False)
        return True
    json_object['class_id'] = class_id
    insert_login_limits_db(json_object=json_object)
    return True


def delete_login_limits_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)


# def delete_login_limits_by_login_limits_id_and_user_id(user_id=0, login_limits_id=0):
#     return repositoriesDB.delete_by_login_limits_id_and_user_id(user_id=user_id, login_limits_id=login_limits_id)


def find_login_limits_by_ids(class_id=0, login_limits_id=0):
    login_limits = find_login_limits_db_by_id(id=login_limits_id, to_model=True)
    if login_limits is None:
        raise_error(msg="login limits not found")
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if kelas is None:
        raise_error(msg="class not found")
    return login_limits.to_response()


def update_login_limits_by_class_id(class_id=0, id=0, json_object={}):
    login_limits = find_login_limits_db_by_id(id=id, to_model=True)
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if login_limits is None:
        raise_error(msg="log book not found")
    if kelas is None:
        raise_error(msg="kelas not found")
    json_object["id"] = login_limits.id
    json_object["class_id"] = class_id
    return update_login_limits_db(json_object=json_object)


def delete_login_limits_by_class_id(class_id=0, id=0):
    login_limits = find_login_limits_db_by_id(id=id, to_model=True)
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if kelas is None:
        raise_error(msg="Kelas not found")
    if login_limits is None:
        raise_error(msg="login limits not found")
    delete_login_limits = delete_login_limits_by_id(id=id)
    if delete_login_limits is None:
        raise_error(msg="Failed to delete")
    return True
