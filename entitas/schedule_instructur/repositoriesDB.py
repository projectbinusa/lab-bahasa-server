from pony.orm import *

from database.schema import SchedulerInstructurDB


@db_session
def get_all(to_model=True):
    result = []
    try:
        for item in select(s for s in SchedulerInstructurDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to.response())
    except Exception as e:
        print("error Room getAll: ", e)
    return result


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    # try:
    data_in_db = select(s for s in SchedulerInstructurDB).order_by(desc(SchedulerInstructurDB.id))
    for item in filters:
        if item["field"] == "id":
            data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
        elif item["field"] == "instructur_name":
            data_in_db = data_in_db.filter(lambda d: item["value"] in d.name)
        elif item["field"] == "schedule_id":
            data_in_db = data_in_db.filter(lambda d: d.schedule_id == item["value"])

    total_record = data_in_db.count()
    if limit > 0:
        data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
    for item in data_in_db:
        if to_model:
            result.append(item.to_model())
        else:
            result.append(item.to_model().to_response())

    # except Exception as e:
    #     print("error getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in SchedulerInstructurDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def update(json_object={}, to_model={}):
    try:
        updated_schedule_instructur = SchedulerInstructurDB[json_object["id"]]
        updated_schedule_instructur.schedule_id = json_object = ["schedule_id"]
        updated_schedule_instructur.instructur_id = json_object = ["instructur_id"]
        updated_schedule_instructur.instructur_name = json_object = ["instructur_name"]
        updated_schedule_instructur.is_deteted = json_object = ["is_deteted"]
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
        SchedulerInstructurDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Room delete: ", e)
    return


@db_session
def insert(json_object={}, to_model=False):
    try:
        new_schedule_instructur = SchedulerInstructurDB(
            schedule_id = json_object["schedule_id"],
            instructur_id = json_object["instructur_id"],
            instructur_name = json_object["instructur_name"],
            is_deteted = json_object["is_deteted"],
        )
        commit()
        if to_model:
            return new_schedule_instructur.to_model()
        else:
            return new_schedule_instructur.to_model().to_response()
    except Exception as e:
        print("error Room insert: ", e)
    return None