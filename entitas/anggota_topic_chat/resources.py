import falcon

from entitas.anggota_topic_chat import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class AnggotaTopicChatResources:
    def on_get(self, req, resp, topic_chat_id, class_id):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['role'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_member_by_topic_id_with_pagination(
            topic_chat_id, class_id, page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp, topic_chat_id, class_id):
        json_object = req.media
        resouce_response_api(resp=resp,
                             data=services.create_member_db(topic_chat_id, class_id, json_object=json_object))


class AnggotaTopicChatWithIdResources:
    def on_delete(self, req, resp, anggota_topic_chat_id: int, class_id: int):
        resouce_response_api(resp=resp, data=services.delete_anggota_topic_chat_by_id(id=int(anggota_topic_chat_id),
                                                                                      class_id=int(class_id)))


class TopicChatDeletionResources:
    def on_delete(self, req, resp, topic_chat_id, class_id, anggota_topic_chat_id):
        try:
            if anggota_topic_chat_id is None:
                raise ValueError("anggota_topic_chat_id is required")

            result = services.delete_topic_chat_by_anggota_topic_chat_id_and_class_id(
                topic_chat_id=int(topic_chat_id), class_id=int(class_id), anggota_topic_chat_id=int(anggota_topic_chat_id)
            )
            resouce_response_api(resp=resp, data=result)
        except ValueError as e:
            resp.status = falcon.HTTP_400  # Bad Request
            resouce_response_api(resp=resp, data={"error": str(e)})
        except Exception as e:
            resp.status = falcon.HTTP_500  # Internal Server Error
            resouce_response_api(resp=resp, data={"error": str(e)})
