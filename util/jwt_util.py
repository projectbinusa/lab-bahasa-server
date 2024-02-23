from datetime import datetime, timedelta

import jwt

from config.config import secret_jwt, dbName


def portprq_auth(payload):
    window = timedelta(seconds=3)
    now = datetime.utcnow()
    if now - datetime.utcfromtimestamp(payload["exp"]) >= window:
        return None
    # from entitas.user.services import is_token_valid
    # if not is_token_valid(id=payload['id'], token=payload['token']):
    #     return None
    return payload


def jwt_encode(user_info=None, type_token='user'):
    if user_info["token"] != "":
        # user_info["exp"] = int((datetime.utcnow() + timedelta(days=7)).timestamp())
        user_info['refresh_token'] = refresh_jwt_encode(refresh_user_info=user_info)
        if 'dev' in dbName:
            user_info["exp"] = int((datetime.now() + timedelta(days=1)).timestamp())
        else:
            user_info["exp"] = int((datetime.now() + timedelta(days=7)).timestamp())
        user_info["type_token"] = type_token
        if "type" in user_info and user_info["type"] == "teacher":
            user_info["role_id"] = 0
        try:
            user_info["token"] = jwt.encode(
                user_info, secret_jwt, algorithm="HS512"
            ).decode("utf-8")
        except:
            user_info["token"] = jwt.encode(user_info, secret_jwt, algorithm="HS512")
        if "role_id" in user_info:
            del user_info["role_id"]
        if 'refresh_token' in user_info:
            del user_info['refresh_token']
    return user_info

def refresh_jwt_encode(refresh_user_info=None):
    if dbName in ["gk2dev"]:    
        refresh_user_info["exp"] = int((datetime.now() + timedelta(days=7)).timestamp())
    elif dbName in ["gk2", "gk2demo"]:    
        refresh_user_info["exp"] = int((datetime.now() + timedelta(days=30)).timestamp())
    refresh_user_info["type_token"] = "refresh_token"
    refresh_user_info["refresh_token"] = jwt.encode(refresh_user_info, secret_jwt, algorithm="HS512")
    return refresh_user_info['refresh_token']

def check_valid_email(email=""):
    import re

    regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
    return re.search(regex, email)

def check_valid_hp(hp=""):
    import re
    regex = "(\+62 ((\d{3}([ -]\d{3,})([- ]\d{4,})?)|(\d+)))|(\(\d+\) \d+)|\d{3}( \d+)+|(\d+[ -]\d+)|\d+"
    return re.search(regex, hp)
