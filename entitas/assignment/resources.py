from entitas.assignment import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class AssignmentResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_assignment_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.insert_assignment_db(json_object=req.media))


class AssignmentWithIdResource:
    def on_get(self, req, resp, assignment_id: int):
        resouce_response_api(resp=resp, data=services.find_assignment_db_by_id(id=int(assignment_id)))

    def on_put(self, req, resp, assignment_id: int):
        body = req.media
        body["id"] = int(assignment_id)
        resouce_response_api(resp=resp, data=services.update_assignment_db(json_object=body))

    def on_delete(self, req, resp, assignment_id: int):
        resouce_response_api(resp=resp, data=services.delete_assignment_by_id(id=int(assignment_id)))

class InstructurCalendarScheduleAssignmentResource:
    def on_get(self, req, resp, schedule_id: int):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        filters.append({'field': 'schedule_id', 'value': int(schedule_id)})
        filters.append({'field': 'instructur_id', 'value': req.context['user']['id']})
        data, pagination = services.get_assignment_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)
    def on_post(self, req, resp, schedule_id: int):
        body=req.media
        body['schedule_id'] = int(schedule_id)
        body['instructur_id'] = req.context['user']['id']
        resouce_response_api(resp=resp, data=services.insert_assignment_instructur(json_object=body))

class InstructurCalendarScheduleAssignmentByAssignmentIdResource:
    def on_get(self, req, resp, schedule_id: int, assignment_id: int):
        resouce_response_api(resp=resp, data=services.find_assignment_instructur_by_id(id=int(assignment_id), instructur_id=req.context['user']['id']))

    def on_put(self, req, resp, schedule_id: int, assignment_id: int):
        body = req.media
        body["id"] = int(assignment_id)
        body["instructur_id"] = req.context['user']['id']
        resouce_response_api(resp=resp, data=services.update_assignment_instructur(json_object=body, instructur_id=req.context['user']['id']))
    #
    # def on_delete(self, req, resp, schedule_id: int, assignment_id: int):
    #     resouce_response_api(resp=resp, data=services.delete_assignment_instructur_by_id(id=int(assignment_id), instructur_id=req.context['user']['id']))