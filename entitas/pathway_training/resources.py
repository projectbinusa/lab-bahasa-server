from entitas.pathway_training import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class PathwayTrainingResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_pathway_training_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.insert_pathway_training_db(json_object=req.media))


class PathwayTrainingWithIdResource:
    def on_get(self, req, resp, pathway_training_id: int):
        resouce_response_api(resp=resp, data=services.find_pathway_training_db_by_id(id=int(pathway_training_id)))

    def on_put(self, req, resp, pathway_training_id: int):
        body = req.media
        body["id"] = int(pathway_training_id)
        resouce_response_api(resp=resp, data=services.update_pathway_training_db(json_object=body))

    def on_delete(self, req, resp, pathway_training_id: int):
        resouce_response_api(resp=resp, data=services.delete_pathway_training_by_id(id=int(pathway_training_id)))
