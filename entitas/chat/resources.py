import json

import falcon

from entitas.chat import services
from entitas.chat.services import get_chat_db_with_pagination_by_group_id
from util.entitas_util import generate_filters_resource, resouce_response_api


class ChatResource:
    def on_post(self, req, resp, class_id):
        try:
            gambar = req.get_param("gambar")
            content = req.get_param("content")
            is_group = req.get_param("is_group")

            if not content:
                raise ValueError("Content is required")

            body = {
                "content": content,
                "is_group": is_group,
                "sender_id": req.context["user"]["id"],
            }

            if gambar:
                body["gambar"] = gambar

            # Log payload yang diterima
            print(f"Received payload: {body}")

            resouce_response_api(
                resp=resp,
                data=services.insert_message_service(
                    class_id=class_id,
                    json_object=body,
                    gambar=gambar
                )
            )

        except Exception as e:
            # Log kesalahan dan tangani error 500
            print(f"Error in ChatResource.on_post: {e}")
            resp.status = falcon.HTTP_500
            resp.body = json.dumps({"error": str(e)})


class ChatByClassIdAndSenderIdAndReceiverId:
    def on_get(self, req, resp, class_id: int, receiver_id: int):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['content'])
        print("class_id in resources ==>", class_id)
        print("receiver_id in resources ==>", receiver_id)
        print("sender_id in resources ==>", req.context['user']['id'])
        filters.append({"field": "class_id", "value": int(class_id)})
        filters.append({"field": "sender_id", "value": req.context['user']['id']})
        filters.append({"field": "receiver_id", "value": int(receiver_id)})
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_chat_db_with_pagination_sender_id_and_receiver_id(
            class_id=class_id, receiver_id=receiver_id, sender_id=req.context['user']['id'], page=page, limit=limit, filters=filters
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
        receiver_id = int(req.get_param("receiver_id"))
        is_group = req.get_param("is_group")
        body = {}
        body["content"] = content
        body["receiver_id"] = receiver_id
        body["is_group"] = is_group
        body["id"] = int(chat_id)
        resouce_response_api(resp=resp, data=services.update_chat_db(json_object=body, gambar=gambar, class_id=class_id, receiver_id=receiver_id))

    def on_delete(self, req, resp, chat_id: int, class_id: int, receiver_id: int):
        resouce_response_api(resp=resp, data=services.delete_chat_by_id(id=int(chat_id), class_id=int(class_id), receiver_id=int(receiver_id)))


class ChatByClassIdAndTopicChatIdResource:
    def on_get(self, req, resp, class_id: int, topic_chat_id: int):
        # print(f"Request Path: {req.path}")
        # print(f"Request Params: {req.params}")
        # print(f"Received class_id: {class_id}, topic_chat_id: {topic_chat_id}")

        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['content'])
        filters.append({'field': 'class_id', 'value': class_id})
        filters.append({'field': 'topic_chat_id', 'value': topic_chat_id})
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))

        data, pagination = services.get_chat_db_with_pagination_by_topic_chat_id(
            class_id, topic_chat_id, page=page, limit=limit, filters=filters
        )

        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp, class_id: int, topic_chat_id: int):
        # Ambil data dari body JSON
        body = req.media

        # Ambil file gambar dari form data
        gambar = req.get_param("gambar")

        # Tambahkan sender_id ke body
        body["sender_id"] = req.context["user"]["id"]

        # Panggil service untuk menyimpan pesan grup
        try:
            resouce_response_api(resp=resp,
                                 data=services.insert_message_group_service(class_id, topic_chat_id, json_object=body,
                                                                            gambar=gambar))
        except Exception as e:
            print("Error while inserting message:", e)
            resp.status = falcon.HTTP_500  # Atur status response sesuai kebutuhan
            resp.media = {"error": "Failed to insert message"}  # Response jika terjadi kesalahan


class ChatByClassIdAndGroupIdResource:
    def on_get(self, req, resp, class_id: int, group_id: int):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['content'])
        filters.append({'field': 'class_id', 'value': class_id})
        filters.append({'field': 'group_id', 'value': group_id})
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=100))

        data, pagination = services.get_chat_db_with_pagination_by_group_id(
            class_id=class_id, group_id=group_id, page=page, limit=limit, filters=filters
        )

        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp, class_id: int, group_id: int):
        gambar = req.get_param("gambar")
        content = req.get_param("content")
        is_group = req.get_param("is_group")

        body = {
            "content": content,
            "is_group": is_group,
            "sender_id": req.context["user"]["id"]
        }
        if gambar is not None:
            body["gambar"] = gambar
        if content is not None:
            body["content"] = content

        resouce_response_api(resp=resp, data=services.insert_message_group_service(class_id, group_id, json_object=body,
                                                                                   gambar=gambar))


class ChatByClassIdAndGroupIdWithIdResource:
    def on_put(self, req, resp, chat_id: int, class_id: int, group_id: int):
        gambar = req.get_param("gambar")
        sender_id = req.get_param("sender_id")
        content = req.get_param("content")
        receiver_id = int(req.get_param("receiver_id"))
        is_group = req.get_param("is_group")
        body = {}
        body["content"] = content
        body["receiver_id"] = receiver_id
        body["sender_id"] = sender_id
        body["is_group"] = is_group
        body["id"] = int(chat_id)
        body["class_id"] = class_id
        body["group_id"] = group_id
        resouce_response_api(resp=resp,
                             data=services.update_chat_by_group_id_and_class_id(json_object=body, gambar=gambar,
                                                                                class_id=class_id, group_id=group_id))

    def on_delete(self, req, resp, chat_id: int, group_id: int, class_id: int):
        resouce_response_api(resp=resp, data=services.delete_chat_by_group_id_and_class_id(id=int(chat_id), group_id=int(group_id), class_id=int(class_id)))

class ChatByClassIdAndByGroupIdResource:
    def on_get(self, req, resp, chat_id: int, group_id: int, class_id: int):
        chat_data = services.get_chat_by_id_and_by_group_id_and_by_class_id(
            id=int(chat_id),
            group_id=int(group_id),
            class_id=int(class_id)
        )
        if chat_data:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps({"chat_data": chat_data.to_json()})
        else:
            resp.status = falcon.HTTP_404
            resp.body = json.dumps({"message": "Chat not found"})
