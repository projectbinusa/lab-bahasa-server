from entitas.baseResponse.models import BaseResponse

def generate_filters_resource(req=None,params_string=[], params_int=[]):
    filters = []
    for i in range(len(params_string)):
        if req.get_param(params_string[i], required=False, default="") != "":
            filters.append(
                {
                    "field": params_string[i],
                    "value": req.get_param(params_string[i], required=False, default=""),
                }
            )
    for i in range(len(params_int)):
        if req.get_param(params_int[i], required=False, default="") != "":
            filters.append(
                {
                    "field": params_int[i],
                    "value": req.get_param(params_int[i], required=False, default=0),
                }
            )
    return filters

def resouce_response_api(resp=None, data=None, pagination=None):
    import falcon
    base_response = BaseResponse()
    base_response.data = data
    base_response.pagination = pagination
    if base_response.data is not None:
        base_response.status = falcon.HTTP_200
        base_response.code = 200
        base_response.message = "success"
    else:
        base_response.status = falcon.HTTP_400
        base_response.code = 400
        base_response.message = "failed"
    resp.media = base_response.toJSON()
    if pagination is None:
        del resp.media['pagination']
    resp.status = base_response.status
    return resp
