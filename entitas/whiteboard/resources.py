import falcon

from entitas.whiteboard import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class WhiteboardResource:
    def on_get(self, req, resp, class_id):
        filters = generate_filters_resource(req=req, params_int=['id'])
        filters.append({'field': 'class_id', 'value': class_id})
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_list_by_class_id(
            class_id=class_id, page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp, class_id):
        body = req.media
        user_ids = body.get('user_id')

        if not isinstance(user_ids, list):
            resp.status = falcon.HTTP_400
            resp.media = {"error": "user_id must be a list"}
            return

        resouce_response_api(
            resp=resp,
            data=services.create_whiteboard_service(class_id=class_id, user_ids=user_ids, json_object=body)
        )


class WhiteboardWithIdResource:
    def on_put(self, req, resp, whiteboard_id: int, class_id: int):
        body = req.media
        resouce_response_api(resp=resp,
                             data=services.update_whiteboard_by_class_id(id=int(whiteboard_id),
                                                                         json_object=body,
                                                                         class_id=class_id
                                                                         ))

    def on_delete(self, req, resp, whiteboard_id: int, class_id: int):
        resouce_response_api(resp=resp,
                             data=services.delete_whiteboard_by_class_id(class_id=class_id, id=int(whiteboard_id)))

    def on_get(self, req, resp, class_id: int, whiteboard_id: int):
        log_book_data = services.find_whiteboard_by_class_id(
            class_id=int(class_id),
            whiteboard_id=int(whiteboard_id),
        )
        resouce_response_api(resp=resp, data=log_book_data)
