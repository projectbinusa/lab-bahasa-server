import datetime
import json
import uuid
from datetime import datetime, timedelta

from pony.orm import *

from database.schema import UserDB
from util.other_util import  raise_error
from util.other_util import encrypt_string


@db_session
def get_all(to_model=False, filters=[]):
    result = []
    try:
        if len(list(filter(lambda: item["field"] == "type", filters))) == 0:
            data_in_db = select(s for s in UserDB if s.fcm_token is not None)
        else:
            data_in_db = select(s for s in UserDB)

        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_json())

    except Exception as e:
        print("error UserDB getAll: ", e)
    return result

@db_session
def get_all_with_pagination(
    page=1,
    limit=9,
    to_model=False,
    filters=[],
    to_response="to_response",
    name=None,
):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in UserDB).order_by(desc(UserDB.id))
        for item in filters:
            if item["field"] == "email":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.email)
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.name)
            elif item["field"] == "hp":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.hp)
            elif item["field"] == "role":
                data_in_db = data_in_db.filter(lambda d: d.role == item["value"])
            elif item["field"] == "tag":
                data_in_db = data_in_db.filter(lambda d: d.tag == item["value"])
        if name:
            data_in_db = data_in_db.filter(lambda d: d.name == name)
        total_record = count(data_in_db)
        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                if to_response == "to_response_profile":
                    result.append(item.to_model().to_response_profile())
                else:
                    result.append(item.to_model().to_response())
    except Exception as e:
        print("error UserDB getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def get_all_with_pagination_managements(
    page=1,
    limit=9,
    to_model=False,
    filters=[],
    to_response="to_response",
    name=None,
):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in UserDB).order_by(desc(UserDB.id))
        for item in filters:
            if item["field"] == "client_ID":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.client_ID)
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: d.name in item["value"])
            elif item["field"] == "class_id":
                data_in_db = data_in_db.filter(lambda d: d.class_id == item["value"])
        if name:
            data_in_db = data_in_db.filter(lambda d: d.name == name)
        total_record = count(data_in_db)
        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                if to_response == "to_response_profile":
                    result.append(item.to_model().to_response_profile())
                else:
                    result.append(item.to_model().to_response_managements_list())
    except Exception as e:
        print("error UserDB getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in UserDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def find_by_list_id(list_id=[]):
    result = []
    for data_in_db in select(s for s in UserDB if s.id in list_id):
        result.append(data_in_db.to_model())
    return result


@db_session
def find_by_name(name="", to_model=False):
    try:
        if to_model:
            return UserDB.get(name=name).to_model()
        else:
            return UserDB.get(name=name).to_model().to_response()
    except Exception as e:
        print("error UserDB findByName: ", e)
        return None


@db_session
def update(json_object=None, to_model=False):
    if json_object is None:
        return None
    try:
        updated_user = UserDB[json_object["id"]]
        updated_user.role = json_object["role"]
        updated_user.address = json_object["address"]
        updated_user.name = json_object["name"]
        updated_user.hp = json_object["hp"]
        updated_user.email = json_object["email"]
        if 'nip' in json_object:
            updated_user.nip = json_object['nip']
        if 'tag' in json_object:
            updated_user.tag = ','.join(json_object['tag'])
        commit()
        if to_model:
            updated_user.to_model()
        else:
            return updated_user.to_model().to_response()
    except Exception as e:
        print("error Account update : ", e)
        return None


@db_session
def update_password(json_object=None, to_model=False):
    if json_object is None:
        return None
    try:
        updated_user = UserDB[json_object["id"]]
        updated_user.password = encrypt_string(json_object["new_password"])
        commit()
        if to_model:
            updated_user.to_model()
        else:
            return updated_user.to_model().to_response_login()
    except Exception as e:
        print("error Account update Password: ", e)
        return None


@db_session
def delete_by_id(id=None):
    try:
        UserDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("Error Account deleteById" + str(e))
    return None


@db_session
def insert(json_object={}, to_model=False):
    if 'description' not in json_object:
        json_object['description'] = ''
    if 'nip' not in json_object:
        json_object['nip'] = ''
    if 'tag' not in json_object:
        json_object['tag'] = ''
    try:
        new_user = UserDB(
            role=json_object["role"],
            address=json_object["address"],
            name=json_object["name"],
            hp=json_object["hp"],
            birth_date=json_object["birth_date"],
            birth_place=json_object["birth_place"],
            email=json_object["email"],
            picture=json_object["picture"],
            active=1,
            password=encrypt_string(json_object["new_password"]),
            token=str(uuid.uuid4()),
            description=json_object['description'],
            nip=json_object['nip'],
            tag=','.join(json_object['tag']),
            position=json_object['position'],
            agency=json_object['agency'],
            work_unit=json_object['work_unit'],
            city=json_object['city'],
            rank=json_object['rank'],
            npwp=json_object['npwp'],
            bank_name=json_object['bank_name'],
            bank_account=json_object['bank_account'],
            bank_in_name=json_object['bank_in_name'],
            bank_book_photo=json_object['bank_book_photo'],
            id_card=json_object['id_card'],
            signature=json_object['signature'],
            last_education=json_object['last_education'],
            # client_ID=json_object['client_ID'],
            # departement=json_object['departement'],
            # class_id=json_object['class_id'],
            # password_prompt=json_object['password_prompt'],
            # gender=json_object['gender']
        )
        commit()
        if to_model:
            return new_user.to_model()
        else:
            return new_user.to_model().to_response()
    except Exception as e:
        return None, "error UserDB insert: " + str(e)

@db_session
def signup(json_object={}):
    if 'description' not in json_object:
        json_object['description'] = ''
    if 'nip' not in json_object:
        json_object['nip'] = ''
    if 'tag' not in json_object:
        json_object['tag'] = ''
    else:
        tag = ",".join(json_object.get("tag").split(","))
        json_object['tag'] = tag
    UserDB(
        address=json_object["address"],
        name=json_object["name"],
        hp=json_object["hp"],
        birth_date=json_object["birth_date"],
        birth_place=json_object["birth_place"],
        email=json_object["email"],
        role=json_object["role"],
        active=1,
        password=encrypt_string(json_object["new_password"]),
        token=str(uuid.uuid4()),
        picture=json_object['picture'],
        description=json_object['description'],
        nip=json_object['nip'],
        # tag=','.join(json_object['tag']),
        tag=json_object['tag'],
        position=json_object['position'],
        agency=json_object['agency'],
        work_unit=json_object['work_unit'],
        city=json_object['city'],
        rank=json_object['rank'],
        npwp=json_object['npwp'],
        bank_name=json_object['bank_name'],
        bank_account=json_object['bank_account'],
        bank_in_name=json_object['bank_in_name'],
        bank_book_photo=json_object['bank_book_photo'],
        id_card=json_object['id_card'],
        signature=json_object['signature'],
        last_education=json_object['last_education'],
        # client_ID=json_object['client_ID'],
        # departement=json_object['departement'],
        # class_id=json_object['class_id'],
        # password_prompt=json_object['password_prompt'],
        # gender=json_object['gender']
    )
    commit()
    return True


@db_session
def post_login(json_object={}):
    # try:
        print('encrypt_string(json_object["password"]) ------>',encrypt_string(json_object["password"]))
        if json_object["email"] not in ["", "-"]:
            account_db = UserDB.get(
                email=json_object["email"],
                password=encrypt_string(json_object["password"]),
            )
        else:
            account_db = UserDB.get(
                hp=json_object["hp"], password=encrypt_string(json_object["password"])
            )
        if account_db is not None:
            account_db.token = str(uuid.uuid4())
            account_db.last_login = datetime.now()
            commit()
            return account_db.to_model()

    # except Exception as e:
    #     print("error UserDB post_login: ", e)
    # return None


@db_session
def find_by_token(token="", to_model=False):
    try:
        account = UserDB.get(token=token)
        if account is None:
            return None
        if to_model:
            return account.to_model()
        else:
            return account.to_model().to_response()
    except Exception as e:
        print("error UserDB find_by_token: " + str(e))
        return None



@db_session
def update_profile(json_object=None, to_model=False):
    try:
        updated_user = UserDB[json_object["id"]]
        if "name" in json_object:
            updated_user.name = json_object["name"]
        if "address" in json_object:
            updated_user.address = json_object["address"]
        if "hp" in json_object:
            updated_user.hp = json_object["hp"]
        if "picture" in json_object:
            updated_user.picture = json_object["picture"]
        if "birth_date" in json_object:
            updated_user.birth_date = json_object["birth_date"]
        if "birth_place" in json_object:
            updated_user.birth_place = json_object["birth_place"]
        if "description" in json_object:
            updated_user.description = json_object["description"]
        if 'nip' in json_object:
            updated_user.nip = json_object['nip']
        if 'tag' in json_object:
            tag = ",".join(json_object.get("tag").split(","))
            json_object['tag'] = tag
            updated_user.tag = json_object['tag']
        if 'position' in json_object:
            updated_user.position = json_object['position']
        if 'agency' in json_object:
            updated_user.agency = json_object['agency']
        if 'work_unit' in json_object:
            updated_user.work_unit = json_object['work_unit']
        if 'city' in json_object:
            updated_user.city = json_object['city']
        if 'rank' in json_object:
            updated_user.rank = json_object['rank']
        if 'npwp' in json_object:
            updated_user.npwp = json_object['npwp']
        if 'bank_name' in json_object:
            updated_user.bank_name = json_object['bank_name']
        if 'bank_account' in json_object:
            updated_user.bank_account = json_object['bank_account']
        if 'bank_in_name' in json_object:
            updated_user.bank_in_name = json_object['bank_in_name']
        if 'bank_book_photo' in json_object:
            updated_user.bank_book_photo = json_object['bank_book_photo']
        if 'id_card' in json_object:
            updated_user.id_card = json_object['id_card']
        if 'signature' in json_object:
            updated_user.signature = json_object['signature']
        if 'last_education' in json_object:
            updated_user.last_education = json_object['last_education']
        # if 'client_ID' in json_object:
        #     updated_user.client_ID = json_object['client_ID']
        # if 'departement' in json_object:
        #     updated_user.departement = json_object['departement']
        # if 'class_id' in json_object:
        #     updated_user.class_id = json_object['class_id']
        # if 'password_prompt' in json_object:
        #     updated_user.password_prompt = json_object['password_prompt']
        # if 'gender' in json_object:
        #     updated_user.gender = json_object['gender']

        commit()
        if to_model:
            return updated_user.to_model()
        else:
            return updated_user.to_model().to_response_profile()
    except Exception as e:
        print("error UserDB update_profile: " + str(e))
        return


@db_session
def get_profile(json_object=None, to_model=False):
    if json_object is None:
        return None
    try:
        updated_user = UserDB[json_object["id"]]
        if to_model:
            updated_user.to_model()
        else:
            return updated_user.to_model().to_response_profile()
    except Exception as e:
        print("error Account get_profile: ", e)
        return None


@db_session
def reset_token(json_object=None, to_model=False):
    if json_object is None:
        return None
    try:
        updated_user = UserDB[json_object["id"]]
        updated_user.token = ""
        commit()
        if to_model:
            updated_user.to_model()
        else:
            return updated_user.to_model().to_response()
    except Exception as e:
        print("error Account reset Token: ", e)
        return None

@db_session
def reset_token_by_token(token=None):
    if token is None:
        return
    data_in_db = select(s for s in UserDB if s.token == token)
    if data_in_db.first() is not None:
        data_in_db.first().token = ""
        commit()
        return True
    return

@db_session
def find_by_email(email="", to_model=False):
    try:
        account = UserDB.get(email=email)
        if account is None:
            return None
        if to_model:
            return account.to_model()
        else:
            return account.to_model().to_response()
    except Exception as e:
        print("error UserDB find_by_email: ", e)
        return None

@db_session
def is_email_user_exist(email=""):
    if select(s for s in UserDB if s.email == email).count() > 0:
        return True
    return False


@db_session
def update_password_by_email(email="", password=""):
    try:
        updated_user = UserDB.get(email=email)
        if updated_user is None:
            return None
        updated_user.password = encrypt_string(password)
        commit()
        return updated_user.to_model()
    except Exception as e:
        print("error update_password_by_email: ", e)
        return None


@db_session
def activate_user_by_email(email="", active=0, new_password=None):
    try:
        generated_token = str(uuid.uuid4())
        updated_user = UserDB.get(email=email)
        updated_user.active = active
        updated_user.token = generated_token
        if new_password is not None:
            updated_user.password = encrypt_string(new_password)
        commit()
        return updated_user.to_model()
    except Exception as e:
        print("error Account update activate_user_by_email: ", e)
        return None


@db_session
def activate_user_by_id(id=0, active=0, new_password=""):
    try:
        generated_token = str(uuid.uuid4())
        updated_user = UserDB.get(id=id)
        updated_user.active = active
        updated_user.password = encrypt_string(new_password)
        updated_user.token = generated_token
        commit()
        return updated_user.to_model()
    except Exception as e:
        print("error Account update activate_user_by_email: ", e)
        return None


@db_session
def update_email_by_id(id=0, email=""):
    try:
        update_email = UserDB[id]
        update_email.email = email
        update_email.token = ""
        commit()
    except Exception as e:
        print("error update_email_by_id", e)
    return


@db_session
def find_by_email(email="", to_model=False):
    data_in_db = select(s for s in UserDB if s.email == email)
    if data_in_db.first() is None:
        return
    if to_model:
        return data_in_db.first().to_model()
    return data_in_db.first().to_model().to_response()

@db_session
def is_email_has_user(email=""):
    if select(s for s in UserDB if s.email == email).count() > 0:
        return True
    return False

@db_session
def get_all_with_pagination_managements(
    page=1,
    limit=9,
    to_model=False,
    filters=[],
    to_response="to_response",
    name=None,
):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in UserDB).order_by(desc(UserDB.id))
        for item in filters:
            if item["field"] == "client_ID":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.client_ID)
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: d.name in item["value"])
            elif item["field"] == "class_id":
                data_in_db = data_in_db.filter(lambda d: d.class_id == item["value"])
        if name:
            data_in_db = data_in_db.filter(lambda d: d.name == name)
        total_record = count(data_in_db)
        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                if to_response == "to_response_profile":
                    result.append(item.to_model().to_response_profile())
                else:
                    result.append(item.to_model().to_response_managements_list())
    except Exception as e:
        print("error UserDB getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }

@db_session
def delete_management_name_list_by_id(id=None):
    try:
        UserDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error User delete: ", e)
    return

@db_session
def update_profile_manage_student_list(json_object=None, to_model=False):
    try:
        updated_user = UserDB[json_object["id"]]
        if "name" in json_object:
            updated_user.name = json_object["name"]
        if "gender" in json_object:
            updated_user.gender = json_object["gender"]
        if "departement" in json_object:
            updated_user.departement = json_object["departement"]
        if "client_ID" in json_object:
            updated_user.student_id = json_object["client_ID"]
        if "class_id" in json_object:
            updated_user.class_id = json_object["class_id"]
        if "password" in json_object:
            updated_user.password = json_object["password"]
        if "password_prompt" in json_object:
            updated_user.password_prompt = json_object["password_prompt"]

        commit()

        if to_model:
            return updated_user.to_model()
        else:
            return updated_user.to_model().to_response_managements_list()
    except Exception as e:
        print("error UserDB update_profile: " + str(e))
        return

@db_session
def create_profile_manage_student_list(json_object=None, to_model=False):
    try:
        name = json_object.get("name")
        gender = json_object.get("gender")
        departement = json_object.get("departement")
        client_ID = json_object.get("client_ID")
        class_id = json_object.get("class_ID")
        password = json_object.get("password")
        password_prompt = json_object.get("password_prompt")

        new_user = UserDB(
            name=name,
            gender=gender,
            departement=departement,
            client_ID=client_ID,
            class_id=class_id,
            password=password,
            password_prompt=password_prompt
        )

        commit()

        if to_model:
            return new_user.to_model()
        else:
            return new_user.to_model().to_response_managements_list()
    except Exception as e:
        print("error creating profile: " + str(e))
        return None
