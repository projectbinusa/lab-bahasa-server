import uuid

from config.config import LOG_BOOK_FOLDER, DOMAIN_FILE_URL
from entitas.kelas_user import repositoriesDB
from entitas.user.services import find_user_db_by_id
from util.excel_util import import_from_excel, export_to_excel
from util.other_util import raise_error


def get_kelas_user_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_kelas_user_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    print("id ==>", id)
    if result is None:
        raise_error('class id not found')
    if to_model:
        return result
    return result.to_response()


def find_kelas_user_for_student_by_id(id=0, user_id=0, to_model=False):
    result = repositoriesDB.find_by_kelas_user_id_and_user_id(id=id, user_id=user_id)
    if result is None:
        raise_error('data not found')
    if to_model:
        return result
    return result.to_response()


def get_kelas_user_ids_by_user_id(user_id=0):
    return repositoriesDB.get_kelas_user_ids_by_user_id(user_id=user_id)


def update_kelas_user_db(json_object={}, file=None):
    if file is None:
        raise raise_error('File not found')
    temp_file = str(uuid.uuid4()) + file.filename.replace(" ", "")
    with open(LOG_BOOK_FOLDER + temp_file, "wb") as f:
        f.write(file.file.read())
    json_object["file"] = DOMAIN_FILE_URL + '/files/' + temp_file
    return repositoriesDB.update(json_object=json_object)


def kelas_user_active_db(json_object={}):
    kelas_user_ids = repositoriesDB.get_kelas_user_ids_by_user_id(json_object.get("user_id", 0))
    if len(kelas_user_ids) >= 1:
        raise_error(msg="Anda sudah memilih satu kelas")

    return repositoriesDB.class_active(json_object=json_object)


def insert_kelas_user_db(json_object={}, file=None):
    try:
        if file is None:
            raise raise_error('File not found')
        temp_file = str(uuid.uuid4()) + file.filename.replace(" ", "")
        with open(LOG_BOOK_FOLDER + temp_file, "wb") as f:
            f.write(file.file.read())
        json_object["file"] = DOMAIN_FILE_URL + '/files/' + temp_file
        return repositoriesDB.insert(json_object=json_object)
    except Exception as e:
        print("Error:", e)
        return None


def delete_kelas_user_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)


def export_kelas_user_to_excel(file_path):
    data, _ = repositoriesDB.get_all_with_pagination(page=1, limit=0, filters=[], to_model=False)
    formatted_data = []
    for idx, item in enumerate(data, start=1):
        item.pop("created_time", None)
        item.pop("updated_time", None)
        item["id"] = idx
        formatted_data.append(item)
    export_to_excel(formatted_data, file_path)
    return file_path


def import_kelas_user_from_excel(file_path):
    data = import_from_excel(file_path)
    for item in data:
        repositoriesDB.insert(json_object=item)
    return len(data)
