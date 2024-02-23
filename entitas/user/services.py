import uuid

import falcon

from entitas.user import repositoriesDB
from util.entitas_util import *
from util.other_util import encrypt_string, get_random_string, raise_error
import datetime
from config.config import TYPE_TOKEN_USER


def get_user_db_with_pagination(
    page=1, limit=9, name="", to_model=False, filters=[], to_response="to_response"
):
    return repositoriesDB.get_all_with_pagination(
        page=page,
        limit=limit,
        name=name,
        to_model=to_model,
        filters=filters,
        to_response=to_response,
    )


def find_user_db_by_id(id=0, to_model=False):
    account = repositoriesDB.find_by_id(id=id)
    if account is None:
        return None
    if to_model:
        return account
    return account.to_response()


def find_user_db_by_list_id(list_id=[], to_model=False):
    accounts = repositoriesDB.find_by_list_id(list_id=list_id)
    if to_model:
        return accounts
    result = []
    for account in accounts:
        result.append(account.to_response())
    return result


def find_user_db_by_name(name="", to_model=False):
    return repositoriesDB.find_by_name(name=name, to_model=to_model)


def get_all_user_db(filters=[], to_model=False):
    return repositoriesDB.get_all(filters=filters, to_model=to_model)


def update_user_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)


def update_password_user_db(json_object={}):
    from util.constant import SUCCESS, AccountConstant

    if json_object["new_password"] == json_object["old_password"]:
        return None, AccountConstant.MESSAGE_NEW_PASSWORD_DOESNT_MATCH
    if "confirm_new_password" in json_object:
        if json_object["confirm_new_password"] != json_object["new_password"]:
            return None, AccountConstant.MESSAGE_NEW_PASSWORD_DOESNT_MATCH
    account = repositoriesDB.find_by_id(id=json_object["user"]["id"])
    if account is None:
        return None, AccountConstant.ACCOUNT_NOT_MATCH
    if encrypt_string(json_object["old_password"]) != account.password:
        return None, AccountConstant.PASSWORD_NOT_MATH

    if "confirm_new_password" not in json_object:
        return None, AccountConstant.MESSAGE_NEW_PASSWORD_DOESNT_MATCH
    json_object["id"] = account.id
    return repositoriesDB.update_password(json_object=json_object), SUCCESS


def insert_user_db(json_object={}, to_model=False):
    if "picture" not in json_object:
        json_object["picture"] = ''
    data, status = repositoriesDB.insert(json_object=json_object, to_model=to_model)
    return data, status


def signup_user_db(json_object={}):
    # aa
    from config.config import domain_name
    from entitas.message.models import Message
    from entitas.message.services import sendEmail
    from util.constant import EMAIL_MUST_FILL
    from util.jwt_util import check_valid_email, jwt_encode

    if "email" not in json_object:
        return {"token": "", "message": EMAIL_MUST_FILL}

    name_from_email = json_object["email"].split("@")[0]
    if "hp" not in json_object:
        json_object["hp"] = ""
    if "role_id" not in json_object:
        json_object["role_id"] = 1
    if "active" not in json_object:
        json_object["active"] = False
    json_object = update_json_object_role(json_object=json_object)

    json_object["token"] = str(uuid.uuid4())
    if "password" not in json_object:
        json_object["password"] = get_random_string(5)
    if not check_valid_email(email=json_object["email"]):
        return {"token": "", "message": "Email tidak valid"}
    account = repositoriesDB.find_by_email(email=json_object["email"], to_model=True)

    if account is None:
        json_object["new_password"] = json_object["password"]
        account_info, _ = repositoriesDB.insert(json_object=json_object, to_model=True)
        message = Message()
        message.receiver = json_object["email"]
        message.receiver_cc = cc_address
        app_name = "Kemenag API"
        message.subject = "Selamat Datang di ByrTagihan"
        sendEmail(
            message=message,
            template_html="create_user",
            data={
                "name": name_from_email,
                "password": json_object["new_password"],
                "email": account_info.email,
                "type": "",
                "sso": True,
                # 'url': url,
                "app_name": app_name,
            },
        )
        return jwt_encode(account_info.to_response_login(), TYPE_TOKEN_USER)

    # elif user.password in [None, '']:
    #     account_info = repositoriesDB.update_password_by_email(json_object['email'], json_object['password'])
    #     message = Message()
    #     message.receiver = json_object['email']
    #     message.receiver_cc = cc_address
    #     message.subject = 'Welcome To Guru Kreator'
    #     sendEmail(message=message, template_html='create_user',
    #               data={'name': user.first_name, 'email': json_object['email'], 'password': json_object['password'],
    #                     'type': account_info.account_type_name,
    #                     'sso': False,
    #                     'app_name': 'Guru Kreator'})
    #
    #     return jwt_encode(account_info.to_response_login())
    else:
        return {"token": "", "message": "Email sudah digunakan"}
    

