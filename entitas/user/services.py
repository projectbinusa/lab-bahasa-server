import uuid

import falcon

from entitas.user import repositoriesDB
from util.constant import EMAIL_MUST_FILL, PASSWORD_MUST_FILL
from util.entitas_util import *
from util.jwt_util import jwt_encode, check_valid_email
from util.other_util import encrypt_string, get_random_string, raise_error, raise_forbidden
import datetime
from config.config import TYPE_TOKEN_USER, PICTURE_FOLDER, DOMAIN_FILE_URL, BANK_FOLDER, CARD_FOLDER


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

def get_user_db_with_pagination_manage_list(
        page=1, limit=9, name="", to_model=False, filters=[], to_response="to_response"
):
    return repositoriesDB.get_all_with_pagination_managements(
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


def insert_user_db(json_object={}, picture=None, bank_book_photo=None, id_card=None):
    print(json_object, picture)
    # if "picture" not in json_object:
    #     json_object["picture"] = ''
    temp_picture = str(uuid.uuid4()) + picture.filename.replace(" ", "")
    temp_bank = str(uuid.uuid4()) + bank_book_photo.filename.replace(" ", "")
    temp_card = str(uuid.uuid4()) + id_card.filename.replace(" ", "")
    with open(PICTURE_FOLDER + temp_picture, "wb") as f:
        f.write(picture.file.read())
        json_object["picture"] = DOMAIN_FILE_URL + '/files/' + json_object["picture"]
    with open(BANK_FOLDER + temp_bank, "wb") as f:
        f.write(bank_book_photo.file.read())
        json_object["bank_book_photo"] = DOMAIN_FILE_URL + '/files/' + json_object["bank_book_photo"]
    with open(CARD_FOLDER + temp_card, "wb") as f:
        f.write(id_card.file.read())
        json_object["id_card"] = DOMAIN_FILE_URL + '/files/' + json_object["id_card"]
    return repositoriesDB.insert(json_object=json_object)


def signup_user_db(json_object={}, picture=None, bank_book_photo=None, id_card=None):
    if "email" not in json_object:
        raise_error(str=EMAIL_MUST_FILL)
    if "password" not in json_object:
        raise_error(str=PASSWORD_MUST_FILL)
    if not check_valid_email(email=json_object["email"]):
        raise_error(msg='Email tidak valid')
    if 'role' not in json_object:
        json_object["role"] = 'student'
    json_object["token"] = str(uuid.uuid4())
    existing_account = repositoriesDB.find_by_email(email=json_object["email"], to_model=True)

    if existing_account is not None:
        raise_error(msg='Email sudah terdaftar')
    if picture is not None:
        temp_picture = str(uuid.uuid4()) + picture.filename.replace(" ", "")
        with open(PICTURE_FOLDER + temp_picture, "wb") as f:
            f.write(picture.file.read())
            json_object["picture"] = DOMAIN_FILE_URL + '/files/' + temp_picture
    if bank_book_photo is not None:
        temp_bank = str(uuid.uuid4()) + bank_book_photo.filename.replace(" ", "")
        with open(BANK_FOLDER + temp_bank, "wb") as f:
            f.write(bank_book_photo.file.read())
            json_object["bank_book_photo"] = DOMAIN_FILE_URL + '/files/' + temp_bank
    if id_card is not None:
        temp_card = str(uuid.uuid4()) + id_card.filename.replace(" ", "")
        with open(CARD_FOLDER + temp_card, "wb") as f:
            f.write(id_card.file.read())
            json_object["id_card"] = DOMAIN_FILE_URL + '/files/' + temp_card
    json_object["new_password"] = json_object["password"]
    return repositoriesDB.signup(json_object=json_object)


def delete_user_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)


def login_db(json_object={}, domain=""):
    from util.jwt_util import jwt_encode

    account_info = repositoriesDB.post_login(json_object=json_object)
    if account_info is None:
        raise_forbidden('Email atau password tidak sesuai')

    if account_info.active == 0:
        raise_error("Email belum di aktivasi")
    domain_result = ""

    account = account_info.to_response_login()
    account["domain"] = domain_result
    return jwt_encode(account, TYPE_TOKEN_USER)


def find_user_db_by_token(token="", to_model=False):
    return repositoriesDB.find_by_token(token=token, to_model=to_model)


def update_profile_id_user_db(json_object={}):
    if json_object is None:
        raise_error('payload data is empty')
    account = find_user_db_by_id(id=json_object["id"], to_model=True)
    if account is None:
        raise_error(msg="akun tidak ditemukan")
    return repositoriesDB.update_profile(json_object=json_object, to_model=False)

def update_profile_id_user_by_admin(json_object={}, picture=None, bank_book_photo=None, id_card=None):
    if json_object is None:
        raise_error('payload data is empty')
    account = find_user_db_by_id(id=json_object["id"], to_model=True)
    if account is None:
        raise_error(msg="akun tidak ditemukan")
        if picture is not None:
            temp_picture = str(uuid.uuid4()) + picture.filename.replace(" ", "")
            with open(PICTURE_FOLDER + temp_picture, "wb") as f:
                f.write(picture.file.read())
                json_object["picture"] = DOMAIN_FILE_URL + '/files/' + temp_picture
        if bank_book_photo is not None:
            temp_bank = str(uuid.uuid4()) + bank_book_photo.filename.replace(" ", "")
            with open(BANK_FOLDER + temp_bank, "wb") as f:
                f.write(bank_book_photo.file.read())
                json_object["bank_book_photo"] = DOMAIN_FILE_URL + '/files/' + temp_bank
        if id_card is not None:
            temp_card = str(uuid.uuid4()) + id_card.filename.replace(" ", "")
            with open(CARD_FOLDER + temp_card, "wb") as f:
                f.write(id_card.file.read())
                json_object["id_card"] = DOMAIN_FILE_URL + '/files/' + temp_card
    return repositoriesDB.update_profile(json_object=json_object, to_model=False)


def update_profile_id_user_db_admin(json_object={}):
    account = find_user_db_by_id(id=json_object["id"], to_model=True)
    if account is None:
        return None, "akun tidak ditemukan"
    return repositoriesDB.update_profile(json_object=json_object, to_model=False)


def logout_user_db(json_object={}):
    return repositoriesDB.reset_token_by_token(token=json_object['token'])


def get_profile_id_user_db(json_object={}):
    account = repositoriesDB.find_by_id(id=json_object["id"])
    if account is None:
        return
    account = account.to_response_profile()
    from entitas.schedule.services import get_mytraining_student
    from entitas.absent.services import get_all_absent_by_user_id
    account['trainings'], _ = get_mytraining_student(user_id=json_object["id"], limit=0)
    account['absents'] = get_all_absent_by_user_id(user_id=json_object["id"])
    return account


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


def update_school_name_in_user(school_id=None, school_name=""):
    return repositoriesDB.update_school_name(
        school_id=school_id, school_name=school_name
    )


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


def is_email_has_user(email=""):
    return repositoriesDB.is_email_has_user(email=email)


def refresh_token_authorization(authorization=None):
    authorization = authorization.split(' ')[1]
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

def update_menage_name_list_dbdb(json_object={}):
    return repositoriesDB.update_profile_menage_student_list(json_object=json_object)

