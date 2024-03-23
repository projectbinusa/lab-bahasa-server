from pony.orm import *

from database.schema import ScheduleInstructurDB


@db_session
def get_all(to_model=True):
    result = []
    try:
        for item in select(s for s in ScheduleInstructurDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to.response())
    except Exception as e:
        print("error Room getAll: ", e)
    return result


@db_session
def get_all_with_pagination(
        page=1,
        limit=9,
        to_model=False,
        filters=[],
        to_response="to_response"
):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in ScheduleInstructurDB)
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
            elif item["field"] == "instructur_name":
                data_in_db = data_in_db.filter(instructur_id=item["value"])
            elif item["field"] == "schedule_id":
                data_in_db = data_in_db.filter(schedule_id=item["value"])
            elif item["field"] == "is_deleted":
                data_in_db = data_in_db.filter(is_deleted=item["value"])

        total_record = count(data_in_db)
        if limit != 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                if to_response == "to_response_profile":
                    result.append(item.to_model().to_response_profile())
                else:
                    result.append(item.to_model().to_response())
    except Exception as e:
        print("error Schedule Instructur getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def get_schedule_instructur_by_schedule_id(schedule_id, page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in ScheduleInstructurDB if s.schedule_id == schedule_id).order_by(
            desc(ScheduleInstructurDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.name)

        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_model())

    except Exception as e:
        print("error getScheduleInstructurByScheduleId: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in ScheduleInstructurDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def update(json_object={}, to_model={}):
    try:
        updated_schedule_instructur = ScheduleInstructurDB[json_object["id"]]
        updated_schedule_instructur.schedule_id = json_object["schedule_id"]
        updated_schedule_instructur.instructur_id = json_object["instructur_id"]
        updated_schedule_instructur.instructur_name = json_object["instructur_name"]
        updated_schedule_instructur.is_deleted = json_object["is_deleted"]
        commit()
        if to_model:
            return updated_schedule_instructur.to_model()
        else:
            return updated_schedule_instructur.to_model().to_response()
    except Exception as e:
        print("error Room update: ", e)
    return None


@db_session
def delete_by_id(id=None):
    try:
        ScheduleInstructurDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Room delete: ", e)
    return


@db_session
def insert(json_object={}, to_model=False):
    try:
        new_schedule_instructur = ScheduleInstructurDB(
            schedule_id=json_object["schedule_id"],
            instructur_id=json_object["instructur_id"],
            instructur_name=json_object["instructur_name"],
            # is_deleted = json_object["is_deleted"],
        )
        commit()
        if to_model:
            return new_schedule_instructur.to_model()
        else:
            return new_schedule_instructur.to_model().to_response()
    except Exception as e:
        print("error Room insert: ", e)
    return None


@db_session
def update_by_schedule_id(schedule_id, json_object={}, to_model=False):
    try:
        updated_schedule_instructur = ScheduleInstructurDB[schedule_id, json_object["id"]]
        updated_schedule_instructur.schedule_id = json_object["schedule_id"]
        updated_schedule_instructur.instructur_id = json_object["instructur_id"]
        updated_schedule_instructur.instructur_name = json_object["instructur_name"]
        updated_schedule_instructur.is_deleted = json_object.get("is_deleted", False)
        commit()
        if to_model:
            return updated_schedule_instructur.to_model()
        else:
            return updated_schedule_instructur.to_model().to_response()
    except Exception as e:
        print("error ScheduleInstructur update: ", e)
        return None


@db_session
def delete_by_schedule_id(schedule_id, instructur_id):
    try:
        schedule_instructur = ScheduleInstructurDB[schedule_id, instructur_id]
        schedule_instructur.delete()
        commit()
        return True
    except Exception as e:
        print("error ScheduleInstructur delete: ", e)
        return False


@db_session
def find_by_schedule_id(schedule_id, instructur_id):
    try:
        schedule_instructur = ScheduleInstructurDB[schedule_id, instructur_id]
        return schedule_instructur.to_model()
    except Exception as e:
        print("error ScheduleInstructur find by id: ", e)
        return None


@db_session
def insert_schedule_instructur_by_schedule_id(schedule_id, json_object={}, to_model=False):
    try:
        new_schedule_instructur = ScheduleInstructurDB(
            schedule_id=schedule_id,
            instructur_id=json_object["instructur_id"],
            instructur_name=json_object["instructur_name"],
            is_deleted=json_object.get("is_deleted", False),
        )
        commit()
        if to_model:
            return new_schedule_instructur.to_model()
        else:
            return new_schedule_instructur.to_model().to_response()
    except Exception as e:
        print("error ScheduleInstructur insert: ", e)
        return None
