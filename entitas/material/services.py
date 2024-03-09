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


def update_material_db(json_object={}, file=None):
    if file is None:
        raise_error('File not found')
    temp_file = str(uuid.uuid4()) + file.filename.replace(" ", "")
    json_object["filename"] = temp_file
    with open(MATERIAL_FOLDER+temp_file, "wb") as f:
        f.write(file.file.read())
    json_object["url_file"] = DOMAIN_FILE_URL + '/files/' + json_object["filename"]
    return repositoriesDB.update(json_object=json_object)

def insert_material_db(json_object={}, file=None):


    if file is None:
        raise_error('File not found')
    temp_file = str(uuid.uuid4()) + file.filename.replace(" ", "")
    json_object["filename"] = temp_file
    with open(MATERIAL_FOLDER+temp_file, "wb") as f:
        f.write(file.file.read())
    json_object["url_file"] = DOMAIN_FILE_URL + '/files/' + json_object["filename"]
    # os.remove(MATERIAL_FOLDER+temp_file)
    return repositoriesDB.insert(json_object=json_object)


def delete_material_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

