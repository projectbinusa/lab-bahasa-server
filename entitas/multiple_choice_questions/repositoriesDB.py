from pony.orm import *

from database.schema import MultipleChoiceQuestionsDB


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        class_id = next((x["value"] for x in filters if x.get("field") == "class_id"), 0)
        data_in_db = select((s) for s in MultipleChoiceQuestionsDB if s.class_id == class_id)
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
            elif item["field"] == "class_id":
                data_in_db = data_in_db.filter(lambda d: item["value"] == d.class_id)
            elif item["field"] == "question_text":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.question_text)
            # elif item["field"] == "instructur_id":
            #     data_in_db = data_in_db.filter(lambda d: d.class_id != item["value"])

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
        print("error ScheduleUser getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def add_multiple_choice_questions(user_id, class_id, user_name, json_objects, to_model=False):
    print("user_id in repositories => ", user_id)
    new_questions = []
    for json_object in json_objects:
        new_question = MultipleChoiceQuestionsDB(
            question_text=json_object["question_text"],
            user_id=user_id,
            user_name=user_name,
            class_id=class_id,
            chosen=json_object["chosen"],
            options=json_object["options"],
            correct_answer=json_object["correct_answer"]
        )
        new_questions.append(new_question)
    commit()
    if to_model:
        return [question.to_model() for question in new_questions]
    return [question.to_model().to_response() for question in new_questions]


# @db_session
# def update_multiple_choice_question(user_id, class_id, user_name, json_object, to_model=False):
#     question_id = json_object["id"]
#     question = MultipleChoiceQuestionsDB.get(id=question_id, user_id=user_id, class_id=class_id)
#     if question:
#         question.question_text = json_object.get("question_text", question.question_text)
#         question.chosen = json_object.get("chosen", question.chosen)
#         question.options = json_object.get("options", question.options)
#         question.correct_answer = json_object.get("correct_answer", question.correct_answer)
#         commit()
#         if to_model:
#             return question.to_model()
#         return question.to_model().to_response()
#     else:
#         raise ValueError(f"Question with ID {question_id} not found.")

@db_session
def update_multiple_choice_question(user_id, user_name, class_id, json_object, to_model=False):
    try:
        updated_question = MultipleChoiceQuestionsDB[json_object["id"]]
        if "question_text" in json_object:
            updated_question.question_text = json_object["question_text"]
        if "chosen" in json_object:
            updated_question.chosen = json_object["chosen"]
        if "options" in json_object:
            updated_question.options = json_object["options"]
        if "correct_answer" in json_object:
            updated_question.correct_answer = json_object["correct_answer"]

        updated_question.user_id = user_id
        updated_question.user_name = user_name
        updated_question.class_id = class_id

        commit()

        if to_model:
            return updated_question.to_model()
        else:
            return updated_question.to_model().to_response()
    except Exception as e:
        print("error Multiple Choice Question: " + str(e))
        return


@db_session
def delete_by_id_multiple_choice_question(id=None):
    try:
        MultipleChoiceQuestionsDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Room delete: ", e)
    return

@db_session
def delete_by_id_and_class_id(id=None, class_id=None):
    try:
        MultipleChoiceQuestionsDB.get(id=id, class_id=class_id).delete()
        commit()
        return True
    except Exception as e:
        print("error Group delete: ", e)
        return False

@db_session
def find_by_id_multiple_choice_question(id=None):
    data_in_db = select(s for s in MultipleChoiceQuestionsDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def find_by_id_multiple_choice_question_by_class_id(id=None, class_id=None):
    data_in_db = select(s for s in MultipleChoiceQuestionsDB if s.id == id and s.class_id == class_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()