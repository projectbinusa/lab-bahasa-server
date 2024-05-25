import json
from urllib.request import urlopen

import falcon
import requests
from entitas.user import services, repositoriesDB
from entitas.baseResponse.models import BaseResponse
from util.entitas_util import generate_filters_resource, resouce_response_api


class UserResource:
    # auth = {
    #     'auth_disabled': True
    # }

    def on_get(self, req, resp):
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        filters = generate_filters_resource(req=req, params_string=['first_name', 'last_name', 'email', ])
        data, pagination = services.get_user_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        picture = req.get_param("picture", default=None)
        # signature = req.get_param("signature", default=None)
        bank_book_photo = req.get_param("bank_book_photo", default=None)
        id_card = req.get_param("id_card", default=None)
        body = {}
        body['name'] = req.get_param("name")
        body['email'] = req.get_param("email")
        body['hp'] = req.get_param("hp")
        body['password'] = req.get_param("password")
        body['address'] = req.get_param("address")
        body['agency'] = req.get_param("agency")
        body['bank_account'] = req.get_param("bank_account")
        # body['bank_book_photo'] = req.get_param("bank_book_photo")
        body['bank_in_name'] = req.get_param("bank_in_name")
        body['bank_name'] = req.get_param("bank_name")
        body['birth_date'] = req.get_param("birth_date")
        body['birth_place'] = req.get_param("birth_place")
        body['city'] = req.get_param("city")
        # body['id_card'] = req.get_param("id_card")
        body['last_education'] = req.get_param("last_education")
        # body['client_ID'] = req.get_param("client_ID")
        # body['departement'] = req.get_param("departement")
        # body['class_id'] = req.get_param("class_id")
        # body['password_prompt'] = req.get_param("password_prompt")
        # body['gender'] = req.get_param("gender")
        body['nip'] = req.get_param("nip")
        body['npwp'] = req.get_param("npwp")
        body['position'] = req.get_param("position")
        body['rank'] = req.get_param("rank")
        body['signature'] = req.get_param("signature")
        body['tag'] = req.get_param("tag")
        body['work_unit'] = req.get_param("work_unit")
        resouce_response_api(resp=resp, data=services.insert_user_db(json_object=body, picture=picture,
                                                                     bank_book_photo=bank_book_photo, id_card=id_card))

class RegisterGuruResource:
    auth = {"auth_disabled": True}
    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.register_guru(json_object=req.media))


class UserWithIdResource:

    def on_get(self, req, resp, id: int):
        resouce_response_api(resp=resp, data=services.find_user_db_by_id(id=int(id)))

    def on_put(self, req, resp, id: int):
        body = req.media
        body["id"] = id
        resouce_response_api(resp=resp, data=services.update_user_db(json_object=body))

    def on_delete(self, req, resp, id: int):
        resouce_response_api(resp=resp, data=services.delete_user_by_id(id=int(id)))


class UserLoginResource:
    auth = {"auth_disabled": True}

    def on_post(self, req, resp):
        body = req.media
        domain = ""
        if "ORIGIN" in req.headers:
            domain = req.headers["ORIGIN"]
        resouce_response_api(resp=resp, data=services.login_db(
            json_object=body, domain=domain
        ), pagination={})