def delete_user_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)


def login_db(json_object={}, domain=""):
    from util.jwt_util import jwt_encode

    account_info = repositoriesDB.post_login(json_object=json_object)
    if account_info is None:
        return None, "Email atau password tidak sesuai"

    if account_info.active == 0:
        return None, "Email belum di aktivasi"
    domain_result = ""

    account = account_info.to_response_login()
    account["domain"] = domain_result
    return jwt_encode(account, TYPE_TOKEN_USER), "success"


def find_user_db_by_token(token="", to_model=False):
    return repositoriesDB.find_by_token(token=token, to_model=to_model)


def update_profile_id_user_db(json_object={}):
    account = find_user_db_by_id(id=json_object["user"]["id"], to_model=True)
    if account is None:
        raise_error(msg="akun tidak ditemukan")
    return repositoriesDB.update_profile(json_object=json_object, to_model=False)


def update_profile_id_user_db_admin(json_object={}):
    account = find_user_db_by_id(id=json_object["id"], to_model=True)
    if account is None:
        return None, "akun tidak ditemukan"
    return repositoriesDB.update_profile(json_object=json_object, to_model=False)


def logout_user_db(json_object={}):
    return repositoriesDB.reset_token_by_token(token=json_object['token'])


def get_profile_id_user_db(json_object={}):
    account = repositoriesDB.find_by_id(id=json_object["user"]["id"])
    if account is None:
        return None, ""
    return account.to_response_profile(), "success"


def get_profile_id_user_db_admin(id=0):
    account = repositoriesDB.find_by_id(id=id)
    if account is None:
        return None, ""
    return account.to_response_profile(), "success"


def find_user_db_by_email(email="", to_model=False):
    return repositoriesDB.find_by_email(email=email, to_model=to_model)


def is_email_user_exist(email=""):
    return repositoriesDB.is_email_user_exist(email=email)


def get_user_name_by_user_id(account_id=0):
    return repositoriesDB.get_user_name_by_user_id(account_id=account_id)


def update_fcm_token_user_db(account_id=0, token=""):
    return repositoriesDB.update_fcm_token_user_db(
        account_id=account_id, token=token
    )


def activate_user_by_email(email=""):
    return repositoriesDB.activate_user_by_email(
        email=email, active=1
    ).to_response_login()


def activate_user_by_id_by_admin(id=0):
    from entitas.message.models import Message
    from entitas.message.services import get_template, sendEmail

    new_password = get_random_string(5)
    account = repositoriesDB.activate_user_by_id(
        id=id, active=1, new_password=new_password
    )
    name_from_email = account.email.split("@")[0]
    message = Message()
    message.receiver = account.email
    message.subject = "Welcome To byrtagihan.com"
    app_name = "byrtagihan.com"
    sendEmail(
        message=message,
        template_html="create_user",
        data={
            "name": name_from_email
            if account.first_name is None or account.first_name == ""
            else account.first_name,
            "email": account.email,
            "password": new_password,
            "type": "",
            "sso": False,
            "app_name": app_name,
        },
    )
    url = "https://byrtagihan.com/"
    return True


