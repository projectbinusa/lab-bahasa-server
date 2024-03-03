from pony.orm import *
from database.schema import  AbsentDB

@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in AbsentDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())
    except Exception as e:
        print("error Absent getAll: ", e)
    return result

@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False ):
    result = []
    total_record = 0
    try:
        data_in_db = select (s for s in AbsentDB).order_by(desc(AbsentDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(id=item["value"])
            elif item["field"] == "user_name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.user_name)
            elif item["field"] == "training_name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.training_name)
            elif item["field"] == "schedule_id":
                data_in_db = data_in_db.filter(schedule_id=item["value"])
            elif item["field"] == "training_id":
                data_in_db = data_in_db.filter(training_id=item["value"])

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

    except Exception as e:
        print("error Absen getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in AbsentDB if s.id == id)
    if data_in_db.first() is None:
        return  None
    return data_in_db.first().to_model()

@db_session
def update(json_object={}, to_model=[]):
    try:
        updated_absent = AbsentDB[json_object["id"]]
        updated_absent.training_id = json_object["training_id"]
        updated_absent.training_name = json_object["training_name"]
        updated_absent.schedule_id = json_object["schedule_id"]
        updated_absent.absent_date = json_object["absent_date"]
        updated_absent.user_id = json_object["user_id"]
        updated_absent.user_name = json_object["user_name"]
        updated_absent.status = json_object["status"]
        updated_absent.description = json_object["description"]
        commit()
        if to_model:
            return updated_absent.to_model()
        else:
            return updated_absent.to_model().to_response()

    except Exception as e:
        print("error Absent update: ", e)
    return None

@db_session
def delete_by_id(id=None):
    try:
        AbsentDB[id].delet()
        commit()
        return None
    except Exception as e:
        print("error Absent deleteById: ", e)
    return

@db_session
def insert(json_object={}, to_model=[]):
    try:
        new_absent = AbsentDB(
            training_id = json_object["training_id"],
            training_name = json_object["training_name"],
            schedule_id = json_object["schedule_id"],
            absent_date = json_object["absent_date"],
            status = json_object["status"],
            user_id = json_object["user_id"],
            user_name = json_object["user_name"],
            description = json_object["description"],
        )
        commit()
        if to_model:
            return new_absent.to_model()
        else:
            return new_absent.to_model().to_response()
    except Exception as e:
        print("error Absent insert: ", e)
    return None












