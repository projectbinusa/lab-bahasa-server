from datetime import datetime, timedelta

from pony.orm import *

from database.schema import QuestionDB, AnswerDB


@db_session
def get_all(to_model=True):
    result = []
    try:
        for item in select(s for s in QuestionDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_json())
    except Exception as e:
        print("error Question getAll: ", e)
    return result


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in QuestionDB).order_by(desc(QuestionDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(id=item["value"])
            elif item["field"] == "user_name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.user_name)
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
        print("error Question getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def insert(json_object={}, to_model=False):
    try:
        # think_time_str = json_object["think_time"]
        # think_time = datetime.strptime(think_time_str, '%H:%M:%S').time()
        # think_time_delta = timedelta(hours=think_time.hour, minutes=think_time.minute, seconds=think_time.second)
        #
        # answer_time_str = json_object.get("answer_time", "00:00:00")  # Default to "00:00:00" if not provided
        # answer_time = datetime.strptime(answer_time_str, '%H:%M:%S').time()
        # answer_time_delta = timedelta(hours=answer_time.hour, minutes=answer_time.minute, seconds=answer_time.second)

        new_question = QuestionDB(
            name=json_object["name"],
            class_id=json_object["class_id"],
            user_id=json_object["user_id"],
            user_name=json_object["user_name"],
            type=json_object["type"],
            think_time=json_object["think_time"],
            answer_time=json_object["answer_time"]
        )
        commit()
        if to_model:
            return new_question.to_model()
        else:
            return new_question.to_model().to_json()
    except Exception as e:
        print("error question insert: ", e)
    return



@db_session
def update(json_object=None, to_model=False):
    try:
        updated_question = QuestionDB[json_object["id"]]
        if "name" in json_object:
            updated_question.name = json_object["name"]
        if "think_time" in json_object:
            updated_question.think_time = json_object["think_time"]
        if "answer_time" in json_object:
            updated_question.answer_time = json_object["answer_time"]
        if "class_id" in json_object:
            updated_question.class_id = json_object["class_id"]
        if "user_id" in json_object:
            updated_question.user_id = json_object["user_id"]
        if "user_name" in json_object:
            updated_question.user_name = json_object["user_name"]
        if "type" in json_object:
            updated_question.type = json_object["type"]

        commit()

        if to_model:
            return updated_question.to_model()
        else:
            return updated_question.to_model().to_response()
    except Exception as e:
        print("error UserDB update_profile: " + str(e))
        return


@db_session
def delete_by_id(id=None):
    try:
        QuestionDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Question delete: ", e)
    return


@db_session
def find_question_by_id(id=None):
    data_in_db = select(s for s in QuestionDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def create_competition(json_object={}, to_model=False):
    try:
        new_competition = QuestionDB(
            name=json_object["name"],
            class_id=json_object["class_id"],
            user_id=json_object["user_id"],
            user_name=json_object["user_name"],
            type=json_object["type"],
            think_time=json_object["think_time"],
            answer_time=json_object["answer_time"]
        )
        commit()
        if to_model:
            return new_competition.to_model()
        else:
            return new_competition.to_model().to_response_competition()
    except Exception as e:
        print("eror create competition: ", e)
    return None


@db_session
def find_by_id_answer_time(answer_time=None):
    data_in_db = select(s for s in QuestionDB if s.answer_time == answer_time)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def find_by_question_id_and_class_id(class_id=0, id=0):
    data_in_db = select(s for s in QuestionDB if s.id == id and s.class_id == class_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

# @db_session
# def answer(json_object={}, to_model=False):
#

@db_session
def save_competition(json_object={}, to_model=False):
    try:
        new_competition = QuestionDB(
            name=json_object["name"],
            class_id=json_object["class_id"],
            user_id=json_object["user_id"],
            user_name=json_object["user_name"],
            type=json_object["type"],
            think_time=json_object["think_time"],
            answer_time=json_object["answer_time"]
        )
        commit()
        if to_model:
            return new_competition.to_model()
        else:
            return new_competition.to_model().to_response_competition()
    except Exception as e:
        print("error Question insert: ", e)
    return None


@db_session
def check_answer_time(question_id):
    # Temukan pertanyaan dan jawaban berdasarkan ID
    question = select(q for q in QuestionDB if q.id == question_id).first()
    answer = select(a for a in AnswerDB if a.question_id == question_id).first()

    if not question or not answer:
        return "Question or answer not found."

    # Tidak perlu konversi jika question.answer_time sudah timedelta
    question_answer_time = question.answer_time
    print("quest_answer_time ==> ", question_answer_time)

    # Konversi answer_time_user ke timedelta jika belum
    if isinstance(answer.answer_time_user, str):
        # Misalkan answer_time_user adalah string dalam format 'HH:MM:SS'
        hours, minutes, seconds = map(int, answer.answer_time_user.split(':'))
        answer_time_user = timedelta(hours=hours, minutes=minutes, seconds=seconds)
        print("answer time user ==> ", answer_time_user)
    else:
        answer_time_user = answer.answer_time_user

    # Bandingkan waktu jawaban pengguna dengan batas waktu jawaban
    if answer_time_user > question_answer_time:
        raise ValueError("Jawaban melebihi batas waktu")
    else:
        return "Jawaban diberikan tepat waktu."
# @db_session
# def save_competition_answer(json_object={}):
#     try:
#         # Format the datetime object to a string
#         answer_time_formatted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#         new_answer = QuestionDB(
#             class_id=json_object['class_id'],
#             user_id=json_object['user_id'],
#             answer=json_object['answer'],
#             answer_time_client=answer_time_formatted  # Save as a formatted string
#         )
#         commit()
#         return new_answer
#     except Exception as e:
#         print(f"Error saving answer: {e}")
#         return None
#
#
# @db_session
# def get_active_competition(class_id):
#     # Get the active competition for the class
#     active_competitions = select(s for s in QuestionDB if s.class_id == class_id)
#     return active_competitions.first() if active_competitions else None
