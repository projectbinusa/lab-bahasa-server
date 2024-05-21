from entitas.absent import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class AbsentResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_absent_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        body = req.media
        body['user_id'] = req.context['user']['id']
        resouce_response_api(resp=resp, data=services.insert_absent_db(json_object=body))

class AdminAbsentResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id', 'training_id', 'schedule_id'], params_string=['user_name', 'training_name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_absent_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        body = req.media
        resouce_response_api(resp=resp, data=services.insert_absent_db(json_object=body))


class AbsentWithIdResource:
    def on_get(self, req, resp, absent_id: int):
        resouce_response_api(resp=resp, data=services.find_absent_db_by_id(id=int(absent_id)))

    def on_put(self, req, resp, absent_id: int):
        body = req.media
        body["id"] = int(absent_id)
        resouce_response_api(resp=resp, data=services.update_absent_db(json_object=body))

    def on_delete(self, req, resp, absent_id: int):
        resouce_response_api(resp=resp, data=services.delete_absent_by_id(id=int(absent_id)))

class AbsentWithIdSignatureResource:
    def on_post(self, req, resp):
        file = req.get_param("file")
        resouce_response_api(resp=resp, data=services.upload_signature_user(file=file, user_id=req.context['user']['id']))

class AdminFileResource:
    def on_post(self, req, resp):
        file = req.get_param("file")
        resouce_response_api(resp=resp, data=services.upload_file_admin(file=file, user_id=req.context['user']['id']))
