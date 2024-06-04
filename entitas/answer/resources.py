from entitas.answer import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class AnswerResource:
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
        resouce_response_api(resp=resp,
                             data=services.create_answer_service(class_id, json_object=req.media, user_id=req.context["user"]["id"]))


class AnswerWithIdResource:
    def on_put(self, req, resp, answer_id: int, class_id: int):
        body = req.media
        resouce_response_api(resp=resp,
                             data=services.update_answer_by_class_id(id=int(answer_id),
                                                                         json_object=body,
                                                                         class_id=class_id
                                                                         ))

    def on_delete(self, req, resp, answer_id: int, class_id: int):
        resouce_response_api(resp=resp,
                             data=services.delete_answer_by_class_id(class_id=class_id, id=int(answer_id)))

    def on_get(self, resp, class_id: int, answer_id: int):
        log_book_data = services.find_answer_by_class_id(
            class_id=int(class_id),
            answer_id=int(answer_id),
        )
        resouce_response_api(resp=resp, data=log_book_data)

# class AnswerByClassIdAndUserIdResource:
#     def on_get(self, req, resp, class_id):
#         filters = generate_filters_resource(req=req, params_int=['id'])
#         filters.append({'field': 'class_id', 'value': class_id})
#         filters.append({'field': 'user_id', 'value': req.context["user"]["id"]})
#         page = int(req.get_param("page", required=False, default=1))
#         limit = int(req.get_param("limit", required=False, default=9))
#         data, pagination = services.get_answer_by_class_id_and_user_id(
#             class_id=class_id, user_id=req.context["user"]["id"], page=page, limit=limit, filters=filters
#         )
#         resouce_response_api(resp=resp, data=data, pagination=pagination)