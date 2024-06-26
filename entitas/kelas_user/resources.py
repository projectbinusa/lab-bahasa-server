import os

from falcon import *

from entitas.kelas_user import services
from entitas.kelas_user.services import *
from util.entitas_util import generate_filters_resource, resouce_response_api


class KelasUserResource:
    def on_get(self, req, resp):
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name'])
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        data, pagination = services.get_kelas_user_db_with_pagination(page=page, limit=limit, filters=filters)
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        file = req.get_param('file')
        description = req.get_param('description')
        name = req.get_param('name')
        is_active = req.get_param('is_active')
        body = {
            "description": description,
            "name": name,
            "is_active": is_active
        }
        # body['user_id'] = req.context["user"]["id"]
        resouce_response_api(resp=resp, data=services.insert_kelas_user_db(json_object=body, file=file))

class KelasUserWithIdResource:
    def on_get(self, req, resp, class_id: int):
        resouce_response_api(resp=resp, data=services.find_kelas_user_db_by_id(id=int(class_id)))

    def on_put(self, req, resp, class_id: int):
        file = req.get_param('file')
        description = req.get_param('description')
        name = req.get_param('name')
        # is_active = req.get_param('is_active')
        body = {}
        body["id"] = int(class_id)
        body["description"] = description
        body["name"] = name
        # body["is_active"] = is_active
        # body['user_id'] = req.context["user"]["id"]
        resouce_response_api(resp=resp, data=services.update_kelas_user_db(json_object=body, file=file))

    def on_delete(self, req, resp, class_id: int):
        resouce_response_api(resp=resp, data=services.delete_kelas_user_by_id(id=int(class_id)))


class KelasUserActive:
    def on_put(self, req, resp, class_id: int):
        body = {}
        body["id"] = int(class_id)
        body["is_active"] = req.media.get("is_active", 1)
        body["user_id"] = req.context["user"]["id"]
        body["user_name"] = req.context["user"]["name"]
        resouce_response_api(resp=resp, data=services.kelas_user_active_db(json_object=body))


class KelasUserNotActive:
    def on_put(self, req, resp, class_id: int):
        body = {}
        body["id"] = int(class_id)
        body["is_active"] = req.media.get("is_active", 0)
        resouce_response_api(resp=resp, data=services.kelas_user_active_db(json_object=body))


class KelasUserExportResource:
    def on_get(self, req, resp):
        try:
            file_path = 'kelas_user.csv'
            export_kelas_user_to_excel(file_path)
            resp.status = HTTP_200
            resp.content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            resp.downloadable_as = file_path
            with open(file_path, 'rb') as f:
                resp.body = f.read()
            os.remove(file_path)
        except Exception as e:
            resp.status = HTTP_500
            resp.media = {'error': str(e)}


class KelasUserImportResource:
    def on_post(self, req, resp):
        uploaded_file = req.get_param('file')
        if uploaded_file.filename.endswith('.csv'):
            file_path = "tmp/" + uploaded_file.filename
            with open(file_path, 'wb') as f:
                f.write(uploaded_file.file.read())
            success, errors = services.import_kelas_user_from_excel(file_path)
            if success:
                resp.media = {"message": "Import successful"}
            if errors:
                resp.media = {"errors": errors}
        else:
            resp.media = {"error": "Only csv files are allowed for import"}


