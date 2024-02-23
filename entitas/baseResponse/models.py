import falcon


class BaseResponse:
    def __init__(self):
        self.status = falcon.HTTP_500
        self.code = 500
        self.data = {}
        self.message = ""
        self.pagination = {}

    def toJSON(self):
        return {
            "status": self.status,
            "code": self.code,
            "data": self.data,
            "message": self.message,
            "pagination": self.pagination,
        }
