from entitas.kelas_user import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class KelasUserResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        filters.append({"field": "user_id", "value": req.context['user']['id']})
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_kelas_user_db_with_pagination(page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        body = req.media
        body["user_id"] = req.context['user']['id']
        resouce_response_api(resp=resp, data=services.insert_kelas_user_db(json_object=body))


class KelasUserWithIdResource:
    def on_get(self, req, resp, class_id: int):
        resouce_response_api(resp=resp, data=services.find_kelas_user_for_student_by_id(id=int(class_id), user_id=req.context['user']['id']))

    def on_put(self, req, resp, class_id: int):
        body = req.media
        body["id"] = int(class_id)
        resouce_response_api(resp=resp, data=services.update_kelas_user_db(json_object=body))

    def on_delete(self, req, resp, class_id: int):
        resouce_response_api(resp=resp, data=services.delete_kelas_user_by_id(id=int(class_id)))

