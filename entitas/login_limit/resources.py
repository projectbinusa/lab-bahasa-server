from entitas.login_limit import services
from util.entitas_util import generate_filters_resource, resouce_response_api

# resources
class LoginLimitResource:
    def on_get(self, req, resp, class_id):
        filters = generate_filters_resource(req=req, params_int=['id'])
        filters.append({'field': 'class_id', 'value': class_id})
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_login_limits_by_class_id(
            class_id=class_id, page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp, class_id):
        resouce_response_api(resp=resp,
                             data=services.insert_login_limits_db_by_class_id(class_id, json_object=req.media))


class LoginLimitWithIdResource:
    # def on_get(self, req, resp, class_id: int, user_id: int, log_book_id: int):
    #     resouce_response_api(resp=resp,
    #                          data=services.find_log_book_by_class_id(class_id=int(class_id), user_id=int(user_id), log_book_id=int(log_book_id)))

    def on_put(self, req, resp, class_id: int, login_limits_id: int):
        # body["id"] = int(log_book_id)
        resouce_response_api(resp=resp,
                             data=services.update_login_limits_by_class_id(id=login_limits_id, json_object=req.media, class_id=class_id))

    def on_delete(self, req, resp, class_id: int, login_limits_id: int):
        resouce_response_api(resp=resp,
                             data=services.delete_login_limits_by_class_id(class_id, login_limits_id))

    def on_get(self, req, resp, class_id: int, login_limits_id: int):
        log_book_data = services.find_login_limits_by_ids(
            class_id=int(class_id),
            login_limits_id=int(login_limits_id),
        )
        resouce_response_api(resp=resp, data=log_book_data)
