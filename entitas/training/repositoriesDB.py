from pony.orm import *

from database.schema import TrainingDB

@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in TrainingDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error TrainingDB getAll: ", e)
    return result


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in TrainingDB)
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(id=item['value'])
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.name)
            elif item["field"] == "description":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.description)
            elif item["field"] == "training_ids":
                print('training_ids ',item["value"])
                data_in_db = data_in_db.filter(lambda d: d.id in item["value"])

        data_in_db.order_by(desc(TrainingDB.id))
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
        print("error TrainingDB getAllWithPagination ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in TrainingDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def update(json_object={}, to_model=False):
    try:
        updated_training = TrainingDB[json_object["id"]]
        updated_training.name = json_object["name"]
        updated_training.description = json_object["description"]
        updated_training.image_url = json_object["image_url"]
        commit()
        if to_model:
            return updated_training.to_model()
        else:
            return updated_training.to_model().to_response()
    except Exception as e:
        print("error Training updated: ", e)
        return None


@db_session
def delete_by_id(id=None):
    try:
        TrainingDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("erorr Training deleteById: ", e)
    return


@db_session
def insert(json_object={}, to_model=False):
    try:
        new_training = TrainingDB(
            name=json_object["name"],
            description=json_object["description"],
            image_url=json_object['image_url']
        )
        commit()
        if to_model:
            return new_training.to_model()
        print('fdsss',new_training.to_model().to_response())
        return new_training.to_model().to_response()

    except Exception as e:
        print("error Training insert: ", e)
    return None
