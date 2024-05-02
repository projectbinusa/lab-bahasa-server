import uuid

from entitas.log_book import repositoriesDB
from entitas.schedule.services import find_schedule_db_by_id
from entitas.user.repositoriesDB import find_by_id
from util.other_util import raise_error
from config.config import LOG_BOOK_FOLDER, DOMAIN_FILE_URL

# ervices
def get_log_book_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_log_book_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


def get_log_book_by_schedule_id(schedule_id=0, page=1, limit=9, filters=[], to_model=False):
    schedule = find_schedule_db_by_id(id=schedule_id, to_model=True)
    if schedule is None:
        raise_error(msg="schedule not found")
    return get_log_book_db_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)


def update_log_book_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)


def insert_log_book_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)


def insert_log_book_db_by_schedule_id(schedule_id=0, json_object={}, bukti_start=None, bukti_end=None):
    log_book = repositoriesDB.find_by_schedule_id_and_user_id(schedule_id=schedule_id, user_id=json_object['user_id'])
    user_name = find_by_id(id=json_object['user_id'])
    # if log_book is not None:
    #     raise raise_error("log book not found")
    if bukti_start is None or bukti_end is None:
        raise raise_error('File not found')
    # Handle bukti_start file
    temp_file_start = str(uuid.uuid4()) + bukti_start.filename.replace(" ", "")
    with open(LOG_BOOK_FOLDER + temp_file_start, "wb") as f:
        f.write(bukti_start.file.read())
    json_object["bukti_start"] = DOMAIN_FILE_URL + '/files/' + temp_file_start
    # Handle bukti_end file
    temp_file_end = str(uuid.uuid4()) + bukti_end.filename.replace(" ", "")
    with open(LOG_BOOK_FOLDER + temp_file_end, "wb") as f:
        f.write(bukti_end.file.read())
    json_object["bukti_end"] = DOMAIN_FILE_URL + '/files/' + temp_file_end
    # data = repositoriesDB.insert(json_object=json_object, to_model=True)
    # json_object['id'] =
    json_object['schedule_id'] = schedule_id
    json_object['user_name'] = user_name.name
    insert_log_book_db(json_object=json_object)
    return True


def delete_log_book_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)


def delete_log_book_by_log_book_id_and_user_id(user_id=0, log_book_id=0):
    return repositoriesDB.delete_by_log_book_id_and_user_id(user_id=user_id, log_book_id=log_book_id)


def find_log_book_by_ids(schedule_id=0, log_book_id=0, user_id=0):
    log_book = find_log_book_db_by_id(id=log_book_id, to_model=True)
    if log_book is None:
        raise_error(msg="Log book not found")
    if log_book.user_id != user_id:
        raise_error('Access denied')
    schedule = find_schedule_db_by_id(id=schedule_id, to_model=True)
    if schedule is None:
        raise_error(msg="Schedule not found")
    return log_book.to_response()


def update_log_book_by_schedule_id(schedule_id=0, id=0, json_object={}, user_id=0, file=None, bukti_start=None,
                                   bukti_end=None):
    log_book = find_log_book_db_by_id(id=id, to_model=True)
    schedule = find_schedule_db_by_id(id=schedule_id, to_model=True)
    if log_book is None:
        raise_error(msg="log book not found")
    if schedule is None:
        raise_error(msg="schedule not found")
    if bukti_start is None or bukti_end is None:
        raise raise_error('File not found')
    # Handle bukti_start file
    temp_file_start = str(uuid.uuid4()) + bukti_start.filename.replace(" ", "")
    with open(LOG_BOOK_FOLDER + temp_file_start, "wb") as f:
        f.write(bukti_start.file.read())
    json_object["bukti_start"] = DOMAIN_FILE_URL + '/files/' + temp_file_start
    # Handle bukti_end file
    temp_file_end = str(uuid.uuid4()) + bukti_end.filename.replace(" ", "")
    with open(LOG_BOOK_FOLDER + temp_file_end, "wb") as f:
        f.write(bukti_end.file.read())
    json_object["bukti_end"] = DOMAIN_FILE_URL + '/files/' + temp_file_end
    json_object["id"] = log_book.id
    json_object["schedule_id"] = schedule_id
    if log_book.user_id != user_id:
        raise_error('Have no access')
    return update_log_book_db(json_object=json_object)


def delete_log_book_by_schedule_id(schedule_id=0, id=0, user_id=0):
    log_book = find_log_book_db_by_id(id=id, to_model=True)
    schedule = find_schedule_db_by_id(id=schedule_id, to_model=True)
    if schedule is None:
        raise_error(msg="Schedule not found")
    if log_book is None:
        raise_error(msg="log book not found")
    delete_log_book = delete_log_book_by_id(id=id)
    if delete_log_book is None:
        raise_error(msg="Failed to delete")
    if log_book.user_id != user_id:
        raise_error('Have no access')
    return True