def update_school_name_in_user(school_id=None, school_name=""):
    return repositoriesDB.update_school_name(
        school_id=school_id, school_name=school_name
    )


def get_user_relations_by_id(id=0, school_id=None):
    data = repositoriesDB.find_by_id(id=id)
    if data is None:
        return None
    if school_id is not None and data.school_id != school_id:
        return None

    from entitas.admin_school.services import find_admin_school_by_user_id
    from entitas.homeroom.services import find_home_room_by_user_id
    from entitas.parent.services import find_parent_by_user_id
    from entitas.student.services import find_student_by_user_id
    from entitas.teacher.services import find_teacher_by_user_id

    result = {}
    result["teacher"] = find_teacher_by_user_id(account_id=id, school_id=school_id)
    result["student"] = find_student_by_user_id(account_id=id)
    result["parent"] = find_parent_by_user_id(account_id=id)
    result["admin_school"] = find_admin_school_by_user_id(account_id=id)
    result["home_room"] = find_home_room_by_user_id(account_id=id)
    return result


def update_user_relations_by_id(id=0, json_object={}, school_id=None):
    data = repositoriesDB.find_by_id(id=id)
    if data is None:
        return None
    if school_id is not None and data.school_id != school_id:
        return None
    from util.entitas_util import update_user_id_multi

    return update_user_id_multi(json_object=json_object, account_id=id)


def update_user_types_in_user(id=0, json_user_type={}):
    data = repositoriesDB.find_by_id(id=id)
    if data is None:
        return None
    finded = False
    for account_type in data.account_types:
        if account_type["account_type_id"] == json_user_type["account_type_id"]:
            finded = True
            break
    if not finded:
        data.account_types.append(json_user_type)
    return repositoriesDB.update_user_types_in_user(
        id=id, account_types=data.account_types
    )


def update_user_for_socket_id(id=0, socket_id=""):
    return repositoriesDB.update_socket_id(id=id, socket_id=socket_id)


def update_teacher_make_as_admin_school(teacher_id=None):
    from entitas.teacher.services import find_teacher_db_by_id

    teacher = find_teacher_db_by_id(id=teacher_id, to_model=True)
    if teacher is None:
        return None
    account = repositoriesDB.find_by_id(id=teacher.account_id)
    for account_type in account.account_types:
        if account_type["account_type_id"] == 2:
            return True
    account.account_types.append(
        update_json_object_user_type(json_object={"account_type_id": 2})
    )
    repositoriesDB.update_user_types_in_user(
        id=teacher.account_id, account_types=account.account_types
    )
    return True


def delete_teacher_make_as_admin_school(teacher_id=None):
    from entitas.teacher.services import find_teacher_db_by_id

    teacher = find_teacher_db_by_id(id=teacher_id, to_model=True)
    if teacher is None:
        return None
    account = repositoriesDB.find_by_id(id=teacher.account_id)
    for item in range(len(account.account_types)):
        if account.account_types[item]["account_type_id"] == 2:
            del account.account_types[item]
    repositoriesDB.update_user_types_in_user(
        id=teacher.account_id, account_types=account.account_types
    )
    return True


def force_update_password_user(json_object={}):
    return repositoriesDB.update_password(json_object=json_object)


def update_email_by_id_from_student(id=None, email=""):
    return repositoriesDB.update_email_by_id(id=id, email=email)


def update_user_for_name_by_id(id=0, first_name="", last_name="", hp=""):
    return repositoriesDB.update_name_by_id(
        id=id, first_name=first_name, last_name=last_name, hp=hp
    )


def update_user_for_schools_by_id(id=0, schools=[]):
    return repositoriesDB.update_schools_by_id(id=id, schools=schools)


def is_token_valid(id=0, token=""):
    return repositoriesDB.is_email_user_exist(id=id, token=token)


def update_name(id=0, first_name="", last_name=""):
    return repositoriesDB.update_name(id=id, first_name=first_name, last_name=last_name)

