from entitas.question import services
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

    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.insert_question_db(json_object=req.media))

class QuestionWithIdResource:
    def on_put(self, req, resp, response_competition_id: int):
        body = req.media
        body["id"] = int(response_competition_id)
        resouce_response_api(resp=resp, data=services.update_question_db(json_object=body))

    def on_delete(self, req, resp, response_competition_id: int):
        resouce_response_api(resp=resp, data=services.delete_question_by_id(id=int(response_competition_id)))