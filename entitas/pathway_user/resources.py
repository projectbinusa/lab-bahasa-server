from entitas.pathway_user import services
from util.entitas_util import generate_filters_resource, resouce_response_api


class PathwayUserResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id','pathway_id','user_id'], params_string=['pathway_name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_pathway_user_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

class PathwayUserWithIdResource:
    def on_get(self, req, resp, pathway_user_id: int):
        resouce_response_api(resp=resp, data=services.find_pathway_user_db_by_id(id=int(pathway_user_id)))

    def on_put(self, req, resp, pathway_user_id: int):
        body = req.media
        body["id"] = int(pathway_user_id)
        resouce_response_api(resp=resp, data=services.update_pathway_user_db(json_object=body))

    def on_delete(self, req, resp, pathway_user_id: int):
        resouce_response_api(resp=resp, data=services.delete_pathway_user_by_id(id=int(pathway_user_id)))

class UserPathwayUserResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id','pathway_id'], params_string=['pathway_name'])
        filters.append({
            'field': 'user_id',
            'value': req.context['user']['id']
        })
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_pathway_user_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        body = req.media
        body['user_id'] = req.context['user']['id']
        body['user_name'] = req.context['user']['name']
        resouce_response_api(resp=resp, data=services.insert_pathway_user_db(json_object=body))

    def on_put(self, req, resp):
        body = req.media
        resouce_response_api(resp=resp, data=services.update_pathway_user_by_user(
            pathway_ids=body['pathway_ids'],
            user_id=req.context['user']['id'],
            user_name=req.context['user']['name']))

class UserPathwayByIdResuorce:
    def on_delete(self, req, resp, pathway_user_id: int):
        resouce_response_api(resp=resp, data=services.delete_pathway_user_by_id(id=int(pathway_user_id), user_id=req.context['user']['id']))