from entitas.user_chat import services
from util.entitas_util import generate_filters_resource, resouce_response_api

class UserChatResources:
    def on_get(self, req, resp, class_id):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_user_chat_db_with_pagination(
            class_id, page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)
    def on_post(self, req, resp, class_id):
        resouce_response_api(resp=resp, data=services.insert_user_chat_db(class_id, json_object=req.media))

class UserChatWithIdResources():
    def on_put(self, req, resp, user_chat_id: int, class_id: int):
        body = req.media
        body["id"] = int(user_chat_id)
        resouce_response_api(resp=resp, data=services.update_user_chat_chat_db(json_object=body, class_id=class_id))

    def on_delete(self, req, resp, user_chat_id: int, class_id: int):
        resouce_response_api(resp=resp, data=services.delete_user_chat_chat_by_id(id=int(user_chat_id), class_id=int(class_id)))