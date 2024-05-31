from entitas.chat import services
from util.entitas_util import generate_filters_resource, resouce_response_api

class ChatResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_chat_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)
    def on_post(self, req, resp):
        json_object = req.media
        resouce_response_api(resp=resp, data=services.insert_chat_db(json_object=json_object))

class ChatWithIdResource:
    def on_put(self, req, resp, chat_id: int):
        body = req.media
        body["id"] = int(chat_id)
        resouce_response_api(resp=resp, data=services.update_chat_db(json_object=body))

    def on_delete(self, req, resp, chat_id: int):
        resouce_response_api(resp=resp, data=services.delete_chat_by_id(id=int(chat_id)))