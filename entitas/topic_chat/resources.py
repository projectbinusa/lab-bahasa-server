from entitas.topic_chat import services
from util.entitas_util import *


class TopicChatResources:
    def on_get(self, req, resp, class_id):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_topic_chat_db_with_pagination(
            class_id, page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp, class_id):
        json_object = req.media
        resouce_response_api(resp=resp, data=services.insert_topic_chat_db(class_id, json_object=json_object))


class TopicChatWithIdResources():
    def on_put(self, req, resp, topic_chat_id: int, class_id: int):
        body = req.media
        body["id"] = int(topic_chat_id)
        resouce_response_api(resp=resp, data=services.update_topic_chat_db(json_object=body, class_id=class_id))

    def on_delete(self, req, resp, topic_chat_id: int, class_id: int):
        resouce_response_api(resp=resp, data=services.delete_topic_chat_by_id(id=int(topic_chat_id), class_id=int(class_id)))
