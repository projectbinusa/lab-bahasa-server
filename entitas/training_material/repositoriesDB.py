from pony.orm import *

from database.schema import TrainingMaterialDB
from entitas.material.services import find_material_db_by_id


@db_session
def get_all(to_model=True):
    result = []
    try:
        for item in select(s for s in TrainingMaterialDB):
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
    try:
        data_in_db = select(s for s in TrainingMaterialDB).order_by(desc(TrainingMaterialDB.id))
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
        print("error TrainingMaterial getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def find_by_training_id_with_pagination(page=1, limit=9, filters=[], training_id=None, to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in TrainingMaterialDB if s.training_id == training_id).order_by(desc(TrainingMaterialDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.material_id)
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.material_name)
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
    data_in_db = select(s for s in TrainingMaterialDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def find_by_training_id_and_material_id(training_id=0, material_id=0):
    data_in_db = select(s for s in TrainingMaterialDB if s.training_id == training_id and s.material_id == material_id)
    if data_in_db.first() is None:
        return
    return data_in_db.first().to_model()

@db_session
def get_material_ids_by_training_id(training_id=0):
    result = []
    for data_in_db in select(s for s in TrainingMaterialDB if s.training_id == training_id):
        result.append(data_in_db.material_id)
    return result

@db_session
def delete_by_material_id(material_id=0):
    for data_in_db in select(s for s in TrainingMaterialDB if s.material_id == material_id):
        data_in_db.delete()
    commit()
    return True

@db_session
def update_material_name_by_material_id(material_id=0, material_name=''):
    for data_in_db in select(s for s in TrainingMaterialDB if s.material_id == material_id):
        data_in_db.material_name=material_name
    commit()
    return True

@db_session
def update(json_object={}, to_model={}):
    material = find_material_db_by_id(id=json_object['material_id'])
    try:
        updated_training_material = TrainingMaterialDB[json_object["id"]]
        updated_training_material.training_id = json_object["training_id"]
        updated_training_material.material_id = json_object["material_id"]
        updated_training_material.material_name = material['name']
        updated_training_material.is_user_access = json_object["is_user_access"]
        commit()
        if to_model:
            return updated_training_material.to_model()
        else:
            return updated_training_material.to_model().to_response()
    except Exception as e:
        print("error Room update: ", e)
    return None


@db_session
def delete_by_id(id=None):
    try:
        TrainingMaterialDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Room delete: ", e)
    return


@db_session
def insert(json_object={}, to_model=False):
    material = find_material_db_by_id(id=json_object['material_id'])
    try:
        new_training_material = TrainingMaterialDB(
            training_id=json_object["training_id"],
            material_id=json_object["material_id"],
            material_name=json_object['name'],
            is_user_access=json_object["is_user_access"],
        )
        commit()
        if to_model:
            return new_training_material.to_model()
        else:
            return new_training_material.to_model().to_response()
    except Exception as e:
        print("error Room insert: ", e)
    return None

@db_session
def get_materials_by_training_id(training_id=0):
    result = []
    for data_in_db in select(s for s in TrainingMaterialDB if s.training_id == training_id):
        result.append(data_in_db.to_model())
    return result
