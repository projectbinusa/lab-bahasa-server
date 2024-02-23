import requests
import falcon
class ImageForPdfResource:
    auth = {"auth_disabled": True}

    def on_get(self, req, resp):
        image_url = req.params.get('url')
        if image_url:
            response = requests.get(image_url)
            resp.content_type = response.headers['content-type']
            resp.status=falcon.HTTP_200
            resp.body=response.content
        else:
            resp.status=falcon.HTTP_202
            resp.body=''