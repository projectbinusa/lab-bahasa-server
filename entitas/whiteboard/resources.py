from entitas.whiteboard import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class WhiteboardResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id', 'class_id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))

        class_id = req.get_param("class_id", required=False)
        if class_id:
            data, pagination = services.get_whiteboard_db_with_pagination_by_class(
                class_id=int(class_id), page=page, limit=limit, filters=filters
            )
        else:
            data, pagination = services.get_whiteboard_db_with_pagination(
                page=page, limit=limit, filters=filters
            )

        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp, class_id):
        resouce_response_api(resp=resp,
                             data=services.create_whiteboard_service(class_id, json_object=req.media))


class WhiteboardWithIdResource:
    def on_put(self, req, resp, management_name_list_id: int, class_id: int):
        body = req.media
        resouce_response_api(resp=resp,
                             data=services.update_whiteboard_by_class_id(id=int(management_name_list_id),
                                                                         json_object=body,
                                                                         class_id=class_id
                                                                         ))

    def on_delete(self, req, resp, whiteboard_id: int, class_id: int):
        resouce_response_api(resp=resp,
                             data=services.delete_whiteboard_by_class_id (class_id, whiteboard_id))

    def on_get(self, req, resp, class_id: int, whiteboard_id: int):
        log_book_data = services.find_whiteboard_by_class_id(
            class_id=int(class_id),
            whiteboard_id=int(whiteboard_id),
        )
        resouce_response_api(resp=resp, data=log_book_data)
