from entitas.multiple_choice_questions import services
from util.entitas_util import generate_filters_resource, resouce_response_api
class MultipleChoiceQuestionsResources:
    def on_get(self, req, resp, class_id: int):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['question_text'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        filters.append({'field': 'class_id', 'value': class_id})
        data, pagination = services.get_services_db_with_pagination(
            page=page, class_id=class_id, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp, class_id: int):
        body = req.media  # Pastikan payload yang diterima adalah daftar objek JSON
        # if not isinstance(body, list):
        #     raise falcon.HTTPBadRequest(description="Payload harus berupa daftar pertanyaan.")
        print("user_id => ", req.context['user']['id'])
        resouce_response_api(
            resp=resp,
            data=services.insert_services_db(json_objects=body, user_id=req.context["user"]["id"], class_id=class_id,
                                             user_name=req.context["user"]["name"])
        )

class MultipleChoiceQuestionsWithByIdResources:
    def on_get(self, req, resp, multiple_questions_id: int, class_id):
        resouce_response_api(resp=resp, data=services.find_services_db_by_id(class_id=class_id, id=multiple_questions_id))

    def on_put(self, req, resp, class_id: int, multiple_questions_id: int):
        body = req.media
        print("user_id => ", req.context['user']['id'])
        resouce_response_api(
            resp=resp,
            data=services.update_service_db(json_object=body, user_id=req.context['user']['id'], class_id=class_id,
                                            user_name=req.context['user']['name'], id=int(multiple_questions_id))
        )

    def on_delete(self, req, resp, multiple_questions_id: int, class_id: int):
        resouce_response_api(resp=resp, data=services.delete_services_by_id(id=int(multiple_questions_id), class_id=int(class_id)))