class UserSignupResource:
    auth = {"auth_disabled": True}

    def on_get(self, req, resp):
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        filters = generate_filters_resource(req=req, params_int=['id'], params_string=['name', 'email', 'role', 'tag'])
        data, pagination = services.get_user_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        picture = req.get_param("picture", default=None)
        # signature = req.get_param("signature", default=None)
        bank_book_photo = req.get_param("bank_book_photo", default=None)
        id_card = req.get_param("id_card", default=None)
        body = {}
        body['name'] = req.get_param("name")
        body['email'] = req.get_param("email")
        body['hp'] = req.get_param("hp")
        body['password'] = req.get_param("password")
        body['address'] = req.get_param("address")
        body['agency'] = req.get_param("agency")
        body['bank_account'] = req.get_param("bank_account")
        body['bank_in_name'] = req.get_param("bank_in_name")
        body['bank_name'] = req.get_param("bank_name")
        body['birth_date'] = req.get_param("birth_date")
        body['birth_place'] = req.get_param("birth_place")
        body['city'] = req.get_param("city")
        body['last_education'] = req.get_param("last_education")
        # body['client_ID'] = req.get_param("client_ID")
        # body['departement'] = req.get_param("departement")
        # body['class_id'] = req.get_param("class_id")
        # body['password_prompt'] = req.get_param("password_prompt")
        # body['gender'] = req.get_param("gender")
        body['nip'] = req.get_param("nip")
        body['npwp'] = req.get_param("npwp")
        body['position'] = req.get_param("position")
        body['rank'] = req.get_param("rank")
        body['signature'] = req.get_param("signature")
        body['tag'] = req.get_param("tag")
        body['work_unit'] = req.get_param("work_unit")
        resouce_response_api(resp=resp, data=services.signup_user_db(json_object=body, picture=picture,
                                                                     bank_book_photo=bank_book_photo, id_card=id_card))


class UserUpdatePasswordWithResource:

    def on_put(self, req, resp):
        body = req.media
        body["user"] = req.context["user"]
        resouce_response_api(resp=resp, data=services.update_password_user_db(
            json_object=body
        ))


class UserUpdateProfileWithIdResource:
    def on_put(self, req, resp):
        body = req.media
        body["id"] = req.context["user"]["id"]
        resouce_response_api(resp=resp, data=services.update_profile_id_user_db(
            json_object=body
        ))

    def on_get(self, req, resp):
        resouce_response_api(resp=resp, data=services.get_profile_id_user_db(
            json_object={"id": req.context["user"]["id"]}
        ))


class AdminUserUpdateProfileWithIdResource:
    def on_put(self, req, resp, user_id: int):
        picture = req.get_param("picture", default=None)
        # signature = req.get_param("signature", default=None)
        bank_book_photo = req.get_param("bank_book_photo", default=None)
        id_card = req.get_param("id_card", default=None)
        body = {}
        body["id"] = int(user_id)
        body['name'] = req.get_param("name")
        body['email'] = req.get_param("email")
        body['hp'] = req.get_param("hp")
        body['password'] = req.get_param("password")
        body['address'] = req.get_param("address")
        body['agency'] = req.get_param("agency")
        body['bank_account'] = req.get_param("bank_account")
        body['bank_in_name'] = req.get_param("bank_in_name")
        body['bank_name'] = req.get_param("bank_name")
        body['birth_date'] = req.get_param("birth_date")
        body['birth_place'] = req.get_param("birth_place")
        body['city'] = req.get_param("city")
        body['last_education'] = req.get_param("last_education")
        # body['client_ID'] = req.get_param("client_ID")
        # body['departement'] = req.get_param("departement")
        # body['class_id'] = req.get_param("class_id")
        # body['password_prompt'] = req.get_param("password_prompt")
        # body['gender'] = req.get_param("gender")
        # body['signed_time'] = req.get_param("signed_time")
        body['nip'] = req.get_param("nip")
        body['npwp'] = req.get_param("npwp")
        body['position'] = req.get_param("position")
        body['rank'] = req.get_param("rank")
        body['signature'] = req.get_param("signature")
        body['tag'] = req.get_param("tag")
        body['work_unit'] = req.get_param("work_unit")
        resouce_response_api(resp=resp, data=services.update_profile_id_user_by_admin(
            json_object=body, picture=picture, bank_book_photo=bank_book_photo, id_card=id_card
        ))

    def on_get(self, req, resp, user_id: int):
        resouce_response_api(resp=resp, data=services.get_profile_id_user_db(
            json_object={"id": int(user_id)}
        ))


class UserLogoutWithIdResource:

    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.logout_user_db(
            json_object={"token": req.context["user"]["token"]}
        ))


class UserForgotPasswordWithResource:
    auth = {"auth_disabled": True}

    def on_post(self, req, resp):
        from util.entitas_util import forgot_password_dynamic
        body = req.media
        resouce_response_api(resp=resp, data=services.forgot_password_dynamic(
            json_object=body
        ))


