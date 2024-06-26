from entitas.schedule_user import repositoriesDB
from entitas.schedule_user.repositoriesDB import get_user_and_schedule_user_with_pagination
from util.other_util import raise_error
from entitas.schedule.services import find_schedule_db_by_id
from entitas.user.repositoriesDB import find_by_id
from threading import Thread
from util.image_util import ImageUtil
def get_schedule_user_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_schedule_user_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    from entitas.schedule.services import find_schedule_db_by_id
    from entitas.schedule_instructur.services import get_user_ids_by_schedule_id
    from entitas.user.services import find_user_db_by_id
    from entitas.assignment.services import get_assignment_db_with_pagination
    result = result.to_response()
    result['schedule'] = find_schedule_db_by_id(id=result['schedule_id'])
    result['instructur'] = None
    result['assignment'], _ = get_assignment_db_with_pagination(
        filters=[{'field': 'schedule_id', 'value': result['schedule_id']}])
    for user_id in get_user_ids_by_schedule_id(schedule_id=result['schedule_id']):
        user = find_user_db_by_id(id=user_id, to_model=True)
        if user is None:
            continue
        if user.role == 'instructur':
            result['instructur'] = user.to_response_simple()
    from entitas.training_material.services import get_materials_by_training_id
    result['materials'] = []
    if result['schedule'] is not None:
        result['materials'] = get_materials_by_training_id(training_id=result['schedule']['training_id'])
    return result


def find_schedule_user_for_student_by_id(schedule_id=0, user_id=0, to_model=False):
    result = repositoriesDB.find_by_schedule_id_and_user_id(schedule_id=schedule_id, user_id=user_id)
    if result is None:
        raise_error('data not found')
    if to_model:
        return result
    if result.user_id != user_id:
        raise_error('have no access')
    from entitas.schedule.services import find_schedule_db_by_id
    from entitas.schedule_instructur.services import get_user_ids_by_schedule_id
    from entitas.user.services import find_user_db_by_id
    from entitas.assignment.services import get_assignment_db_with_pagination
    from entitas.assignment_user.services import get_assignment_user_by_id
    result = result.to_response()
    result['schedule'] = find_schedule_db_by_id(id=result['schedule_id'])
    result['instructur'] = None
    result['assignment'], _ = get_assignment_db_with_pagination(
        filters=[{'field': 'schedule_id', 'value': result['schedule_id']}])
    for i in range(len(result['assignment'])):
        result['assignment'][i]['result'] = None
        assignment_user = get_assignment_user_by_id(assignment_id=result['assignment'][i]['id'], user_id=user_id)
        if assignment_user is not None:
            result['assignment'][i]['result'] = assignment_user.to_response_simple()

    for user_id in get_user_ids_by_schedule_id(schedule_id=result['schedule_id']):
        user = find_user_db_by_id(id=user_id, to_model=True)
        if user is None:
            continue
        if user.role == 'instructur':
            result['instructur'] = user.to_response_simple()
    from entitas.training_material.services import get_materials_by_training_id
    result['materials'] = []
    if result['schedule'] is not None:
        result['materials'] = get_materials_by_training_id(training_id=result['schedule']['training_id'])
    return result


def get_schedule_ids_by_user_id(user_id=0):
    return repositoriesDB.get_schedule_ids_by_user_id(user_id=user_id)


def get_schedule_user_by_schedule_id(schedule_id=0, page=1, limit=9, filters=[], to_model=False):
    schedule = find_schedule_db_by_id(id=schedule_id, to_model=True)
    if schedule is None:
        raise_error(msg="schedule not found")
    return get_schedule_user_db_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)

def get_schedule_user_by_schedule_id_user(schedule_id=0, page=1, limit=9, filters=[], to_model=False):
    schedule = find_schedule_db_by_id(id=schedule_id, to_model=True)
    if schedule is None:
        raise_error(msg="schedule not found")
    return get_user_and_schedule_user_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)

def update_schedule_user_db(json_object={}):
    print('ini json objectnya kakak ---------->', json_object)
    return repositoriesDB.update(json_object=json_object)

def update_schedule_user_for_feeback(schedule_id=0, user_id=0, kritik='', saran=''):
    schedule_user = repositoriesDB.find_by_schedule_id_and_user_id(schedule_id=schedule_id, user_id=user_id)
    if schedule_user is None:
        raise_error('ID not found')
    if schedule_user.user_id != user_id:
        raise_error('Have no access')
    return repositoriesDB.update_feedback(id=schedule_user.id, kritik=kritik, saran=saran)

def insert_schedule_user_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)

def insert_schedule_user_db_by_schedule_id(schedule_id=0, json_object={}):
    schedule_user = repositoriesDB.find_by_schedule_id_and_user_id(schedule_id=schedule_id, user_id=json_object['user_id'])
    user_name = find_by_id(id=json_object['user_id'])
    if schedule_user is not None:
        repositoriesDB.update_delete_by_id(id=schedule_user.id, is_deleted=False)
        return True
    json_object['schedule_id'] = schedule_id
    json_object['user_name'] = user_name.name
    insert_schedule_user_db(json_object=json_object)
    return True


def delete_schedule_user_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)


def is_found_user_id_and_schedule_id(schedule_id=0, user_id=0):
    return repositoriesDB.is_found_user_id_and_schedule_id(user_id=user_id, schedule_id=schedule_id)


