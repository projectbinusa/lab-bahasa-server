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

    def on_get(self, req, resp, class_id):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['content'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_chat_db_with_pagination(
            class_id, page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)


class UserChatResource:
    def on_get(self, req, resp, user_id):
        sender_id = req.get_param("sender_id", required=False)
        # user_id = req.context["user"]["id"]
        resouce_response_api(resp=resp, data=services.get_messages_for_user_service(user_id, sender_id))


# class ChatResource:
#     def on_post(self, req, resp):
#         json_object = req.media
#         try:
#             if json_object['is_group']:
#                 chat = services.start_group_chat(json_object['user_ids'], json_object=json_object)
#             else:
#                 chat = services.start_private_chat(json_object['user_ids'], json_object=json_object)
#             resouce_response_api(resp=resp, data={'chat_id': chat.id})
#         except ValueError as e:
#             resp.status = falcon.HTTP_400
#             resp.media = {'error': str(e)}
#         except Exception as e:
#             # Log the error for debugging
#             print(f"Unexpected error: {e}")
#             resp.status = falcon.HTTP_500
#             resp.media = {'error': 'Internal Server Error'}

    # def on_get(self, req, resp):
    #     filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
    #     page = int(req.get_param("page", required=False, default=1))
    #     limit = int(req.get_param("limit", required=False, default=9))
    #     data, pagination = services.get_chat_db_with_pagination(
    #         page=page, limit=limit, filters=filters
    #     )
    #     resouce_response_api(resp=resp, data=data, pagination=pagination)
    # def on_post(self, req, resp):
    #     json_object = req.media
    #     resouce_response_api(resp=resp, data=services.insert_chat_db(json_object=json_object))

        # except ValueError as e:
        #     resouce_response_api(resp=resp, data={'error': str(e)}, status=falcon.HTTP_400)
        # except Exception as e:
        #     # Log the error for debugging
        #     print(f"Unexpected error: {e}")
        #     resouce_response_api(resp=resp, data={'error': 'Internal Server Error'}, status=falcon.HTTP_500)

    # def on_get(self, req, resp, user_id):
    #     try:
    #         chats = services.get_user_chats(user_id)
    #         resp.media = {
    #             'chats': [{
    #                 'id': chat.id,
    #                 'name': chat.name,
    #                 'is_group': chat.is_group,
    #                 'users': [user.to_json() for user in chat.users],
    #                 'last_message': chat.last_message.to_json() if chat.last_message else None
    #             } for chat in chats]
    #         }
    #     except ValueError as e:
    #         resp.status = falcon.HTTP_400
    #         resp.media = {'error': str(e)}

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