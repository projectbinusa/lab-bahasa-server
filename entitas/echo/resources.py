import sys

import falcon

def my_500_error_decorator(func):
    def wrapper(*args):
        try:
            func(*args)
        except Exception as e:
            print('halooooo ',e)
            # resp.status = falcon.HTTP_500
            # resp.body = json.dumps({'status': 0, 'message': 'Server Error'})
        return wrapper
class EchoResource:
    auth = {"auth_disabled": True}

    def on_get(self, req, resp):
        resp.media = "echo"
        resp.status = falcon.HTTP_200

class CertbotResource:
    auth = {"auth_disabled": True}

    def on_get(self, req, resp, token: str):
        resp.media = "echo"
        resp.status = falcon.HTTP_200

class TesstErrorResource:
    auth = {"auth_disabled": True}

    def on_get(self, req, resp):
        from util.entitas_util import resouce_response_api
        from entitas.user.services import find_user_db_by_id
        account = find_user_db_by_id(id=1)
        print('user ---> ',account)
        print('user ---> ', account.name)
        resouce_response_api(resp=resp, data=1/0)

class TestEnvResource:
    auth = {"auth_disabled": True}

    def on_get(self, req, resp):
        resp.media = "Wed Jul 27 12:35:37 WIB 2022"
        resp.status = falcon.HTTP_200

class PythonVersionResource:
    auth = {"auth_disabled": True}

    def on_get(self, req, resp):
        resp.media = sys.version
        resp.status = falcon.HTTP_200