def update_schedule_user_for_instructur(schedule_id=0, schedule_user_id=0, instructur_id=0, score=0):
    if not repositoriesDB.is_found_user_id_and_schedule_id(user_id=instructur_id, schedule_id=schedule_id):
        raise_error("Have no access")
    schedule_user = repositoriesDB.find_by_id(id=schedule_user_id)
    if schedule_user is None:
        raise_error("Data not found")
    if schedule_user.schedule_id != schedule_id:
        raise_error("Data not match")
    return repositoriesDB.update_score(id=schedule_user_id, score=score)


def update_schedule_user_for_confirmed(schedule_id=0, schedule_user_id=0, user_id=0, confirmed=False):
    if not repositoriesDB.is_found_user_id_and_schedule_id(user_id=user_id, schedule_id=schedule_id):
        raise_error("Have no access")
    schedule_user = repositoriesDB.find_by_id(id=schedule_user_id)
    if schedule_user is None:
        raise_error("Data not found")
    if schedule_user.schedule_id != schedule_id:
        raise_error("Data not match")
    return repositoriesDB.update_confirmed(id=schedule_user_id, confirmed=confirmed)

def update_schedule_user_for_confirmed_user(schedule_id=0, user_id=0, confirmed=False):
    schedule_user = repositoriesDB.find_by_schedule_id_and_user_id(schedule_id=schedule_id, user_id=user_id)
    if schedule_user is  None:
        raise_error('Data not found')
    return repositoriesDB.update_confirmed(id=schedule_user.id, confirmed=confirmed)


def get_schedule_user_for_instructur(schedule_id=0, schedule_user_id=0):
    return repositoriesDB.get_score_by_id_schedule(schedule_id=schedule_id, schedule_user_id=schedule_user_id)



def schedule_user_generate_certificate(filters=[]):
    from util.image_util import ImageUtil
    datas, _ = repositoriesDB.get_all_with_pagination(page=1, limit=0, filters=filters)
    imageUtil = ImageUtil()
    for data in datas:
        repositoriesDB.update_certificate(id=data['id'], certificate_url=imageUtil.write(text=data['user_name']))
    return True

def schedule_user_generate_undangan(schedule_id=0):
    from entitas.schedule.services import find_schedule_db_by_id
    schedule = find_schedule_db_by_id(id=schedule_id, to_model=False)
    if schedule is None:
        raise_error('Schedule not found')
    Thread(target=send_email_undangan_bulk, kwargs={"schedule_id": schedule_id, "schedule": schedule}).start()
    return True

def send_email_undangan_bulk(schedule_id=0, schedule=None):
    from util.mail_service import MailService
    from entitas.user.services import find_user_db_by_id
    filters=[]
    filters.append({'field': 'schedule_id', 'value': int(schedule_id)})
    datas, _ = repositoriesDB.get_all_with_pagination(page=1, limit=0, filters=filters, to_model=True)
    mail_service = MailService()
    for data in datas:
        user = find_user_db_by_id(id=data.user_id, to_model=True)
        if user is not None:
            user.email = 'candra@g2academy.co'
            print('schedule --> ',schedule)
            mail_service.send_email_undangan(receiver_email=user.email, data=schedule, subject=schedule['name'])


def delete_schedule_user_by_schedule_id(schedule_id=0, id=0):
    schedule_user = find_schedule_user_db_by_id(id=id, to_model=True)
    if schedule_user is None:
        raise_error(msg="Schedule Instructur not found")
    delete_schedule_user = delete_schedule_user_by_id(id=id)
    if delete_schedule_user is None:
        raise_error(msg="Failed to delete")
    return True

def update_schedule_user_by_schedule_id(schedule_id=0, user_id=0, json_object={}):
    schedule_user = find_schedule_user_for_student_by_id(schedule_id=schedule_id, user_id=user_id, to_model=True)
    print(json_object)
    if schedule_user is None:
        raise_error(msg="Schedule User not found")
    json_object["in_absent"] = json_object["in_absent"]
    json_object["out_absent"] = json_object["out"]
    return repositoriesDB.update_absent(user_id=user_id, json_object=json_object)

def update_schedule_user_for_in_absen(schedule_id=0, user_id=0, in_absent=None):

    schedule_user = repositoriesDB.find_by_schedule_id_and_user_id(schedule_id=schedule_id, user_id=user_id)
    if schedule_user is None:
        raise_error('Schedul user tidak ditemukan')
    if schedule_user.certificate_url in [None, '', '-', ' ']:
        imageUtil = ImageUtil()
        repositoriesDB.update_certificate(id=schedule_user.id, certificate_url=imageUtil.write(text=schedule_user.user_name))
    return repositoriesDB.update_absent_in(schedule_id=schedule_id, user_id=user_id, in_absent=in_absent)

def update_schedule_user_for_out_absen(schedule_id=0, user_id=0, out_absent=None):
    schedule_user = repositoriesDB.find_by_schedule_id_and_user_id(schedule_id=schedule_id, user_id=user_id)
    if schedule_user is None:
        raise_error('Schedul user tidak ditemukan')
    if schedule_user.certificate_url in [None, '', '-', ' ']:
        imageUtil = ImageUtil()
        repositoriesDB.update_certificate(id=schedule_user.id, certificate_url=imageUtil.write(text=schedule_user.user_name))
    return repositoriesDB.update_absent_out(schedule_id=schedule_id, user_id=user_id, out_absent=out_absent)
