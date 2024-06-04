from pony.orm import *

from database.schema import LoginLimitsDB, KelasUserDB
from util.other_util import raise_error


@db_session
def get_all(to_model=True):
    result = []
    try:
        for item in select(s for s in LoginLimitsDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to.response())
    except Exception as e:
        print("error Room getAll: ", e)
    return result

@db_session
def get_login_limits_ids_by_class_id(class_id=0):
    result = []
    try:
        for item in select(s for s in LoginLimitsDB if s.class_id == class_id):
            result.append(item.schedule_id)
    except Exception as e:
        print("error get_login_limits_ids_by_class_id: ", e)
    return result

# @db_session
# def is_found_class_id_and_login_limits_id(class_id=0, schedule_id=0):
#     data_in_db = select(s for s in LoginLimitsDB if s.class_id == class_id and s.schedule_id == schedule_id)
#     if data_in_db.count() > 0:
#         return True
#     return False

@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    # try:
    class_id = next((x["value"] for x in filters if x.get("field") == "class_id"), 0)
    data_in_db = select((s) for s in LoginLimitsDB if s.class_id == class_id)
    for item in filters:
        if item["field"] == "id":
            data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
        elif item["field"] == "class_id":
            data_in_db = data_in_db.filter(lambda d: item["value"] == d.class_id)
        # elif item["field"] == "instructur_id":
        #     data_in_db = data_in_db.filter(lambda d: d.class_id != item["value"])

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
    data_in_db = select(s for s in LoginLimitsDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def find_by_login_limits_id_and_class_id(class_id=0, id=0):
    data_in_db = select(s for s in LoginLimitsDB if s.id == id and s.class_id == class_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


# @db_session
# def update_class_login_limit(limit_id, start_time):
#     limit = LoginLimitsDB.get(id=limit_id)
#     if limit is None:
#         raise raise_error("Class login limit not found")
#     limit.start_time = start_time
#     commit()
#     return limit.to_model()

@db_session
def update(json_object={}, to_model={}):
    # limit =
    try:
        updated_login_limits = LoginLimitsDB[json_object["id"]]
        updated_login_limits.class_id = json_object["class_id"]
        updated_login_limits.end_time = json_object["end_time"]
        commit()
        if to_model:
            return updated_login_limits.to_model()
        else:
            return updated_login_limits.to_model().to_response()
    except Exception as e:
        print("error login limits update: ", e)
    return None

@db_session
def delete_by_id(id=None):
    try:
        LoginLimitsDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Room delete: ", e)
    return

# @db_session
# def find_by_schedule_id_and_class_id(schedule_id=None, class_id=0):
#     data_in_db = select(s for s in LoginLimitsDB if s.schedule_id == schedule_id and s.class_id == class_id)
#     if data_in_db.first() is None:
#         return None
#     return data_in_db.first().to_model()

# @db_session
# def delete_by_login_limits_id_and_class_id(class_id=0, login_limits_id=0):
#     try:
#         for item in select(s for s in LoginLimitsDB if s.login_limits_id == login_limits_id and s.class_id == class_id):
#             item.delete()
#         commit()
#         return True
#
#     except Exception as e:
#         print("error TrainingDB getAll: ", e)
#     return

@db_session
def update_delete_by_id(id=None, is_deleted=False):
    try:
        LoginLimitsDB[id].is_deleted = is_deleted
        commit()
        return True
    except Exception as e:
        print('error login_limits delete: ', e)
    return



@db_session
def insert(json_object={}, to_model=False):
    try:
        new_login_limits = LoginLimitsDB(
            class_id=json_object['class_id'],
            end_time=json_object['end_time'],
        )
        commit()
        if to_model:
            return new_login_limits.to_model()
        else:
            return new_login_limits.to_model().to_response()
    except Exception as e:
        print("error login limits insert: ", e)
    return None