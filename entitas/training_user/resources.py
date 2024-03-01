from entitas.training_user import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class TrainingUserResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_training_user_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.insert_training_user_db(json_object=req.media))


class TrainingUserWithIdResource:
    def on_get(self, req, resp, training_user_id: int):
        resouce_response_api(resp=resp, data=services.find_training_user_db_by_id(id=int(training_user_id)))

    def on_put(self, req, resp, training_user_id: int):
        body = req.media
        body["id"] = int(training_user_id)
        resouce_response_api(resp=resp, data=services.update_training_user_db(json_object=body))

    def on_delete(self, req, resp, training_user_id: int):
        resouce_response_api(resp=resp, data=services.delete_training_user_by_id(id=int(training_user_id)))
