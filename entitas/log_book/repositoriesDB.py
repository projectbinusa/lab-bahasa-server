from pony.orm import *

from database.schema import LogBookDB

@db_session
def get_all(to_model=True):
    result = []
    try:
        for item in select(s for s in LogBookDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to.response())
    except Exception as e:
        print("error Room getAll: ", e)
    return result

@db_session
def get_log_book_ids_by_user_id(user_id=0):
    result = []
    try:
        for item in select(s for s in LogBookDB if s.user_id == user_id and not s.is_deleted):
            result.append(item.schedule_id)
    except Exception as e:
        print("error get_log_book_ids_by_user_id: ", e)
    return result

@db_session
def is_found_user_id_and_log_book_id(user_id=0, schedule_id=0):
    data_in_db = select(s for s in LogBookDB if s.user_id == user_id and s.schedule_id == schedule_id)
    if data_in_db.count() > 0:
        return True
    return False

@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    # try:
    data_in_db = select(s for s in LogBookDB).order_by(desc(LogBookDB.id))
    for item in filters:
        if item["field"] == "id":
            data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
        elif item["field"] == "user_name":
            data_in_db = data_in_db.filter(lambda d: item["value"] in d.user_name)
        elif item["field"] == "schedule_id":
            data_in_db = data_in_db.filter(lambda d: item["value"] == d.schedule_id)
        # elif item["field"] == "instructur_id":
        #     data_in_db = data_in_db.filter(lambda d: d.user_id != item["value"])

    total_record = data_in_db.count()
    if limit > 0:
        data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
    else:
        data_in_db = data_in_db
    for item in data_in_db:
        if to_model:
            result.append(item.to_model())
        else:
            result.append(item.to_model().to_response())

    # except Exception as e:
    #     print("error ScheduleUser getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in LogBookDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def find_by_logg_book_id_and_user_id(schedule_id=None, user_id=0):
    data_in_db = select(s for s in LogBookDB if s.schedule_id == schedule_id and s.user_id == user_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def update(json_object={}, to_model={}):
    try:
        updated_log_book = LogBookDB[json_object["id"]]
        updated_log_book.user_name = json_object["user_name"]
        updated_log_book.user_id = json_object["user_id"]
        updated_log_book.schedule_id = json_object["schedule_id"]
        updated_log_book.periode_date = json_object["periode_date"]
        updated_log_book.periode_start_time = json_object["periode_start_time"]
        updated_log_book.periode_end_time = json_object["periode_end_time"]
        updated_log_book.topic = json_object["topic"]
        updated_log_book.materi = json_object["materi"]
        updated_log_book.training_proof_start = json_object["training_proof_start"]
        updated_log_book.bukti_start = json_object["bukti_start"]
        updated_log_book.bukti_end = json_object["bukti_end"]
        commit()
        if to_model:
            return updated_log_book.to_model()
        else:
            return updated_log_book.to_model().to_response()
    except Exception as e:
        print("error log book update: ", e)
    return None

@db_session
def delete_by_id(id=None):
    try:
        LogBookDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Room delete: ", e)
    return

@db_session
def find_by_schedule_id_and_user_id(schedule_id=None, user_id=0):
    data_in_db = select(s for s in LogBookDB if s.schedule_id == schedule_id and s.user_id == user_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def delete_by_log_book_id_and_user_id(user_id=0, log_book_id=0):
    try:
        for item in select(s for s in LogBookDB if s.log_book_id == log_book_id and s.user_id == user_id):
            item.delete()
        commit()
        return True

    except Exception as e:
        print("error TrainingDB getAll: ", e)
    return

def update_delete_by_id(id=None, is_deleted=False):
    try:
        LogBookDB[id].is_deleted = is_deleted
        commit()
        return True
    except Exception as e:
        print('error log_book delete: ', e)
    return

@db_session
def insert(json_object={}, to_model=False):
    try:
        new_log_book = LogBookDB(
            schedule_id=json_object["schedule_id"],
            periode_date=json_object["periode_date"],
            user_name=json_object["user_name"],
            user_id=json_object["user_id"],
            periode_start_time=json_object["periode_start_time"],
            periode_end_time=json_object["periode_end_time"],
            topic=json_object["topic"],
            materi=json_object["materi"],
            training_proof_start=json_object["training_proof_start"],
            bukti_start=json_object["bukti_start"],
            bukti_end=json_object["bukti_end"]
        )
        commit()
        if to_model:
            return new_log_book.to_model()
        else:
            return new_log_book.to_model().to_response()
    except Exception as e:
        print("error log book insert: ", e)
    return None