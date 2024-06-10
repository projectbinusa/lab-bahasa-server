import falcon

from entitas.anggota_group import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class AnggotaGroupResources:
    def on_get(self, req, resp, group_id, class_id):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['role'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_group_member_by_group_id_with_pagination(
            group_id, class_id, page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp, group_id, class_id):
        json_object = req.media
        resouce_response_api(resp=resp, data=services.create_member_db(group_id, class_id, json_object=json_object))


class AnggotaGroupWithIdResources:
    def on_delete(self, req, resp, anggota_group_id: int, class_id: int):
        resouce_response_api(resp=resp, data=services.delete_anggota_group_chat_by_id(id=int(anggota_group_id),
                                                                                      class_id=int(class_id)))


class GroupDeletionResources:
    def on_delete(self, req, resp, group_id, class_id, anggota_group_id):
        try:
            if anggota_group_id is None:
                raise ValueError("anggota_group_id is required")

            result = services.delete_group_by_anggota_group_id_and_class_id(
                group_id=int(group_id), class_id=int(class_id), anggota_group_id=int(anggota_group_id)
            )
            resouce_response_api(resp=resp, data=result)
        except ValueError as e:
            resp.status = falcon.HTTP_400  # Bad Request
            resouce_response_api(resp=resp, data={"error": str(e)})
        except Exception as e:
            resp.status = falcon.HTTP_500  # Internal Server Error
            resouce_response_api(resp=resp, data={"error": str(e)})
