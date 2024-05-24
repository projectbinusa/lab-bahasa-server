from datetime import datetime

from pony.orm import commit

from entitas.question import repositoriesDB

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
