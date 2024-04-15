from entitas.announcement import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class AnnouncementResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_announcement_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.insert_announcement_db(json_object=req.media))


class AnnouncementWithIdResource:
    def on_get(self, req, resp, announcement_id: int):
        resouce_response_api(resp=resp, data=services.find_announcement_db_by_id(id=int(announcement_id)))

    def on_put(self, req, resp, announcement_id: int):
        body = req.media
        body["id"] = int(announcement_id)
        resouce_response_api(resp=resp, data=services.update_announcement_db(json_object=body))

    def on_delete(self, req, resp, announcement_id: int):
        resouce_response_api(resp=resp, data=services.delete_announcement_by_id(id=int(announcement_id)))

class AnnouncementWithIdPublishResource:
    def on_put(self, req, resp, announcement_id: int):
        resouce_response_api(resp=resp, data=services.update_announcement_for_publish_by_id(id=int(announcement_id), is_published=True))

class AnnouncementWithIdUnPublishResource:
    def on_put(self, req, resp, announcement_id: int):
        resouce_response_api(resp=resp, data=services.update_announcement_for_publish_by_id(id=int(announcement_id), is_published=False))

class AnnouncementStudentResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        filters.append({'field': 'is_published', 'value': True})
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_announcement_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

class AnnouncementInstructurResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        filters.append({'field': 'is_published', 'value': True})
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_announcement_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)