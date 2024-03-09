from entitas.material import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class MaterialResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=3))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_material_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)
    def on_post(self, req, resp):
        file = req.get_param("file")
        body = {}
        body['name'] = req.get_param("name")
        body['description'] = req.get_param("description")
        body["user_id"] = req.context["user"]["id"]
        resouce_response_api(resp=resp, data=services.insert_material_db(json_object=body, file=file))


class MaterialWithIdResource:
    def on_get(self, req, resp, material_id: int):
        resouce_response_api(resp=resp, data=services.find_material_db_by_id(id=int(material_id)))

    def on_put(self, req, resp, material_id: int):
        file = req.get_param("file")
        body = {}
        body['name'] = req.get_param("name")
        body['description'] = req.get_param("description")
        body["user_id"] = req.context["user"]["id"]
        resouce_response_api(resp=resp, data=services.update_material_db(json_object=body, file=file))

    def on_delete(self, req, resp, material_id: int):
        resouce_response_api(resp=resp, data=services.delete_material_by_id(id=int(material_id)))
