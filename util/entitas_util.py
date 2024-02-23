from entitas.baseResponse.models import BaseResponse
from util.other_util import raise_error
def update_json_object_role(json_object={}):
    from entitas.role.services import find_role_db_by_id

    json_object["role_name"] = ""
    data = find_role_db_by_id(
        id=json_object["role_id"], to_model=True
    )
    if data is not None:
        json_object["role_name"] = data.name
    return json_object

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
    # from guppy import hpy
    # h = hpy()
    # print(h.heap())
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

def update_json_object_organization(json_object={}):
    from entitas.organization.services import find_organization_db_by_id

    json_object["organization_name"] = ""
    data = find_organization_db_by_id(
        id=json_object["organization_id"], to_model=True
    )
    if data is not None:
        json_object["organization_name"] = data.name
    return json_object

def update_json_object_channel(json_object={}):
    from entitas.channel.services import find_channel_db_by_id

    json_object["channel_name"] = ""
    data = find_channel_db_by_id(
        id=json_object["channel_id"], to_model=True
    )
    if data is not None:
        json_object["channel_name"] = data.name
    return json_object

def update_json_object_message_type(json_object={}):
    from entitas.message_type.services import find_message_type_db_by_id

    json_object["message_type_name"] = ""
    data = find_message_type_db_by_id(
        id=json_object["message_type_id"], to_model=True
    )
    if data is not None:
        json_object["message_type_name"] = data.name
    return json_object

def forgot_password_dynamic(json_object={}):
    from config.config import domain_name
    from entitas.message.models import Message
    from entitas.message.services import sendEmail
    from entitas.reset_password.services import forgot_password_by_email, forgot_password_by_unique_id
    from entitas.customer.services import find_customer_db_by_email
    from entitas.member.services import find_member_db_by_unique_id
    from entitas.message.services import sendWhatsapp
    from entitas.user.services import find_user_db_by_email

    if "email" not in json_object and "unique_id" not in json_object:
        raise_error(msg="Please enter email or unique_id")
    customer = None
    member = None
    account = None
    if "email" in json_object:
        customer = find_customer_db_by_email(email=json_object["email"], to_model=True)
        member = find_member_db_by_unique_id(unique_id=json_object["email"], to_model=True)
        account = find_user_db_by_email(email=json_object["email"], to_model=True)
    if "unique_id" in json_object:
        customer = find_customer_db_by_email(email=json_object["unique_id"], to_model=True)
        member = find_member_db_by_unique_id(unique_id=json_object["unique_id"], to_model=True)
        account = find_user_db_by_email(email=json_object["unique_id"], to_model=True)

    if customer is None and member is None and account is None:
        raise_error(msg="Email or unique_id not found")
    if customer is not None:
        if customer.active == 0:
            raise_error(msg="Account has not been Activated")
        reset_password = forgot_password_by_email(email=json_object["email"])
        url = domain_name + "/api/customer/reset_password/" + reset_password

        message = Message()
        message.receiver = customer.email
        message.subject = "Konfirmasi Reset Password"

        sendEmail(
            message=message,
            template_html="forgot_password",
            data={"name": customer.name, "url": url, "type": "-"},
        )

        return True
    elif member is not None:
        if member.organization_name == 0:
            raise_error(msg="Account has not been Activated")
        reset_password = forgot_password_by_unique_id(unique_id=json_object["unique_id"])
        url = domain_name + "/api/member/reset_password/" + reset_password
        message = Message()
        message.receiver = member.hp
        message.subject = "Konfirmasi Reset Password"
        message.message = 'Anda menerima pesan ini karena Anda menekan tombol LUPA PASSWORD.' + \
                          '\nKlik link di bawah untuk menyetel ulang password. \n' + url
        sendWhatsapp(message=message)
        return True
    elif account is not None:
        if account.active == 0:
            raise_error(msg="Account has not been Activated")
        reset_password = forgot_password_by_email(email=json_object["email"])
        url = domain_name + "/api/user/reset_password/" + reset_password
        message = Message()
        message.receiver = account.email
        message.subject = "Konfirmasi Reset Password"
        sendEmail(
            message=message,
            template_html="forgot_password",
            data={"name": account.name, "url": url, "type": "-"},
        )
        return True
