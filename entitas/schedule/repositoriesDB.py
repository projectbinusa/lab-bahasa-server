from pony.orm import *
from database.schema import ScheduleDB, TrainingDB

@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in ScheduleDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error Schedule getAll ", e)
    return result

@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in ScheduleDB).order_by(desc(ScheduleDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(id=item["value"])
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda  d: d.name == item["name"])

        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            if to_model:
                result.append(item.to_model.to_response())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error Schedule getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in ScheduleDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def update(json_obejct={}, to_model=False):
    try:
        updated_schedule = ScheduleDB[json_obejct["id"]]
        updated_schedule.name = json_obejct["name"]
        updated_schedule.training_id = json_obejct["training_id"]
        updated_schedule.is_online = json_obejct["is_online"]
        updated_schedule.link = json_obejct["link"]
        updated_schedule.location = json_obejct["location"]
        updated_schedule.start_date = json_obejct["start_date"]
        commit()
        if to_model:
            return updated_schedule.to_model()
        else:
            return updated_schedule.to_model().to_response()

    except Exception as e:
        print("error Schedule update: ", e)
    return None

@db_session
def delete_by_id(id=None):
    try:
        ScheduleDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Schedule deleteById: ", e)
    return

@db_session
def insert(json_object={}, to_model=False):
    try:
        training = TrainingDB[json_object["training_id"]]
        new_schedule = ScheduleDB(
            name = json_object["name"],
            training_id = training,
            link = json_object["link"],
            is_online = json_object["is_online"],
            location = json_object["location"],
            start_date = json_object["start_date"],
        )
        commit()
        if to_model:
            return new_schedule.to_model()
        else:
            return new_schedule.to_model().to_response()
    except Exception as e :
        print("error Schedule insert: ", e)
    return None