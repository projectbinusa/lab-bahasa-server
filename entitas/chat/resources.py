import json

import falcon

from entitas.chat import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class ChatResource:
    def on_post(self, req, resp, class_id):
        gambar = req.get_param("gambar")
        content = req.get_param("content")
        receiver_id = req.get_param("receiver_id")
        is_group = req.get_param("is_group")
        body = {}
        body["content"] = content
        body["receiver_id"] = receiver_id
        body["is_group"] = is_group
        body["sender_id"] = req.context["user"]["id"]
        resouce_response_api(resp=resp, data=services.insert_message_service(class_id, json_object=body, gambar=gambar))



class ChatByClassIdAndSenderIdAndReceiverId:
    def on_get(self, req, resp, class_id, receiver_id):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['content'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_chat_db_with_pagination_sender_id_and_receiver_id(
            class_id, sender_id=req.context['user']['id'], receiver_id=receiver_id, page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)


class UserChatResource:
    def on_get(self, req, resp, user_id):
        sender_id = req.get_param("sender_id", required=False)
        # user_id = req.context["user"]["id"]
        resouce_response_api(resp=resp, data=services.get_messages_for_user_service(user_id, sender_id))

class ChatWithIdResource:
    def on_put(self, req, resp, chat_id: int, class_id: int):
        gambar = req.get_param("gambar")
        content = req.get_param("content")
        receiver_id = req.get_param("receiver_id")
        is_group = req.get_param("is_group")
        body = {}
        body["content"] = content
        body["receiver_id"] = receiver_id
        body["is_group"] = is_group
        body["id"] = int(chat_id)
        resouce_response_api(resp=resp, data=services.update_chat_db(json_object=body, gambar=gambar, class_id=class_id))

    def on_delete(self, req, resp, chat_id: int, class_id: int):
        resouce_response_api(resp=resp, data=services.delete_chat_by_id(id=int(chat_id), class_id=int(class_id)))