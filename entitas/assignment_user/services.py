from entitas.assignment_user import repositoriesDB
from util.other_util import raise_error
from config.config import ASSIGNMENT_FOLDER, DOMAIN_FILE_URL
import uuid

def get_assignment_user_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_assignment_user_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


def update_assignment_user_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)

def insert_assignment_user_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)


def delete_assignment_user_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

def find_assignment_user_by_id(assignment_id=0, user_id=0):
    from entitas.assignment.services import find_assignment_db_by_id
    assignment = find_assignment_db_by_id(id=assignment_id, to_model=True)
    if assignment is None:
        raise_error('assignment not found')
    assignment_user = repositoriesDB.find_by_assignment_id_and_user_id(assignment_id=assignment_id, user_id=user_id)
    if assignment_user is None:
        return {}
    return assignment_user.to_response()

def update_assignment_user(file=None, assignment_id=0, user_id=0, json_object={}):
    from entitas.assignment.services import find_assignment_db_by_id
    if file is None:
        raise_error('File not found')

    assignment = find_assignment_db_by_id(id=assignment_id, to_model=True)
    if assignment is None:
        raise_error('assignment not found')
    temp_file = str(uuid.uuid4()) + file.filename.replace(" ", "")
    json_object["filename"] = temp_file
    with open(ASSIGNMENT_FOLDER + temp_file, "wb") as f:
        f.write(file.file.read())
    json_object['instructur_id'] = assignment.instructur_id
    json_object['training_id'] = assignment.training_id
    json_object['user_id'] = user_id
    json_object["url_file"] = DOMAIN_FILE_URL + '/files/' + json_object["filename"]
    assignment_user = repositoriesDB.find_by_assignment_id_and_user_id(assignment_id=assignment_id, user_id=user_id)
    if assignment_user is None:
        return repositoriesDB.insert(json_object=json_object)
    json_object['id'] = assignment_user.id
    return repositoriesDB.update(json_object=json_object)
