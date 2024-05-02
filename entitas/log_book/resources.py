from entitas.log_book import services
from util.entitas_util import generate_filters_resource, resouce_response_api

class LogBookResource:
    def on_get(self, req, resp, schedule_id):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['user_name'])
        filters.append({'field': 'schedule_id', 'value': schedule_id})

        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_log_book_by_schedule_id(
            schedule_id=schedule_id, page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp, schedule_id):
        bukti_start = req.get_param("bukti_start")
        bukti_end = req.get_param("bukti_end")
        periode_date = req.get_param("periode_date")
        periode_start_time = req.get_param("periode_start_time")
        periode_end_time = req.get_param("periode_end_time")
        topic = req.get_param("topic")
        materi = req.get_param("materi")
        training_proof_start = req.get_param("training_proof_start")
        user_name = req.get_param("user_name")
        body = {}
        body["periode_date"] = periode_date
        body["periode_start_time"] = periode_start_time
        body["periode_end_time"] = periode_end_time
        body["topic"] = topic
        body["materi"] = materi
        body["training_proof_start"] = training_proof_start
        body["user_name"] = user_name
        body["user_id"] = req.context["user"]["id"]
        resouce_response_api(resp=resp,
                             data=services.insert_log_book_db_by_schedule_id(schedule_id, json_object=body,
                                                                             bukti_start=bukti_start,
                                                                             bukti_end=bukti_end))


class LogBookWithIdResource:
    # def on_get(self, req, resp, schedule_id: int, user_id: int, log_book_id: int):
    #     resouce_response_api(resp=resp,
    #                          data=services.find_log_book_by_schedule_id(schedule_id=int(schedule_id), user_id=int(user_id), log_book_id=int(log_book_id)))

    def on_put(self, req, resp, schedule_id: int, log_book_id: int):
        bukti_start = req.get_param("bukti_start")
        bukti_end = req.get_param("bukti_end")
        periode_date = req.get_param("periode_date")
        periode_start_time = req.get_param("periode_start_time")
        periode_end_time = req.get_param("periode_end_time")
        topic = req.get_param("topic")
        materi = req.get_param("materi")
        training_proof_start = req.get_param("training_proof_start")
        user_name = req.get_param("user_name")
        body = {}
        body["periode_date"] = periode_date
        body["periode_start_time"] = periode_start_time
        body["periode_end_time"] = periode_end_time
        body["topic"] = topic
        body["materi"] = materi
        body["training_proof_start"] = training_proof_start
        body["user_name"] = user_name
        # body["schedule_id"] = int(schedule_id)
        # body["user_id"] = int(user_id)
        body["user_id"] = req.context["user"]["id"]
        # body["id"] = int(log_book_id)
        resouce_response_api(resp=resp,
                             data=services.update_log_book_by_schedule_id(bukti_start=bukti_start, bukti_end=bukti_end,
                                                                          schedule_id=schedule_id,
                                                                          user_id=req.context['user']['id'],
                                                                          id=log_book_id, json_object=body))

    def on_delete(self, req, resp, schedule_id: int, log_book_id: int):
        resouce_response_api(resp=resp,
                             data=services.delete_log_book_by_schedule_id(schedule_id, log_book_id,
                                                                          user_id=req.context['user']['id']))

    def on_get(self, req, resp, schedule_id: int, log_book_id: int):
        user_id = req.context['user']['id']
        log_book_data = services.find_log_book_by_ids(
            schedule_id=int(schedule_id),
            log_book_id=int(log_book_id),
            user_id=user_id
        )
        resouce_response_api(resp=resp, data=log_book_data)
