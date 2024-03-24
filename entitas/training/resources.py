from entitas.training import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class TrainingResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_training_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.insert_training_db(json_object=req.media))


class TrainingWithIdResource:
    def on_get(self, req, resp, training_id: int):
        resouce_response_api(resp=resp, data=services.find_training_db_by_id(id=int(training_id)))

    def on_put(self, req, resp, training_id: int):
        body = req.media
        body["id"] = int(training_id)
        resouce_response_api(resp=resp, data=services.update_training_db(json_object=body))

    def on_delete(self, req, resp, training_id: int):
        resouce_response_api(resp=resp, data=services.delete_training_by_id(id=int(training_id)))

class InstructurTrainingResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_training_for_instructur(
            page=page, limit=limit, filters=filters, user_id=req.context['user']['id']
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

class InstructurTrainingWithIdResource:
    def on_get(self, req, resp, training_id: int):
        resouce_response_api(resp=resp, data=services.instructur_preview_training_db_by_id(id=int(training_id), user_id=req.context['user']['id']))
