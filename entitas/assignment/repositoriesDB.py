from pony.orm import *

from database.schema import AssignmentDB, TrainingDB, InstructurDB


@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in AssignmentDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error AssignmentDB getAll: ", e)
    return result


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in AssignmentDB).order_by(desc(AssignmentDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.name)
            elif item["field"] == "schedule_id":
                data_in_db = data_in_db.filter(lambda d: item["value"] == d.schedule_id)
            elif item["field"] == "instructur_id":
                data_in_db = data_in_db.filter(lambda d: item["value"] == d.instructur_id)

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
        print("error AssignmentDB getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def find_by_schedule_id_with_pagination(page=1, limit=9, filters=[], schedule_id=None, to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in AssignmentDB if s.schedule_id == schedule_id).order_by(desc(AssignmentDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.name)
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
        print("error TrainingMaterialByTrainingId getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in AssignmentDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def update(json_object={}, to_model=False):
    try:
        updated_assignment = AssignmentDB[json_object["id"]]
        # updated_assignment.schedule_id = json_object["schedule_id"]
        # updated_assignment.instructur_id = json_object["instructur_id"]
        updated_assignment.name = json_object["name"]
        updated_assignment.description = json_object["description"]
        updated_assignment.max_date = json_object["max_date"]
        commit()
        if to_model:
            return updated_assignment.to_model()
        else:
            return updated_assignment.to_model().to_response()
    except Exception as e:
        print("error Material update: ", e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        AssignmentDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Material deleteById: ", e)
    return


@db_session
def insert(json_object={}, to_model=False):
    try:
        new_assignment = AssignmentDB(
            schedule_id=json_object['schedule_id'],
            training_id=json_object["training_id"],
            instructur_id=json_object["instructur_id"],
            name=json_object["name"],
            description=json_object["description"],
            max_date=json_object["max_date"],
        )
        commit()
        if to_model:
            return new_assignment.to_model()
        else:
            return new_assignment.to_model().to_response()
    except Exception as e:
        print("error Material insert: ", e)
        return None
