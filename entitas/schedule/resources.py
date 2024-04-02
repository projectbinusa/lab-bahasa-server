from entitas.schedule import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class ScheduleResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_schedule_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.insert_schedule_db(json_object=req.media))


class ScheduleWithIdResource:
    def on_get(self, req, resp, schedule_id: int):
        resouce_response_api(resp=resp, data=services.find_schedule_db_by_id(id=int(schedule_id)))

    def on_put(self, req, resp, schedule_id: int):
        body = req.media
        body["id"] = int(schedule_id)
        resouce_response_api(resp=resp, data=services.update_schedule_db(json_object=body))

    def on_delete(self, req, resp, schedule_id: int):
        resouce_response_api(resp=resp, data=services.delete_schedule_by_id(id=int(schedule_id)))

class UserCalendarResource:
    def on_get(self, req, resp):
        year = req.get_param("year", required=False, default='')
        month = req.get_param("month", required=False, default='')
        resouce_response_api(resp=resp, data=services.get_calendar(year=year, month=month, user_id=req.context['user']['id']))

class UserMyTrainingResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_mytraining_student(
            user_id=req.context['user']['id'], page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

class AdminCalendarResource:
    def on_get(self, req, resp):
        year = req.get_param("year", required=False, default='')
        month = req.get_param("month", required=False, default='')
        resouce_response_api(resp=resp, data=services.get_calendar(year=year, month=month, user_id=0))

class InstructurCalendarResource:
    def on_get(self, req, resp):
        year = req.get_param("year", required=False, default='')
        month = req.get_param("month", required=False, default='')
        resouce_response_api(resp=resp, data=services.get_calendar_instructur(year=year, month=month, user_id=req.context['user']['id']))

class InstructurMytrainingResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_mytraining_instructur(
            user_id=req.context['user']['id'], page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)
