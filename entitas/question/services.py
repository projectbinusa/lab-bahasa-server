
from pony.orm import commit, db_session, desc
from select import select

from database.schema import QuestionDB
from entitas.question import repositoriesDB
from entitas.question.repositoriesDB import get_active_competition
from datetime import datetime, timedelta


def insert_question_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)


def get_question_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def delete_question_by_id(id=0):
    return repositoriesDB.delete_by_id(id)


def update_question_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)


def start_competition(class_id, question_id):
    question = repositoriesDB.find_question_by_id(question_id)
    if not question:
        raise ValueError("Question not found")

    question.class_id = class_id
    question.created_date = datetime.now()
    commit()
    return question.to_json()


def submit_answer(user_id, question_id, answer, type):
    question = repositoriesDB.find_question_by_id(question_id)
    if not question:
        raise ValueError("Question not found")

    if type == 'first_to_answer':
        if not question.answer:
            question.answer = answer
            question.user_id = user_id
            question.answer_time_client = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            commit()
            return {"status": "answered", "message": "You are the first to answer"}
        else:
            return {"status": "failed", "message": "Question already answered"}

    elif type == 'enter_an_answer':
        question.answer = answer
        question.user_id = user_id
        question.answer_time_client = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        commit()
        return {"status": "submitted", "message": "Answer submitted"}

    elif type == 'demo_to_answer':
        if not question.answer:
            question.answer = answer
            question.user_id = user_id
            question.answer_time_client = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            commit()
            return {"status": "answered", "message": "You have demonstrated the answer"}
        else:
            return {"status": "failed", "message": "Question already answered"}

    return {"status": "failed", "message": "Unknown competition mode"}


def start_competition(json_object={}):
    class_id = json_object.get('class_id')
    # Optional: Validate other fields as well
    if not class_id:
        raise ValueError("class_id is required")

    # Check if an active competition exists and return it or create a new one
    # existing_competition = get_active_competition(class_id)
    # if existing_competition:
    #     return existing_competition.to_response_competition()

    # Otherwise, create a new competition
    return repositoriesDB.save_competition(json_object=json_object)


# def handle_first_to_answer(json_object={}):
#     class_id = json_object.get('class_id')
#     user_id = json_object.get('user_id')
#     answer = json_object.get('answer')
#     if not class_id or not user_id or not answer:
#         raise ValueError("class_id, user_id, and answer are required")
#
#     competition = get_active_competition(class_id)
#     if not competition:
#         raise ValueError("No active competition found for this class")
#
#     if competition.answer:
#         return {"status": "failed", "message": "Question already answered"}
#
#     competition.user_id = user_id
#     competition.answer = answer
#     competition.answer_time_client = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     commit()
#     return {"status": "answered", "message": "You are the first to answer"}
#
#
# @db_session
# def handle_enter_answer(json_object={}):
#     class_id = json_object.get('class_id')
#     user_id = json_object.get('user_id')
#     answer = json_object.get('answer')
#
#     if not class_id or not user_id or not answer:
#         return {"status": "failed", "message": "Missing required parameters: class_id, user_id, and/or answer"}
#
#         # Check if the user has already answered this question
#     existing_answer = QuestionDB.select(lambda q: q.class_id == class_id and q.user_id == user_id).order_by(
#         desc(QuestionDB.id)).first()
#     if existing_answer:
#         return {"status": "failed", "message": "You have already answered this question."}
#
#
# def handle_demo_to_answer(json_object={}, userjson_object={}):
#     class_id = json_object.get('class_id')
#     user_id = json_object.get('user_id')
#     answer = json_object.get('answer')
#
#     if not class_id or not user_id or not answer:
#         raise ValueError("Missing required parameters: class_id, user_id, and/or answer")
#
#     competition = get_active_competition(class_id)
#     if not competition:
#         return {"status": "failed", "message": "No active competition found for this class"}
#
#     # Demo logic might include handling predefined answers or simulations
#     # For demonstration, let's assume it simply logs the attempt
#     print(f"Demo answer received: {answer} from user {userjson_object['user_id']} in class {class_id}")
#
#     # Save the competition answer for demo as well
#     saved_answer = repositoriesDB.save_competition_answer(json_object)
#     if saved_answer:
#         return {"status": "success", "message": "Demo answer submitted successfully"}
#     else:
#         return {"status": "error", "message": "Failed to submit demo answer"}

