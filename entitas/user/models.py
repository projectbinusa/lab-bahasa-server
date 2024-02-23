class User:
    def __init__(
        self,
        id=0,
        email="",
        password="",
        name="",
        token="",
        hp="",
        active=False,
        last_login=None,
        role='',
        address="",
        picture="",
        created_date=None,
        updated_date=None,
        birth_date=None,
        birth_place='',
        firebase_token='',
        ws_id=''
    ):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.token = token
        self.last_login = last_login
        self.hp = hp
        self.picture = picture
        self.active = active
        self.role = role
        self.address = address
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.firebase_token = firebase_token
        self.ws_id = ws_id
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "name": self.name,
            "token": self.token,
            "last_login": str(self.last_login) if self.last_login is not None else None,
            "hp": self.hp,
            "picture": self.picture,
            "active": self.active,
            "role": self.role,
            "birth_date": str(self.birth_date) if self.birth_date is not None else None,
            "birth_place": self.birth_place,
            "firebase_token": self.firebase_token,
            "ws_id": self.ws_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response_login(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "token": self.token,
            "last_login": str(self.last_login) if self.last_login is not None else None,
            "picture": self.picture,
        }

    def to_response_profile(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "hp": self.hp,
            "address": self.address,
            "picture": self.picture,
            "birth_date": self.birth_date,
            "birth_place": self.birth_place,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "last_login": str(self.last_login) if self.last_login is not None else None,
            "hp": self.hp,
            "picture": self.picture,
            "active": self.active,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response_forgot(self):
        return {"email": self.email}


    def to_response_simple(self):
        return {
            "name": self.name,
            "email": self.email,
            "picture": "",
        }
