from entitas.schedule_instructur import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class ScheduleInstructurResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_schedule_instructur_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.insert_schedule_instructur_db(json_object=req.media))


class ScheduleInstructurByScheduleResource:
    def on_get(self, req, resp, schedule_id):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        filters.append({'field': 'schedule_id', 'value': schedule_id})
        filters.append({'field': 'is_deleted', 'value': False})

        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_schedule_instructur_by_schedule_id(
            schedule_id=schedule_id, page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp, schedule_id):
        body = req.media
        resouce_response_api(resp=resp,
                             data=services.insert_schedule_instructur_db_by_schedule_id(schedule_id, json_object=body))


class ScheduleInstructurWithIdResource:
    def on_get(self, req, resp, schedule_instructur_id: int):
        resouce_response_api(resp=resp, data=services.find_schedule_instructur_db_by_id(id=int(schedule_instructur_id)))

    def on_put(self, req, resp, schedule_instructur_id: int):
        body = req.media
        body["id"] = int(schedule_instructur_id)
        resouce_response_api(resp=resp, data=services.update_schedule_instructur_db(json_object=body))

    def on_delete(self, req, resp, schedule_instructur_id: int):
        resouce_response_api(resp=resp, data=services.delete_schedule_instructur_by_id(id=int(schedule_instructur_id)))


class ScheduleInstructurByIdWithScheduleIdResource:
    def on_get(self, req, resp, schedule_id: int, user_id: int):
        resouce_response_api(resp=resp,
                             data=services.find_schedule_instructur_by_schedule_id(schedule_id=int(schedule_id), user_id=int(user_id)))

    def on_put(self, req, resp, schedule_id: int, user_id: int):
        body = req.media
        # body["schedule_id"] = int(schedule_id)
        # body["user_id"] = int(user_id)
        resouce_response_api(resp=resp,
                             data=services.update_schedule_instructur_by_schedule_id(schedule_id=schedule_id, id=user_id, json_object=body))

    def on_delete(self, req, resp, schedule_id: int, user_id: int):
        resouce_response_api(resp=resp,
                             data=services.delete_schedule_instructur_by_schedule_id(schedule_id, user_id))
