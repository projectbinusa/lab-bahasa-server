from entitas.kelas_user.repositoriesDB import find_kelas_user_db_by_id
from entitas.whiteboard import repositoriesDB
from entitas.whiteboard.repositoriesDB import update, find_by_whiteboard_id_and_class_id, get_all_with_pagination
from util.other_util import raise_error


def get_whiteboard_db_with_pagination(
        page=1, limit=9, name="", to_model=False, filters=[], to_response="to_response"
):
    return repositoriesDB.get_all_with_pagination(
        page=page,
        limit=limit,
        name=name,
        to_model=to_model,
        filters=filters,
        to_response=to_response,
    )


def find_whiteboard_db_by_id(id=0, to_model=False):
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


def update_whiteboard_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)


def get_whiteboard_db_by_class_id(class_id, to_model=True):
    return repositoriesDB.get_all_by_class_id(class_id=class_id, to_model=to_model)


def get_whiteboard_db_with_pagination_by_class(class_id, page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination_by_class(class_id=class_id, page=page, limit=limit, filters=filters,
                                                           to_model=to_model)


def find_whiteboard_by_class_id(class_id=0, whiteboard_id=0):
    whiteboard = find_whiteboard_db_by_id(id=whiteboard_id, to_model=True)
    if whiteboard is None:
        raise_error(msg="whiteboard not found")
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if kelas is None:
        raise_error(msg="class not found")
    return whiteboard.to_response()


def update_whiteboard_by_class_id(class_id=0, id=0, json_object={}):
    # try:
    whiteboard = find_whiteboard_db_by_id(id=id, to_model=True)
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if whiteboard is None:
        raise_error(msg="log book not found")
    if kelas is None:
        raise_error(msg="kelas not found")
    json_object["id"] = whiteboard.id
    json_object["class_id"] = class_id
    return update(json_object=json_object)
    # except Exception as e:
    #     print("Error:", e)
    #     return None


def create_whiteboard_service(class_id=0, json_object={}):
    kelas_user = repositoriesDB.find_by_whiteboard_id_and_class_id(class_id=class_id)
    if kelas_user is not None:
        repositoriesDB.update_delete_by_id(id=kelas_user.id, is_deleted=False)
        return True
    json_object['class_id'] = class_id
    return repositoriesDB.create_profile_manage_student_list(json_object=json_object)


def delete_whiteboard_db_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)


def delete_whiteboard_by_class_id(class_id=0, id=0):
    whiteboard = find_whiteboard_db_by_id(id=id, to_model=True)
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if kelas is None:
        raise_error(msg="Kelas not found")
    if whiteboard is None:
        raise_error(msg="whiteboard not found")
    delete_whiteboard = delete_whiteboard_db_by_id(id=id)
    if delete_whiteboard is None:
        raise_error(msg="Failed to delete")
    return True