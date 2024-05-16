from entitas.absent import repositoriesDB
from util.other_util import raise_error
import datetime
import uuid
from config.config import SIGNATURE_FOLDER, DOMAIN_FILE_URL

def get_absent_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )

def get_all_absent_by_user_id(user_id=0, to_model=False):
    return repositoriesDB.get_all_by_user_id(user_id=user_id, to_model=to_model)

def find_absent_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()

def update_absent_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)

def upload_signature_user(file=None, user_id=0):
    if file is None:
        raise_error('File not found')
    temp_file = 'sign' + str(user_id) + '_'+ str(uuid.uuid4()) + file.filename.replace(" ", "")
    json_object = {}
    json_object["filename"] = temp_file
    with open(SIGNATURE_FOLDER + json_object['filename'], "wb") as f:
        f.write(file.file.read())
    json_object['user_id'] = user_id
    json_object["url_file"] = DOMAIN_FILE_URL + '/files/' + json_object["filename"]
    return json_object

def insert_absent_db(json_object={}):
    from entitas.schedule.services import find_schedule_db_by_id
    from entitas.user.services import find_user_db_by_id
    from entitas.schedule_user.services import update_schedule_user_by_schedule_id
    schedule = find_schedule_db_by_id(id=json_object['schedule_id'], to_model=True)
    if schedule is None:
        raise_error("schedule not found")
    json_object['training_id'] = schedule.training_id
    json_object['training_name'] = schedule.training_name
    json_object['absent_date'] = datetime.datetime.now()

    user = find_user_db_by_id(id=json_object['user_id'], to_model=True)
    schedule_user = {}
    if user is None:
        raise_error("user not found")
    json_object['user_name'] = user.name
    if 'signature' not in json_object:
        json_object['signature'] = ''
    schedule_user['in_absent'] = json_object['in_absent']
    schedule_user['out_absent'] = json_object['out_absent']

    repositoriesDB.insert(json_object=json_object)
    update_schedule_user_by_schedule_id(schedule_id=schedule.id, user_id=user.id, json_object=schedule_user)

    return True


def delete_absent_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)