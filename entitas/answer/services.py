from entitas.answer import repositoriesDB
from entitas.answer.repositoriesDB import get_all_with_pagination, update
from entitas.kelas_user.repositoriesDB import find_kelas_user_db_by_id
from entitas.user.repositoriesDB import find_by_id
from util.other_util import raise_error


def get_services_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_services_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


def find_answer_by_class_id(class_id=0, answer_id=0):
    answer = find_answer_db_by_id(id=answer_id, to_model=True)
    if answer is None:
        raise_error(msg="answer not found")
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if kelas is None:
        raise_error(msg="class not found")
    return answer.to_response()


def find_answer_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


def get_list_by_class_id(class_id=0, page=1, limit=9, filters=[], to_model=False):
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    print("ini class id =====>", class_id)
    if kelas is None:
        raise_error(msg="class not found")
    return get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)


def update_services_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)


def update_answer_by_class_id(class_id=0, id=0, json_object={}):
    # try:
    answer = find_answer_db_by_id(id=id, to_model=True)
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if answer is None:
        raise_error(msg="answer not found")
    if kelas is None:
        raise_error(msg="kelas not found")
    json_object["id"] = answer.id
    json_object["class_id"] = class_id
    return update(json_object=json_object)
    # except Exception as e:
    #     print("Error:", e)
    #     return None


def insert_answer_db(json_object={}):
    return repositoriesDB.create_profile_answer(json_object=json_object)

def create_answer_service(answer_time_user, class_id=0, json_object={}, user_id=0):
    # try:
    kelas_user = repositoriesDB.find_by_answer_id_and_class_id(class_id=class_id)
    user = find_by_id(id=user_id)
    print("ini user user_id di services", user_id)
    if kelas_user is not None:
        repositoriesDB.update_delete_by_id(id=kelas_user.id, is_deleted=False)
        return True
    if user is None:
        raise_error(msg="user not found")
    json_object['class_id'] = class_id
    json_object['user_id'] = user_id
    insert_answer_db(json_object=json_object)
    return True
    # except Exception as e:
    #     print("Error:", e)
    #     return None


def delete_answer_db_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)


def delete_answer_by_class_id(class_id=0, id=0):
    answer = find_answer_db_by_id(id=id, to_model=True)
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if kelas is None:
        raise_error(msg="Kelas not found")
    if answer is None:
        raise_error(msg="answer not found")
    delete_answer = delete_answer_db_by_id(id=id)
    if delete_answer is None:
        raise_error(msg="Failed to delete")
    return True

def get_answer_by_class_id_and_user_id(class_id=0, page=1, user_id=0, limit=9, filters=[], to_model=False):
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    user = find_by_id(id=user_id)
    if kelas is None:
        raise_error(msg="kelas not found")
    if user is None:
        raise_error(msg="user not found")
    return get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)
