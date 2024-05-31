from entitas.message_chat import services
from util.entitas_util import generate_filters_resource, resouce_response_api

class MessageChatResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['content'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_message_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)
    def on_post(self, req, resp):
        json_object = req.media
        resouce_response_api(resp=resp, data=services.insert_message_chat_db(json_object=json_object))

class MessageChatWithIdResource:
    def on_put(self, req, resp, message_chat_id: int):
        body = req.media
        body["id"] = int(message_chat_id)
        resouce_response_api(resp=resp, data=services.update_message_chat_db(json_object=body))

    def on_delete(self, req, resp, message_chat_id: int):
        resouce_response_api(resp=resp, data=services.delete_message_chat_by_id(id=int(message_chat_id)))