# script update email
def update_email_for_student(email_lama="", email_baru="", school_id=None):
    from entitas.class_student.services import update_all_class_student_email
    from entitas.student.services import update_email_in_student
    from entitas.files.services import update_email_in_file
    account = repositoriesDB.find_by_email(email=email_lama, to_model=True)
    if account is None:
        return None
    if school_id is not None and account.school_id != school_id:
        return None
    repositoriesDB.update_email_by_id(id=account.id, email=email_baru)
    student = update_email_in_student(account_id=account.id, student_email_lama=email_lama, student_email_baru=email_baru)
    update_all_class_student_email(student_id=student.id, student_email_lama=email_lama, student_email_baru=email_baru)
    update_email_in_file(account_id=account.id, account_email=email_baru)
    return True

# script update email
def update_email_from_gsheet(spread_sheet_id="", tab_name="", school_id=None):
    from util.gsheet_util import get_gsheet, update_gsheet

    result = {"success": 0, "failed": 0, "email_failed": []}
    values_gsheet = get_gsheet(
        spread_sheet_id=spread_sheet_id, range_sheet=tab_name + "!A2:AK"
    )
    student_id_values = []
    for row in values_gsheet:
        print(row[5], '------>', row[6])
        if row[7] == "":
            email = update_email_for_student(email_lama=row[5], email_baru=row[6], school_id=school_id)
            if email is None:
                result["failed"] += 1
                student_id_values.append(["failed"])
                result["email_failed"].append(row[5])
                continue
            result["success"] += 1
            student_id_values.append(["success"])
    update_gsheet(
        spread_sheet_id=spread_sheet_id,
        range_sheet=tab_name + "!H11:H",
        values=student_id_values,
    )
    print(result, '====')
    return result


# script update email
def update_email_from_gsheet_demo(spread_sheet_id="", tab_name="", school_id=None):
    from util.gsheet_util import get_gsheet, update_gsheet

    result = {"success": 0, "failed": 0, "email_failed": []}
    values_gsheet = get_gsheet(
        spread_sheet_id=spread_sheet_id, range_sheet=tab_name + "!A2:AK"
    )
    student_id_values = []
    for row in values_gsheet:
        print(row[0], '------>', row[1])
        email = update_email_for_student(email_lama=row[0], email_baru=row[1], school_id=school_id)
        if email is None:
            result["failed"] += 1
            student_id_values.append(["failed"])
            result["email_failed"].append(row[0])
            continue
        result["success"] += 1
        student_id_values.append(["success"])
    update_gsheet(
        spread_sheet_id=spread_sheet_id,
        range_sheet=tab_name + "!C2:C",
        values=student_id_values,
    )
    print(result, '=====')
    return result

def is_email_has_user(email=""):
    return repositoriesDB.is_email_has_user(email=email)

def oauth_login_with_google(json_object={}):
    from google.oauth2 import id_token
    from google.auth.transport import requests
    from config.config import google_oauth_cliend_id
    from util.jwt_util import jwt_encode
    from entitas.admin_school.services import (
        update_admin_school_last_login_by_user_id,
    )
    from entitas.school.services import find_school_db_by_id
    from entitas.student.services import update_student_last_login_by_user_id
    from entitas.teacher.services import update_teacher_last_login_by_user_id
    from entitas.parent.services import update_parent_last_login_by_user_id

    request = requests.Request()
    try:
        id_info = id_token.verify_oauth2_token(json_object['token'], request, google_oauth_cliend_id)
        if is_email_has_user(email=id_info["email"]):
            account_info = find_user_db_by_email(
                email=id_info["email"], to_model=True
            )
            if account_info is None:
                return None, "Email atau password tidak sesuai"

            if account_info.active == 0:
                return None, "Email belum di aktivasi"
            teacher_id = update_teacher_last_login_by_user_id(account_id=account_info.id)
            student_id = update_student_last_login_by_user_id(account_id=account_info.id)
            parent_id = update_parent_last_login_by_user_id(account_id=account_info.id)
            update_admin_school_last_login_by_user_id(account_id=account_info.id)
            domain_result = ""
            if len(account_info.schools) < 2:
                school = find_school_db_by_id(id=account_info.school_id, to_model=True)
                if school is not None:
                    domain_result = school.domain
            else:
                for item in account_info.schools:
                    school = find_school_db_by_id(id=int(item["school_id"]), to_model=True)
                    if school is None:
                        continue
                    if school.domain.upper() in domain.upper():
                        account_info.school_id = school.id
                        account_info.school_name = school.name
                        domain_result = school.domain
                        teacher_id = update_teacher_last_login_by_user_id(account_id=account_info.id,school_id=school.id)
                        break


            account = account_info.to_response_login()
            account["student_id"] = student_id
            account["teacher_id"] = teacher_id
            account['parent_id'] = parent_id
            account["domain"] = domain_result
            return jwt_encode(account, TYPE_TOKEN_USER)
        else:
           raise Exception('Email Not Found')
    except Exception as e:
        raise_error(msg=str(e))
        return None
    
