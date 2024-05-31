from datetime import datetime

import falcon

from entitas.question import services
from entitas.question.services import handle_first_to_answer, start_competition, handle_enter_answer, \
    handle_demo_to_answer
from util.entitas_util import generate_filters_resource, resouce_response_api


class QuestionResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['user_name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_question_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    # def on_post(self, req, resp):
    #     resouce_response_api(resp=resp, data=services.insert_question_db(json_object=req.media))

    def on_post(self, req, resp):
        json_object = req.media
        resouce_response_api(resp=resp, data=services.insert_question_db(json_object=json_object))


class QuestionWithIdResource:
    def on_put(self, req, resp, response_competition_id: int):
        body = req.media
        body["id"] = int(response_competition_id)
        resouce_response_api(resp=resp, data=services.update_question_db(json_object=body))

    def on_post(self, req, resp, response_competition_id: int):
        body = req.media
        body["id"] = int(response_competition_id)
        body["updated_date"] = datetime.now()
        resouce_response_api(resp=resp, data=services.update_question_db(json_object=body))

    def on_delete(self, req, resp, response_competition_id: int):
        resouce_response_api(resp=resp, data=services.delete_question_by_id(id=int(response_competition_id)))


class StartCompetitionResource:
    def on_post(self, req, resp, class_id):
        json_object = req.media
        json_object["class_id"] = class_id
        resouce_response_api(resp=resp, data=services.start_competition(json_object=json_object))
        # def on_post(self, req, resp):
        #     data = req.media
        #     class_id = data.get('class_id')
        #     question_type = data.get('type')
        #     think_time = data.get('think_time')
        #     answer_time = data.get('answer_time')
        #     if not class_id or not question_type or not think_time or not answer_time:
        #         raise falcon.HTTPBadRequest('Bad Request', 'All fields are required')
        #     competition = start_competition(class_id, question_type, think_time, answer_time)
        #     resp.media = {'competition': competition}


# class FirstToAnswerResource:
#     def on_post(self, req, resp, class_id):
#         json_object = req.media
#         json_object["class_id"] = class_id
#         resouce_response_api(resp=resp, data=services.handle_first_to_answer(json_object=json_object))
#         # data = req.media
#         # user_id = data.get('user_id')
#         # class_id = data.get('class_id')
#         # answer = data.get('answer')
#         # if not user_id or not class_id or not answer:
#         #     raise falcon.HTTPBadRequest('Bad Request', 'All fields are required')
#         # result = handle_first_to_answer(user_id, class_id, answer)
#         # resp.media = {'result': result}
#
#
# class EnterAnswerResource:
#     def on_put(self, req, resp, class_id):
#         json_object = req.media
#         json_object["class_id"] = class_id
#         resouce_response_api(resp=resp, data=services.handle_enter_answer(json_object=json_object))
#         # data = req.media
#         # user_id = data.get('user_id')
#         # class_id = data.get('class_id')
#         # answer = data.get('answer')
#         # if not user_id or not class_id or not answer:
#         #     raise falcon.HTTPBadRequest('Bad Request', 'All fields are required')
#         # result = handle_enter_answer(user_id, class_id, answer)
#         # resp.media = {'result': result}
#
#
# class DemoToAnswerResource:
#     def on_post(self, req, resp, class_id):
#         json_object = req.media
#         json_object["class_id"] = class_id
#         resouce_response_api(resp=resp, data=services.handle_demo_to_answer(json_object=json_object))
#         # data = req.media
#         # user_id = data.get('user_id')
#         # class_id = data.get('class_id')
#         # answer = data.get('answer')
#         # if not user_id or not class_id or not answer:
#         #     raise falcon.HTTPBadRequest('Bad Request', 'All fields are required')
#         # result = handle_demo_to_answer(user_id, class_id, answer)
#         # resp.media = {'result': result}
