from entitas.training_material import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class TrainingMaterialResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_training_material_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.insert_training_material_db(json_object=req.media))


class TrainingMaterialWithIdResource:
    def on_get(self, req, resp, training_material_id: int):
        resouce_response_api(resp=resp, data=services.find_training_material_db_by_id(id=int(training_material_id)))

    def on_put(self, req, resp, training_material_id: int):
        body = req.media
        body["id"] = int(training_material_id)
        resouce_response_api(resp=resp, data=services.update_training_material_db(json_object=body))

    def on_delete(self, req, resp, training_material_id: int):
        resouce_response_api(resp=resp, data=services.delete_training_material_by_id(id=int(training_material_id)))

class TrainingMaterialWithTrainingIdResource:
    def on_get(self, req, resp, training_id: int):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param('page', required=False, default=1))
        limit = int(req.get_param('limit', required=False, default=9))
        data, pagination = services.get_training_material_by_training_id_with_pagination(
            page=page, limit=limit, filters=filters, training_id=training_id
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

class dInstructurTrainingMaterialWithTrainingIdResource:
    def on_get(self, req, resp, training_id: int):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param('page', required=False, default=1))
        limit = int(req.get_param('limit', required=False, default=9))
        data, pagination = services.get_training_material_by_training_id_for_instructur(
            page=page, limit=limit, filters=filters, training_id=int(training_id), user_id=req.context['user']['id']
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

