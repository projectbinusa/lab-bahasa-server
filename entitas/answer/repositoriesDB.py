from datetime import timedelta

from pony.orm import *

from database.schema import AnswerDB, QuestionDB


@db_session
def get_all(to_model=True):
    result = []
    try:
        for item in select(s for s in AnswerDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to.response())
    except Exception as e:
        print("error answer getAll: ", e)
    return result


@db_session
def get_all_with_pagination(
        page=1,
        limit=9,
        to_model=False,
        filters=[],
):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in AnswerDB)
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
            elif item["field"] == "class_id":
                data_in_db = data_in_db.filter(lambda d: item["value"] == d.class_id)
            elif item["field"] == "user_id":
                data_in_db = data_in_db.filter(lambda d: item["value"] == d.user_id)

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
        print("error Answer getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in AnswerDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def find_by_id_answer_time_user(answer_time_user=None):
    data_in_db = select(s for s in AnswerDB if s.answer_time_user == answer_time_user)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def find_by_answer_id_and_class_id(class_id=0, id=0):
    data_in_db = select(s for s in AnswerDB if s.id == id and s.class_id == class_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def update(json_object={}, to_model={}):
    try:
        updated_answer = AnswerDB[json_object["id"]]
        updated_answer.question_id = json_object["question_id"]
        updated_answer.answer = json_object["answer"]
        updated_answer.user_id = json_object["user_id"]
        updated_answer.answer_time_user = json_object["answer_time_user"]
        updated_answer.class_id = json_object["class_id"]
        commit()
        if to_model:
            return updated_answer.to_model()
        else:
            return updated_answer.to_model().to_response()
    except Exception as e:
        print("error Answer update: ", e)
    return None


@db_session
def delete_by_id(id=None):
    try:
        AnswerDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Answer delete: ", e)
    return


@db_session
def update_delete_by_id(id=None, is_deleted=False):
    try:
        AnswerDB[id].is_deleted = is_deleted
        commit()
        return True
    except Exception as e:
        print('error Answer delete: ', e)
    return


@db_session
def create_profile_answer(json_object={}, to_model=False):
    print("ini create answer di repo == >", json_object)
    try:
        new_answer = AnswerDB(
            question_id=json_object['question_id'],
            answer=json_object['answer'],
            user_id=json_object['user_id'],
            answer_time_user=json_object['answer_time_user'],
            class_id=json_object['class_id']
        )
        commit()
        return new_answer.to_model() if to_model else new_answer.to_model().to_response()
    except Exception as e:
        print("error creating profile: " + str(e))
        raise

@db_session
def find_existing_answer_by_question_id(question_id):
    return select(a for a in AnswerDB if a.question_id == question_id).first()

@db_session
def check_answer(question_id):
    # Mendapatkan waktu jawaban terbaru dari tabel jawaban (Answer)
    answer_time = select(a.answer_time_user for a in AnswerDB if a.question_id == question_id).first()

    # Mendapatkan waktu pertanyaan dari tabel pertanyaan (Question)
    question_time = select(q for q in QuestionDB if q.id == question_id).first()

    question_answer_time = question_time.answer_time
    # Konversi answer_time_user ke timedelta jika belum
    if isinstance(answer_time.answer_time_user, str):
        # Misalkan answer_time_user adalah string dalam format 'HH:MM:SS'
        hours, minutes, seconds = map(int, answer_time.answer_time_user.split(':'))
        answer_time_user = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        print("answer time user ==> ", answer_time_user)
    else:
        answer_time_user = answer_time.answer_time_user
    # Memeriksa apakah waktu jawaban melebihi waktu pertanyaan
    if answer_time_user > question_answer_time:
        raise ValueError("Waktu jawaban melebihi waktu pertanyaan")

    # Jika tidak, mengembalikan jawaban
    return select(a for a in AnswerDB if a.question_id == question_id).first()


@db_session
def insert(json_object={}, to_model=False):
    try:
        new_answer = AnswerDB(
            question_id=json_object["question_id"],
            answer=json_object["answer"],
            user_id=json_object["user_id"],
            answer_time_user=json_object["answer_time_user"],
            class_id=json_object["class_id"],
        )
        commit()
        if to_model:
            return new_answer.to_model()
        else:
            return new_answer.to_model().to_response()
    except Exception as e:
        print("error Answer insert: ", e)
    return None
