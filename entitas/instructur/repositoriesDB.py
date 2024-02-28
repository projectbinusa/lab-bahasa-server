from pony.orm import *
from database.schema import InstructurDB


@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in InstructurDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error MaterialDB getAll: ", e)
    return result

@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_id_db = select(s for s in InstructurDB).order_by(desc(InstructurDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_id_db.filter(id=item["value"])
            elif item["field"] == "name":
                data_in_db = data_id_db.filter(lambda d: d.name == item["value"])

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
        print("error instructur getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in InstructurDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def update(json_object={}, to_model=False):
    try:
        updated_instructur = InstructurDB[json_object["id"]]
        updated_instructur.name = json_object["name"]
        updated_instructur.email = json_object["email"]
        updated_instructur.address = json_object["address"]
        updated_instructur.birth_date = json_object["birth_date"]
        updated_instructur.birth_place = json_object["birth_place"]
        updated_instructur.avatar_url = json_object["avatar_url"]
        updated_instructur.is_faciliator = json_object["is_faciliator"]
        commit()
        if to_model:
            return updated_instructur.to_model()
        else:
            return updated_instructur.to_model().to_response()

    except Exception as e:
        print("error Intstuctur update:", e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        InstructurDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Traininf deletedById: ", e)
    return

@db_session
def insert(json_object={}, to_model=False):
    try:
        new_instructur = InstructurDB(
            name=json_object["name"],
            email=json_object["email"],
            address=json_object["address"],
            birth_date=json_object["birth_date"],
            birth_place=json_object["birth_place"],
            avatar_url=json_object["avatar_url"],
            is_faciliator=json_object["is_faciliator"],
        )
        commit()
        if to_model:
            return new_instructur.to_model()
        else:
            return new_instructur.to_model().to_response()
    except Exception as e:
        print("error Training insert: ", e)
        return None