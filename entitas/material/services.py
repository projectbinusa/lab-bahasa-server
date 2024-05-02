from entitas.material import repositoriesDB
from util.other_util import raise_error
import os, uuid
from config.config import MATERIAL_FOLDER, DOMAIN_FILE_URL

def get_material_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_material_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()

def find_material_for_instructur_by_id(id=0, training_id=0, user_id=0, to_model=False):
    from entitas.schedule_user.services import get_schedule_ids_by_user_id
    from entitas.schedule.services import get_training_ids_by_schedule_ids
    from entitas.training_material.services import find_training_material_by_training_id_and_material_id
    schedule_ids = get_schedule_ids_by_user_id(user_id=user_id)
    training_ids = get_training_ids_by_schedule_ids(schedule_ids=schedule_ids)
    if training_id not in training_ids:
        raise_error("have no access")
    material = repositoriesDB.find_by_id(id=id)
    if material is None:
        return
    training_material = find_training_material_by_training_id_and_material_id(training_id=training_id, material_id=id)
    if training_material is None:
        raise_error("have no access")
    return material.to_response()

def update_material_for_instructur(json_object={}, file=None, training_id=0, user_id=0):
    if file is None:
        raise_error('File not found')
    from entitas.schedule_user.services import get_schedule_ids_by_user_id
    from entitas.schedule.services import get_training_ids_by_schedule_ids
    from entitas.training_material.services import find_training_material_by_training_id_and_material_id, update_training_materia_for_material_name_by_material_id
    schedule_ids = get_schedule_ids_by_user_id(user_id=user_id)
    training_ids = get_training_ids_by_schedule_ids(schedule_ids=schedule_ids)
    # print('user_id ',user_id ,' schedule_ids ',schedule_ids ,' training_ids',training_ids, 'training_id ',training_id)
    if training_id not in training_ids:
        raise_error("have no access")
    training_material = find_training_material_by_training_id_and_material_id(training_id=training_id,
                                                                              material_id=json_object['id'])
    if training_material is None:
        raise_error("have no access")

    material = repositoriesDB.find_by_id(id=json_object['id'])
    if material is None:
        raise_error("Material not found")
    temp_file = str(uuid.uuid4()) + file.filename.replace(" ", "")
    json_object["filename"] = temp_file
    with open(MATERIAL_FOLDER+temp_file, "wb") as f:
        f.write(file.file.read())
    json_object["url_file"] = DOMAIN_FILE_URL + '/files/' + json_object["filename"]
    repositoriesDB.update(json_object=json_object)
    update_training_materia_for_material_name_by_material_id(material_id=json_object['id'],
                                                             material_name=json_object['name'])
    return True

def delete_material_for_instructur_by_id(id=0, training_id=0, user_id=0):
    from entitas.schedule_user.services import get_schedule_ids_by_user_id
    from entitas.schedule.services import get_training_ids_by_schedule_ids
    from entitas.training_material.services import find_training_material_by_training_id_and_material_id
    from entitas.training_material.services import delete_training_material_by_material_id
    schedule_ids = get_schedule_ids_by_user_id(user_id=user_id)
    training_ids = get_training_ids_by_schedule_ids(schedule_ids=schedule_ids)
    # print('user_id ',user_id ,' schedule_ids ',schedule_ids ,' training_ids',training_ids, 'training_id ',training_id)
    if training_id not in training_ids:
        raise_error("have no access")

    material = repositoriesDB.find_by_id(id=id)
    if material is None:
        raise_error("Material not found")
    training_material = find_training_material_by_training_id_and_material_id(training_id=training_id,
                                                                              material_id=id)
    if training_material is None:
        raise_error("have no access")

    delete_training_material_by_material_id(material_id=id)
    return repositoriesDB.delete_by_id(id=id)

def get_material_by_training_id_for_instructur(page=1, limit=9, filters=[], training_id=0, user_id=0, to_model=False):
    from entitas.schedule_user.services import get_schedule_ids_by_user_id
    from entitas.schedule.services import get_training_ids_by_schedule_ids
    from entitas.training_material.services import get_material_ids_by_training_id
    schedule_ids = get_schedule_ids_by_user_id(user_id=user_id)
    training_ids = get_training_ids_by_schedule_ids(schedule_ids=schedule_ids)
    # print('user_id ',user_id ,' schedule_ids ',schedule_ids ,' training_ids',training_ids, 'training_id ',training_id)
    if training_id not in training_ids:
        raise_error("have no access")
    material_ids = get_material_ids_by_training_id(training_id=training_id)
    filters.append({'field': 'ids', 'value': material_ids})
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )
def update_material_db(json_object={}, file=None):
    if not json_object.get("other_link"):
        if file is None:
            raise_error('File not found')
        temp_file = str(uuid.uuid4()) + file.filename.replace(" ", "")
        json_object["filename"] = temp_file
        with open(MATERIAL_FOLDER+temp_file, "wb") as f:
            f.write(file.file.read())
        json_object["url_file"] = DOMAIN_FILE_URL + '/files/' + json_object["filename"]
    else:
        json_object["filename"] = json_object["other_link"]
        json_object["url_file"] = ""
    return repositoriesDB.update(json_object=json_object)

def insert_material_db(json_object={}, file=None):
    if not json_object.get("other_link"):
        if file in [None, "", "null"]:
            raise_error('File not found')
        temp_file = str(uuid.uuid4()) + file.filename.replace(" ", "")
        json_object["filename"] = temp_file
        with open(MATERIAL_FOLDER+temp_file, "wb") as f:
            f.write(file.file.read())
        json_object["url_file"] = DOMAIN_FILE_URL + '/files/' + json_object["filename"]
    else:
        json_object["filename"] = json_object["other_link"]
        json_object["url_file"] = ""
    return repositoriesDB.insert(json_object=json_object)

def insert_material_by_instructur(json_object={}, file=None, training_id=0):
    from entitas.training_material.services import insert_training_material_db
    if file is None:
        raise_error('File not found')
    temp_file = str(uuid.uuid4()) + file.filename.replace(" ", "")
    json_object["filename"] = temp_file
    with open(MATERIAL_FOLDER+temp_file, "wb") as f:
        f.write(file.file.read())
    json_object["url_file"] = DOMAIN_FILE_URL + '/files/' + json_object["filename"]
    data = repositoriesDB.insert(json_object=json_object, to_model=True)
    json_object['material_id'] = data.id
    json_object['training_id'] = int(training_id)
    json_object['is_user_access'] = True
    insert_training_material_db(json_object=json_object)
    return True
def delete_material_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

