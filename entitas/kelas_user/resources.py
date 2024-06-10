from entitas.kelas_user import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class KelasUserResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_kelas_user_db_with_pagination(page=page, limit=limit, filters=filters)
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        file = req.get_param('file')
        description = req.get_param('description')
        name = req.get_param('name')
        is_active = req.get_param('is_active')
        body = {}
        body["description"] = description
        body["name"] = name
        body["is_active"] = is_active
        # body['user_id'] = req.context["user"]["id"]
        resouce_response_api(resp=resp, data=services.insert_kelas_user_db(json_object=body, file=file))


class KelasUserWithIdResource:
    def on_get(self, req, resp, class_id: int):
        resouce_response_api(resp=resp, data=services.find_kelas_user_db_by_id(id=int(class_id)))

    def on_put(self, req, resp, class_id: int):
        file = req.get_param('file')
        description = req.get_param('description')
        name = req.get_param('name')
        # is_active = req.get_param('is_active')
        body = {}
        body["id"] = int(class_id)
        body["description"] = description
        body["name"] = name
        # body["is_active"] = is_active
        # body['user_id'] = req.context["user"]["id"]
        resouce_response_api(resp=resp, data=services.update_kelas_user_db(json_object=body, file=file))

    def on_delete(self, req, resp, class_id: int):
        resouce_response_api(resp=resp, data=services.delete_kelas_user_by_id(id=int(class_id)))

class KelasUserActive:
    def on_put(self, req, resp, class_id: int):
        body = {}
        body["id"] = int(class_id)
        body["is_active"] = req.media.get("is_active", 1)
        body["user_id"] = req.context["user"]["id"]
        body["user_name"] = req.context["user"]["name"]
        resouce_response_api(resp=resp, data=services.kelas_user_active_db(json_object=body))

class KelasUserNotActive:
    def on_put(self, req, resp, class_id: int):
        body = {}
        body["id"] = int(class_id)
        body["is_active"] = req.media.get("is_active", 0)
        resouce_response_api(resp=resp, data=services.kelas_user_active_db(json_object=body))