import os
import pathlib

import falcon
from util.jwt_auth_backend import JWTAuthBackend
from util.falcon_midleware import FalconAuthMiddleware
from falcon_multipart.middleware import MultipartMiddleware


from config import config
from router.core_routes import core_routes
from util.jwt_util import portprq_auth

os.environ["TZ"] = "Asia/Jakarta"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api = falcon.App(
    cors_enable=True,
    middleware=[
        FalconAuthMiddleware(
            JWTAuthBackend(
                portprq_auth,
                secret_key=config.secret_jwt,
                algorithm="HS512",
                required_claims=["exp", "token"],
            ),
            exempt_routes=["/docs", "/metrics", "/api/certificate/code","/api/traffic/weekly/{billboard_id}", "/api/traffic/recap/monthly/{billboard_id", "/api/traffic/recap/weekly/{billboard_id", "/api/traffic/recap/minute/{billboard_id"],
            exempt_methods=["OPTIONS", "HEAD"],
        ),
        MultipartMiddleware(),
    ],
)
def generic_error_handler(ex, req, resp, params):
    if not isinstance(ex, falcon.HTTPError):
        print('halo ',ex)
        raise falcon.HTTPInternalServerError("Internal Server Error", str(ex))
    else:  # reraise :ex otherwise it will gobble actual HTTPError returned from the application code ref. https://stackoverflow.com/a/60606760/248616
        raise ex
# api.add_error_handler(Exception, generic_error_handler)
api.req_options.auto_parse_form_urlencoded = True

print("Event API Backend")
core_routes(api)

# SWAGGERUI_URL = "/docs"
# SCHEMA_URL = "/static/openapi.yaml"
STATIC_PATH = pathlib.Path(__file__).parent / "images"
favicon_url = "https://falconframework.org/favicon-32x32.png"
api.add_static_route('/images', str(STATIC_PATH))