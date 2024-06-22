from datetime import datetime, timedelta

from falcon import HTTPBadRequest

from entitas.answer import repositoriesDB
from entitas.answer.repositoriesDB import update, get_all_with_pagination, find_existing_answer_by_question_id
from entitas.kelas_user.repositoriesDB import find_kelas_user_db_by_id
from entitas.user.repositoriesDB import find_by_id
from entitas.question.repositoriesDB import find_question_by_id, find_by_id_answer_time, \
    find_by_question_id_and_class_id, check_answer_time
from util.other_util import raise_error


def get_services_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_services_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


def find_answer_by_class_id(class_id=0, answer_id=0):
    answer = find_answer_db_by_id(id=answer_id, to_model=True)
    if answer is None:
        raise_error(msg="answer not found")
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if kelas is None:
        raise_error(msg="class not found")
    return answer.to_response()


def find_answer_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


def get_list_by_class_id(class_id=0, page=1, limit=9, filters=[], answer="", to_model=False):
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    print("ini class id =====>", class_id)
    if kelas is None:
        raise_error(msg="class not found")
    return get_answer_db_with_pagination(page=page, limit=limit, filters=filters, answer=answer, to_model=to_model)

def get_answer_db_with_pagination(page=1, limit=9, answer="", to_model=False, filters=[], to_response="to_response"):
    return repositoriesDB.get_all_with_pagination(page=page, limit=limit, answer=answer, to_model=to_model, filters=filters, to_response=to_response)



def update_services_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)


def update_answer_by_class_id(class_id=0, id=0, json_object={}):
    # try:
    answer = find_answer_db_by_id(id=id, to_model=True)
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if answer is None:
        raise_error(msg="answer not found")
    if kelas is None:
        raise_error(msg="kelas not found")
    json_object["id"] = answer.id
    json_object["class_id"] = class_id
    return update(json_object=json_object)
    # except Exception as e:
    #     print("Error:", e)
    #     return None


def insert_answer_db(json_object={}):
    return repositoriesDB.create_profile_answer(json_object=json_object, to_model=True)


# from datetime import datetime, timedelta

def check_answer(json_object, answer_time_user_str):
    question = find_question_by_id(json_object['question_id'])
    if not question:
        raise ValueError("Question not found")

    answer_time_user = json_object["answer_time_user"]
    end_time = question.answer_time
    print(answer_time_user)
    print(end_time)

    # answer_time_user = datetime.combine(datetime.today(), answer_time_user) - datetime.combine(datetime.today(), datetime.min.time())

    if answer_time_user > end_time:
        raise ValueError("Waktu telah habis")

    return True

import pytz

def create_answer_service(json_object={}):
    class_id = json_object['class_id']
    user_id = json_object['user_id']
    question_id = json_object['question_id']

    # Zona waktu WIB (UTC+7)
    wib = pytz.timezone('Asia/Jakarta')
    answer_time_user_str = datetime.now(wib).strftime('%H:%M')

    json_object['answer_time_user'] = answer_time_user_str

    check_answer(json_object, answer_time_user_str)

    question = find_question_by_id(question_id)
    if question is None:
        raise ValueError("Question not found")

    if question.type == 'first_to_answer':
        existing_answer = find_existing_answer_by_question_id(question_id)
        if existing_answer:
            raise ValueError("Question has already been answered by another user")

    answer_info = repositoriesDB.create_profile_answer(json_object=json_object)

    kelas_user = repositoriesDB.find_by_answer_id_and_class_id(class_id=class_id)
    user = find_by_id(id=user_id)

    if kelas_user is not None:
        repositoriesDB.update_delete_by_id(id=kelas_user.id, is_deleted=False)
        return True

    if user is None:
        raise ValueError("User not found")

    return answer_info



# def create_answer_service(class_id=0, json_object={}, user_id=0):
#     try:
#         question = find_by_id_answer_time(answer_time=json_object['answer_time_user'])
#         print("ini question id di service ==> ", question)
#         if question is None:
#             raise_error(msg="Batas waktu jawaban sudah habis")
#
#         existing_answer = find_question_by_id(json_object['question_id'])
#         if existing_answer:
#             raise_error(msg="Pertanyaan sudah dijawab oleh siswa lain")
#
#         kelas_user = repositoriesDB.find_by_answer_id_and_class_id(class_id=class_id)
#         user = find_by_id(id=user_id)
#         if kelas_user is not None:
#             repositoriesDB.update_delete_by_id(id=kelas_user.id, is_deleted=False)
#             return True
#         if user is None:
#             raise_error(msg="User not found")
#         json_object['class_id'] = class_id
#         json_object['user_id'] = user_id
#         insert_answer_db(json_object=json_object)
#         return True
#     except Exception as e:
#         print("Error:", e)
#         return None


def delete_answer_db_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)


def delete_answer_by_class_id(class_id=0, id=0):
    answer = find_answer_db_by_id(id=id, to_model=True)
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    if kelas is None:
        raise_error(msg="Kelas not found")
    if answer is None:
        raise_error(msg="answer not found")
    delete_answer = delete_answer_db_by_id(id=id)
    if delete_answer is None:
        raise_error(msg="Failed to delete")
    return True

def get_answer_by_class_id_and_user_id(class_id=0, page=1, user_id=0, limit=9, filters=[], to_model=False):
    kelas = find_kelas_user_db_by_id(id=class_id, to_model=True)
    user = find_by_id(id=user_id)
    if kelas is None:
        raise_error(msg="kelas not found")
    if user is None:
        raise_error(msg="user not found")
    return get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)