def execute_reset_password_in_user_demo():
    from entitas.message.models import Message
    from entitas.message.services import sendEmail

    email_list = ["demoadminschool.2@gmail.com", "demoteacher.2@gmail.com", "demostudent.2@gmail.com"]
    for email in email_list:
        json_object = {}
        account = repositoriesDB.find_by_email(email=email)
        if account is not None:
            json_object['id'] = account['id']
            json_object['new_password'] = get_random_string(6)
            print(json_object['new_password'], '====', account['email'])
            repositoriesDB.update_password(json_object=json_object)
            repositoriesDB.reset_token(json_object=json_object)
            message = Message()
            message.receiver_cc = ""
            message.receiver = email
            message.subject = "Password Baru"
            app_name = "byrtagihan.com"
            sendEmail(
                message=message,
                template_html="password_received",
                data={"new_password": json_object['new_password'], "type": "", "app_name": app_name},
            )
    print('execute_reset_password_in_user_demo')
    
def refresh_token_authorization(authorization=None):
    authorization=authorization.split(' ')[1]
    import jwt
    from config.config import secret_jwt
    from util.jwt_util import jwt_encode
    try:
        if authorization is None or authorization == '':
            raise Exception('authorization empty')
        auth = jwt.decode(
                authorization, secret_jwt, algorithms="HS512"
            )
    except:
        raise falcon.HTTPUnauthorized(
                title="401 Unauthorized",
                description="Signature has expired",
                challenges=None)
    
    date_time_exp = datetime.datetime.fromtimestamp(auth['exp'])
    print(date_time_exp, '===', datetime.datetime.now())
    if date_time_exp <= datetime.datetime.now():
        raise falcon.HTTPUnauthorized(
                title="401 Unauthorized",
                description="Signature has expired",
                challenges=None)
    return jwt_encode(user_info=auth, type_token=TYPE_TOKEN_USER)

def get_user_member_with_pagination(
    page=1, limit=9, to_model=False, filters=[], to_response="to_response"
):
    from entitas.member.services import get_member_db_with_pagination
    return get_member_db_with_pagination(page=page, limit=limit, filters=filters, to_response=to_response, to_model=to_model)

def find_user_member_by_id(member_id=0):
    from entitas.member.services import find_member_db_by_id
    member = find_member_db_by_id(id=member_id, to_model=True)
    if member is None:
        raise_error(msg='Member not found')
    return member.to_response()

def delete_user_member_by_id(member_id=0):
    from entitas.member.services import find_member_db_by_id, delete_member_by_id
    member = find_member_db_by_id(id=member_id, to_model=True)
    if member is None:
        raise_error(msg='Member not found')
    data = delete_member_by_id(id=member_id)
    if data is None:
        raise_error(msg="Failed to delete")
    return True

def update_user_member(json_object={}):
    from entitas.member.services import find_member_db_by_id, update_member_db
    member = find_member_db_by_id(id=json_object['member_id'], to_model=True)
    if member is None:
        raise_error(msg='Member not found')
    json_object["id"] = member.id
    return update_member_db(json_object=json_object)