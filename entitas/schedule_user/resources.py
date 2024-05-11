from entitas.schedule_user import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class ScheduleUserResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_schedule_user_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.insert_schedule_user_db(json_object=req.media))


class ScheduleUserWithIdResource:
    def on_get(self, req, resp, schedule_user_id: int):
        resouce_response_api(resp=resp, data=services.find_schedule_user_for_student_by_id(schedule_id=int(schedule_user_id), user_id=req.context['user']['id']))

    def on_put(self, req, resp, schedule_user_id: int):
        body = req.media
        body["id"] = int(schedule_user_id)
        resouce_response_api(resp=resp, data=services.update_schedule_user_db(json_object=body))

    def on_delete(self, req, resp, schedule_user_id: int):
        resouce_response_api(resp=resp, data=services.delete_schedule_user_by_id(id=int(schedule_user_id)))


class ScheduleUserByScheduleResource:
    def on_get(self, req, resp, schedule_id):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name', 'confirmed'])
        filters.append({"field": "schedule_id", "value": int(schedule_id)})
        filters.append({"field": "is_deleted", "value": False})

        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_schedule_user_by_schedule_id_user(
            schedule_id=schedule_id, page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp, schedule_id):
        body = req.media
        resouce_response_api(resp=resp,
                             data=services.insert_schedule_user_db_by_schedule_id(schedule_id, json_object=body))

class ScheduleUserByIdWithScheduleIdResource:
    def on_put(self,req,resp, schedule_id: int, user_id: int):
        body = req.media
        resouce_response_api(resp=resp, data=services.update_schedule_user_by_schedule_id(schedule_id= schedule_id, user_id= user_id, json_object=body))

    def on_delete(self, req, resp, schedule_id: int, user_id: int):
        resouce_response_api(resp=resp,
                             data=services.delete_schedule_user_by_schedule_id(schedule_id, user_id))

class InstructurCalendarScheduleParticipantResource:
    def on_get(self, req, resp, schedule_id: int):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        filters.append({'field': 'schedule_id', 'value': int(schedule_id)})
        filters.append({'field': 'instructur_id', 'value': req.context['user']['id']})
        data, pagination = services.get_schedule_user_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

class InstructurCalendarScheduleParticipantGenerateCertificateResource:
    def on_post(self, req, resp, schedule_id: int):
        filters=[]
        filters.append({'field': 'schedule_id', 'value': int(schedule_id)})
        filters.append({'field': 'instructur_id', 'value': req.context['user']['id']})
        resouce_response_api(resp=resp, data=services.schedule_user_generate_certificate(filters=filters))

class InstructurCalendarScheduleParticipantScoreResource:
    def on_put(self, req, resp, schedule_id: int, schedule_user_id: int):
        body = req.media
        resouce_response_api(resp=resp, data=services.update_schedule_user_for_instructur(
            schedule_id=int(schedule_id),
            schedule_user_id=int(schedule_user_id),
            instructur_id=req.context['user']['id'], score=body['score']))

    def on_get(self, req, resp, schedule_id: int, schedule_user_id: int):
        resouce_response_api(resp=resp, data=services.get_schedule_user_for_instructur(
            schedule_id=int(schedule_id),
            schedule_user_id=int(schedule_user_id)))

class InstructurCalendarScheduleParticipantConfirmedResource:
    def on_put(self, req, resp, schedule_id: int):
        body = req.media
        resouce_response_api(resp=resp, data=services.update_schedule_user_for_confirmed_user(
            schedule_id=int(schedule_id),
            user_id=req.context['user']['id'],
            confirmed=body['confirmed']))

class ScheduleUserWithIdFeedbackResource:
    def on_put(self, req, resp, schedule_user_id: int):
        body = req.media
        resouce_response_api(resp=resp, data=services.update_schedule_user_for_feeback(id=int(schedule_user_id), user_id=req.context['user']['id'], kritik=body['kritik'], saran=body['saran']))
#
# class AdminScheduleUserWithIdFeedbackResource:
#
#     def on_get(self, req, resp, schedule_id: int, user_id: int):
#         resouce_response_api(resp=resp,
#                              data=services.find_schedule_user_by_schedule_id(schedule_id=int(schedule_id), user_id=int(user_id)))
#
#     def on_put(self, req, resp, schedule_id: int, user_id: int):
#         body = req.media
#         # body["schedule_id"] = int(schedule_id)
#         # body["user_id"] = int(user_id)
#         resouce_response_api(resp=resp,
#                              data=services.update_schedule_instructur_by_schedule_id(schedule_id=schedule_id, id=user_id, json_object=body))
#
#     def on_delete(self, req, resp, schedule_id: int, user_id: int):
#         resouce_response_api(resp=resp,
#                              data=services.delete_schedule_instructur_by_schedule_id(schedule_id, user_id))
#
