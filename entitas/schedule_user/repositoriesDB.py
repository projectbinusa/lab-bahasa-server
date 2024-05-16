from pony.orm import *

from database.schema import ScheduleUserDB, ScheduleInstructurDB


@db_session
def get_all(to_model=True):
    result = []
    try:
        for item in select(s for s in ScheduleUserDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to.response())
    except Exception as e:
        print("error Room getAll: ", e)
    return result

@db_session
def get_schedule_ids_by_instructur_id(user_id=0):
    result = []
    try:
        for item in select(s for s in ScheduleInstructurDB if s.user_id == user_id and not s.is_deleted):
            result.append(item.schedule_id)
    except Exception as e:
        print("error get_schedule_ids_by_user_id: ", e)
    return result

@db_session
def get_schedule_ids_by_user_id(user_id=0):
    result = []
    try:
        for item in select(s for s in ScheduleUserDB if s.user_id == user_id and not s.is_deleted):
            result.append(item.schedule_id)
    except Exception as e:
        print("error get_schedule_ids_by_user_id: ", e)
    return result

@db_session
def is_found_user_id_and_schedule_id(user_id=0, schedule_id=0):
    data_in_db = select(s for s in ScheduleUserDB if s.user_id == user_id and s.schedule_id == schedule_id)
    if data_in_db.count() > 0:
        return True
    return False

@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    from database.schema import UserDB
    result = []
    total_record = 0
    # try:
    data_in_db = select(s for s in ScheduleUserDB).order_by(desc(ScheduleUserDB.id))
    # data_in_db = select((s, u) for s in ScheduleUserDB for u in UserDB if s.id == id and s.user_id == u.id)
    for item in filters:
        if item["field"] == "id":
            data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
        elif item["field"] == "name":
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
            result.append(item.to_model().to_response_participant())

    # except Exception as e:
    #     print("error ScheduleUser getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def get_user_and_schedule_user_with_pagination(page=1, limit=9, filters=[], to_model=False):
    from database.schema import UserDB
    result = []
    total_record = 0
    # try:
    # data_in_db = select(s for s in ScheduleUserDB).order_by(desc(ScheduleUserDB.id))
    schedule_id = next((x["value"] for x in filters if x.get("field") == "schedule_id"), 0)
    data_in_db = select((s, u) for s in ScheduleUserDB for u in UserDB if s.schedule_id == schedule_id and s.user_id == u.id)
    for item in filters:
        if item["field"] == "id":
            data_in_db = data_in_db.filter(lambda d, i: item["value"] in d.id)
        elif item["field"] == "name":
            data_in_db = data_in_db.filter(lambda d, i: item["value"] in d.user_name)
        elif item["field"] == "schedule_id":
            data_in_db = data_in_db.filter(lambda d, i: item["value"] == d.schedule_id)
        elif item["field"] == "confirmed":
            data_in_db = data_in_db.filter(lambda d, i: item["value"] == d.confirmed)

    total_record = data_in_db.count()
    if limit > 0:
        data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
    else:
        data_in_db = data_in_db
    for item, user in data_in_db:
        # if to_model:
        #     result.append(item.to_model())
        # else:
        data = item.to_model().to_response_participant()
        data['user_profile'] = user.to_model().to_response_participant_schedule()
        result.append(data)


    # except Exception as e:
    #     print("error ScheduleUser getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in ScheduleUserDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def find_by_schedule_id_and_user_id(schedule_id=None, user_id=0):
    data_in_db = select(s for s in ScheduleUserDB if s.schedule_id == schedule_id and s.user_id == user_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def update_score(id=0, score=0):
    for item in select(s for s in ScheduleUserDB if s.id == id):
        item.score = score
    commit()
    return True

@db_session
def update_feedback(id=0, kritik='', saran=''):
    for item in select(s for s in ScheduleUserDB if s.id == id):
        item.kritik = kritik
        item.saran = saran
    commit()
    return True

@db_session
def update_confirmed(id=0, confirmed=False):
    for item in select(s for s in ScheduleUserDB if s.id == id):
        item.confirmed = confirmed
    commit()
    return True

@db_session
def update(json_object={}, to_model={}):
    try:
        updated_schedule_user = ScheduleUserDB[json_object["id"]]
        updated_schedule_user.instructur_id = json_object["instructur_id"]
        updated_schedule_user.schedule_id = json_object["schedule_id"]
        updated_schedule_user.instructur_name = json_object["instructur_name"]
        updated_schedule_user.score = json_object["score"]
        commit()
        if to_model:
            print(updated_schedule_user.to_model())
            return updated_schedule_user.to_model()
        else:
            print(updated_schedule_user.to_model().to_response())
            return updated_schedule_user.to_model().to_response()
    except Exception as e:
        print("error Room update: ", e)
    return None

@db_session
def update_score(id=0, score=0):
    try:
        updated_schedule_user = ScheduleUserDB[id]
        updated_schedule_user.score = score
        commit()
        return True
    except Exception as e:
        print("error ScheduleUser update_score: ", e)
    return

@db_session
def update_absent(schedule_id=0, user_id=0, json_object={}, to_model=False):
    try:
        updated_schedule_user = ScheduleUserDB[user_id]
        updated_schedule_user.in_absent = json_object["in_absent"]
        updated_schedule_user.out_absent = json_object["out_absent"]
        commit()
        if to_model:
            return updated_schedule_user.to_model()
        else:
            print(updated_schedule_user.in_absent)
            print(updated_schedule_user.out_absent)
            return updated_schedule_user.to_model().to_response()
    except Exception as e:
        print("error ScheduleUser update_absent: ", e)
        return None

@db_session
def get_score_by_id_schedule(schedule_id=None, schedule_user_id=None):
    data_in_db = select(s for s in ScheduleUserDB if s.id == schedule_user_id and s.schedule_id == schedule_id)
    return data_in_db.first().to_model().to_response()

@db_session
def update_certificate(id=0, certificate_url=''):
    try:
        updated_schedule_user = ScheduleUserDB[id]
        updated_schedule_user.certificate_url = certificate_url
        commit()
        return True
    except Exception as e:
        print("error ScheduleUser update_score: ", e)
    return


@db_session
def delete_by_id(id=None):
    try:
        ScheduleUserDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Room delete: ", e)
    return

def update_delete_by_id(id=None, is_deleted=False):
    try:
        ScheduleUserDB[id].is_deleted = is_deleted
        commit()
        return True
    except Exception as e:
        print('error schedule_user delete: ', e)
    return

@db_session
def insert(json_object={}, to_model=False):
    try:
        new_schedule_user = ScheduleUserDB(
            user_id=json_object["user_id"],
            schedule_id=json_object["schedule_id"],
            user_name=json_object["user_name"]
            # is_deleted = json_object["is_deleted"],
        )
        commit()
        if to_model:
            return new_schedule_user.to_model()
        else:
            return new_schedule_user.to_model().to_response()
    except Exception as e:
        print("error Room insert: ", e)
    return None