class UserResetPasswordWithResource:
    auth = {"auth_disabled": True}

    def on_get(self, req, resp, token: str):
        base_response = BaseResponse()
        base_response.data = services.reset_password_by_token(token=token)
        if base_response.data is not None:
            base_response.status = falcon.HTTP_200
            base_response.code = 200
            base_response.message = "success"
        else:
            base_response.status = falcon.HTTP_400
            base_response.code = 400
            base_response.message = "failed"

        # base_response.status = falcon.HTTP_500
        resp.content_type = "text/html"
        resp.body = "".join(base_response.data)


class UserActivationResource:
    auth = {"auth_disabled": True}

    def on_get(self, req, resp, token: str):
        from user_agents import parse

        base_response = BaseResponse()
        user_agent = parse(req.headers["USER-AGENT"])
        is_mobile = user_agent.is_mobile or user_agent.is_tablet
        base_response.data = services.account_activation_by_token(
            token=token, is_mobile=is_mobile
        )
        if base_response.data is not None:
            base_response.status = falcon.HTTP_200
            base_response.code = 200
            base_response.message = "success"
        else:
            base_response.status = falcon.HTTP_400
            base_response.code = 400
            base_response.message = "failed"

        resp.content_type = "text/html"
        resp.text = base_response.data


class UserUpdateProfileWithIdResourceAdmin:

    def on_put(self, req, resp, id: int):
        body = req.media
        body["id"] = id
        resouce_response_api(resp=resp, data=services.update_profile_id_user_db_admin(
            json_object=body
        ))

    def on_get(self, req, resp, id: int):
        resouce_response_api(resp=resp, data=services.get_profile_id_user_db_admin(id=int(id)))


class UserRefreshTokenResource:
    # auth = {"auth_disabled": True}
    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.refresh_token_authorization(
            authorization=req.headers['AUTH-EVENT'] if 'AUTH-EVENT' in req.headers else ''))


class AdminInstructurResource:
    def on_get(self, req, resp):
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        filters = generate_filters_resource(req=req, params_string=['ame', 'email'])
        filters.append({'field': 'role', 'value': 'instructur'})
        data, pagination = services.get_user_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)


class AdminUserUserIdResource:

    def on_get(self, req, resp, instructur_id: int):
        resouce_response_api(resp=resp, data=services.find_user_db_by_id(id=int(instructur_id)))


class ManagementListResource:
    # auth = {
    #     'auth_disabled': True
    # }

    def on_get(self, req, resp, class_id: int):
        filters = generate_filters_resource(req=req, params_int=['id'])
        filters.append({"field": "class_id", "value": int(class_id)})
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        # filters = generate_filters_resource(req=req, params_string=['first_name', 'last_name', 'email',])
        data, pagination = services.get_list_by_class_id(
            class_id=class_id, page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)

    def on_post(self, req, resp):
        resouce_response_api(resp=resp,
                             data=services.create_profile_manage_student_list_service(json_object=req.media))


class ManagementListWithByIdResources:
    # auth = {
    #     'auth_disabled': True
    # }

    # def on_get(self, req, resp, user_id: int):
    #     resouce_response_api(resp=resp, data=services.update_menage_name_list_db(
    #         json_object={"id": user_id}
    #     ))

    def on_put(self, req, resp, user_id: int):
        body = req.media
        resouce_response_api(resp=resp, data=services.update_menage_name_list_db(
            user_id=req.context['user_id']['id'], json_object=body
        ))

    def on_delete(self, req, resp, management_name_list_id: int):
        resouce_response_api(resp=resp,
                             data=services.delete_management_name_list_by_id(id=int(management_name_list_id)))

    def on_get(self, req, resp, class_id: int, management_list_id: int):
        log_book_data = services.find_management_list_by_ids(
            class_id=int(class_id),
            management_list_id=int(management_list_id),
        )
        resouce_response_api(resp=resp, data=log_book_data)
