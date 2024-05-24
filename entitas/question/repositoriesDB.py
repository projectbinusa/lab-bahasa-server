from pony.orm import *

from database.schema import QuestionDB

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
        new_question = QuestionDB(
            think_time=json_object["think_time"],
            answer_time=json_object["answer_time"],
            class_id=json_object["class_id"],
            user_id=json_object["user_id"],
            user_name=json_object["user_name"],
            score=json_object["score"],
            answer_time_client=json_object["answer_time_client"],
            answer=json_object["answer"]
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
        if "score" in json_object:
            updated_question.score = json_object["score"]
        if "answer_time_client" in json_object:
            updated_question.answer_time_client = json_object["answer_time_client"]
        if "answer" in json_object:
            updated_question.answer = json_object["answer"]

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