from entitas.instructur import services
from util.entitas_util import *

class InstructurResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination= services.get_instructur_db_with_pagination(page=page, limit=limit, filters=filters)
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.insert_instructur_db(json_object=req.media))

class InstructurWithIdResource:
    def on_get(self, req, resp, instructur_id: int):
        resouce_response_api(resp=resp, data=services.find_instructur_db_by_id(id=int(instructur_id)))

    def on_put(self, req, resp, instructur_id: int):
        body = req.media
        body["id"] = int(instructur_id)
        resouce_response_api(resp=resp, data=services.update_instructur_db(json_object=body))

    def on_delete(self, req, resp, instructur_id: int):
        resouce_response_api(resp=resp, data=services.delete_instructur_db(id=int(instructur_id)))