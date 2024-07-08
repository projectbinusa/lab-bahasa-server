from entitas.user.repositoriesDB import find_by_id
from entitas.kelas_user.services import find_kelas_user_db_by_id
from entitas.multiple_choice_questions import repositoriesDB
from util.other_util import raise_error

def get_services_db_with_pagination(page=1, limit=9, filters=[], to_model=False, class_id=0):
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if kelas is None:
        raise_error(msg="kelas not found")
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )



def find_services_db_by_id(class_id=0, id=0, to_model=False):
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if kelas is None:
        raise_error(msg="kelas not found")
    result = repositoriesDB.find_by_id_multiple_choice_question_by_class_id(id=id, class_id=class_id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


# def update_services_db(json_object={}):
#     return repositoriesDB.update_multiple_choice_question(json_object=json_object)

def insert_services_db(json_objects=[], user_id=0, class_id=0, user_name=''):
    print("user_id in service => ", user_id)
    user = find_by_id(id=user_id)
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if user is None:
        raise_error(msg="user not found")
    if kelas is None:
        raise_error(msg="kelas not found")
    # Tidak perlu menambahkan class_id, user_id, user_name ke json_objects karena ini daftar
    return repositoriesDB.add_multiple_choice_questions(user_id=user_id, class_id=class_id, user_name=user_name, json_objects=json_objects)


def update_service_db(json_object={}, user_id=0, class_id=0, user_name='', id=0):
    print("user_id in service => ", user_id)
    user = find_by_id(id=user_id)
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    question = repositoriesDB.find_by_id_multiple_choice_question_by_class_id(id=id, class_id=class_id)

    if user is None:
        raise_error(msg="user not found")
    if kelas is None:
        raise_error(msg="kelas not found")
    if question is None:
        raise_error(msg="multiple choice question not found")

    json_object['id'] = id
    json_object['user_id'] = user_id
    json_object['user_name'] = user_name
    json_object['class_id'] = class_id

    return repositoriesDB.update_multiple_choice_question(user_id=user_id, class_id=class_id, user_name=user_name,
                                                          json_object=json_object)


def delete_services_by_id(id=0, class_id=0,):
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if kelas is None:
        raise_error(msg="kelas not found")
    return repositoriesDB.delete_by_id_and_class_id(id=id, class_id=class_id)

