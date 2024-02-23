import os
import pathlib
import falcon

os.environ["TZ"] = "Asia/Jakarta"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api = falcon.App(cors_enable=True)
api.req_options.auto_parse_form_urlencoded = True
print("Event File API Backend")
STATIC_PATH = pathlib.Path(__file__).parent / "files"
favicon_url = "https://falconframework.org/favicon-32x32.png"
api.add_static_route('/files', str(STATIC_PATH))