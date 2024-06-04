import json

import falcon

from entitas.message_chat import services
from util.entitas_util import generate_filters_resource, resouce_response_api

class MessageChatResource:
    def on_post(self, req, resp):
        json_object = req.media
        try:
            message = services.send_message(json_object['sender_id'], json_object['chat_id'], json_object['content'])
            resp.media = {'message_id': message.id}
        except ValueError as e:
            resp.status = falcon.HTTP_400
            resp.media = {'error': str(e)}
        except Exception as e:
            # Log the error for debugging
            print(f"Unexpected error: {e}")
            resp.status = falcon.HTTP_500
            resp.media = {'error': 'Internal Server Error'}

    def on_get(self, req, resp, chat_id):
        try:
            messages = services.get_chat_messages(chat_id)
            resp.media = {
                'messages': [{
                    'id': message.id,
                    'sender_id': message.sender_id,
                    'content': message.content,
                    'timestamp': message.timestamp.isoformat()
                } for message in messages]
            }
        except ValueError as e:
            resp.status = falcon.HTTP_400
            resp.media = {'error': str(e)}

    # def on_get(self, req, resp):
    #     filters = generate_filters_resource(req=req, params_int=['id'], params_string=['content'])
    #     page = int(req.get_param("page", required=False, default=1))
    #     limit = int(req.get_param("limit", required=False, default=9))
    #     data, pagination = services.get_message_db_with_pagination(
    #         page=page, limit=limit, filters=filters
    #     )
    #     resouce_response_api(resp=resp, data=data, pagination=pagination)
    # def on_post(self, req, resp):
    #     json_object = req.media
    #     resouce_response_api(resp=resp, data=services.insert_message_chat_db(json_object=json_object))

class MessageChatWithIdResource:
    def on_put(self, req, resp, message_chat_id: int):
        body = req.media
        body["id"] = int(message_chat_id)
        resouce_response_api(resp=resp, data=services.update_message_chat_db(json_object=body))

    def on_delete(self, req, resp, message_chat_id: int):
        resouce_response_api(resp=resp, data=services.delete_message_chat_by_id(id=int(message_chat_id)))