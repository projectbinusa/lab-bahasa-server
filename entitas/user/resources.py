import json
from urllib.request import urlopen

import falcon
import requests
from entitas.user import services
from entitas.baseResponse.models import BaseResponse
from util.entitas_util import generate_filters_resource, resouce_response_api


class UserResource:
    # auth = {
    #     'auth_disabled': True
    # }

    def on_get(self, req, resp):
        page = int(req.get_param("page", required=False, default=1))
        limit = int(req.get_param("limit", required=False, default=9))
        filters = generate_filters_resource(req=req, params_string=['first_name', 'last_name', 'email',])
        data, pagination = services.get_user_db_with_pagination(
            page=page, limit=limit, filters=filters
        )
        resouce_response_api(resp=resp, data=data, pagination=pagination)


    def on_post(self, req, resp):
        resouce_response_api(resp=resp, data=services.insert_user_db(json_object=req.media))


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
        resouce_response_api(resp=resp, data=services.signup_user_db(json_object=req.media))


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
        body = req.media
        body["id"] = int(user_id)
        resouce_response_api(resp=resp, data=services.update_profile_id_user_db(
            json_object=body
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
        resouce_response_api(resp=resp, data=services.refresh_token_authorization(authorization=req.headers['AUTH-EVENT'] if 'AUTH-EVENT' in req.headers else ''))


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