from entitas.assignment_user import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class AssignmentUserResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_assignment_user_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.insert_assignment_user_db(json_object=req.media))


class AssignmentUserWithIdResource:
    def on_get(self, req, resp, assignment_user_id: int):
        resouce_response_api(resp=resp, data=services.find_assignment_user_db_by_id(id=int(assignment_user_id)))

    def on_put(self, req, resp, assignment_user_id: int):
        body = req.media
        body["id"] = int(assignment_user_id)
        resouce_response_api(resp=resp, data=services.update_assignment_user_db(json_object=body))

    def on_delete(self, req, resp, assignment_user_id: int):
        resouce_response_api(resp=resp, data=services.delete_assignment_user_by_id(id=int(assignment_user_id)))

class UserCalendarScheduleAssignmentByAssignmentIdResource:
    def on_get(self, req, resp, schedule_id: int, assignment_id: int):
        resouce_response_api(resp=resp, data=services.find_assignment_user_by_id(assignment_id=int(assignment_id), user_id=req.context['user']['id']))

    def on_post(self, req, resp, schedule_id: int, assignment_id: int):
        file = req.get_param("file")
        body = {}
        body["assignment_id"] = int(assignment_id)
        body['description'] = req.get_param("description")
        body['schedule_id'] = int(schedule_id)
        resouce_response_api(resp=resp, data=services.update_assignment_user(file=file, json_object=body, user_id=req.context['user']['id'], assignment_id=int(assignment_id)))

class InstructurCalendarScheduleAssignmentByAssignmentIdUserResource:
    def on_get(self, req, resp, schedule_id: int, assignment_id: int):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        filters.append({'field': 'schedule_id', 'value': int(schedule_id)})
        filters.append({'field': 'assignment_id', 'value': int(assignment_id)})
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_assignment_user_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

class InstructurCalendarScheduleAssignmentByAssignmentIdUserIdResource:
    def on_put(self, req, resp, schedule_id: int, assignment_id: int, assignment_user_id: int):
        body = req.media
        resouce_response_api(resp=resp, data=services.assignment_user_update_score(
            id=int(assignment_user_id), instructur_id=req.context['user']['id'], score=body['score'], comment=body['comment']))

    def on_get(self, req, resp, schedule_id: int, assignment_id: int, assignment_user_id: int):
        resouce_response_api(resp=resp, data=services.preview_assignment_user_for_instructur(
            id=int(assignment_user_id), instructur_id=req.context['user']['id']))
