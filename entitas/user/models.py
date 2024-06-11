class User:
    def init(
            self,
            id=0,
            name='',
            email='',
            password='',
            address='',
            birth_date='',
            role='',
            birth_place='',
            picture='',
            firebase_token='',
            ws_id=0,
            activate='',
            last_login=None,
            hp='',
            token='',
            description='',
            nip='',
            tag='',
            position='',
            agency='',
            work_unit='',
            city='',
            rank='',
            npwp='',
            bank_name='',
            bank_account='',
            comment='',
            bank_in_name='',
            id_card='',
            signature='',
            last_education='',
            client_id='',
            departement='',
            class_id=0,
            password_prompt='',
            gender='',
            reset_code='',
            code_expiry=None,
            signed_time=None,
            bank_book_photo='',
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.birth_date = birth_date
        self.role = role
        self.birth_place = birth_place
        self.picture = picture
        self.firebase_token = firebase_token
        self.ws_id = ws_id
        self.activate = activate
        self.comment = comment
        self.last_login = last_login
        self.hp = hp
        self.token = token
        self.description = description
        self.nip = nip
        self.tag = tag
        self.position = position
        self.agency = agency
        self.work_unit = work_unit
        self.city = city
        self.rank = rank
        self.npwp = npwp
        self.bank_name = bank_name
        self.bank_account = bank_account
        self.bank_in_name = bank_in_name
        self.bank_book_photo = bank_book_photo
        self.id_card = id_card
        self.signature = signature
        self.last_education = last_education
        self.client_id = client_id
        self.departement = departement
        self.class_id = class_id
        self.password_prompt = password_prompt
        self.gender = gender
        self.reset_code = reset_code
        self.code_expiry = code_expiry
        self.signed_time = signed_time
        self.bank_book_photo = bank_book_photo
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "address": self.address,
            "birth_date": str(self.birth_date) if self.birth_date is not None else None,
            "role": self.role,
            "birth_place": self.birth_place,
            "picture": self.picture,
            "firebase_token": self.firebase_token,
            "ws_id": self.ws_id,
            # "activate": self.activate,
            "last_login": str(self.last_login) if self.last_login is not None else None,
            "token": self.token,
            "description": self.description,
            "nip": self.nip,
            "tag": self.tag.split(',') if self.tag not in [None, ''] else [],
            "position": self.position,
            "agency": self.agency,
            "work_unit": self.work_unit,
            "city": self.city,
            "rank": self.rank,
            "npwp": self.npwp,
            "bank_name": self.bank_name,
            "bank_account": self.bank_account,
            "bank_in_name": self.bank_in_name,
            "bank_book_photo": self.bank_book_photo,
            "id_card": self.id_card,
            "signature": self.signature,
            "last_education": self.last_education,
            "client_id": self.client_id,
            "departement": self.departement,
            "class_id": self.class_id,
            "password_prompt": self.password_prompt,
            "gender": self.gender,
            "signed_time": str(self.signed_time) if self.signed_time is not None else None,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }
    def to_response_login(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "class_id": self.class_id,
            "last_login": str(self.last_login) if self.last_login is not None else None,
            "token": self.token,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response_profile(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "birth_date": str(self.birth_date) if self.birth_date is not None else None,
            "role": self.role,
            "birth_place": self.birth_place,
            "picture": self.picture,
            # "activate": self.activate,
            "description": self.description,
            "last_login": str(self.last_login) if self.last_login is not None else None,
            "hp": self.hp,
            "nip": self.nip,
            "tag": self.tag.split(',') if self.tag not in [None, ''] else [],
            "position": self.position,
            "agency": self.agency,
            "work_unit": self.work_unit,
            "city": self.city,
            "rank": self.rank,
            "npwp": self.npwp,
            "bank_name": self.bank_name,
            "bank_account": self.bank_account,
            "bank_in_name": self.bank_in_name,
            # "bank_book_photo": self.bank_book_photo,
            "id_card": self.id_card,
            "signature": self.signature,
            "last_education": self.last_education,
            "client_id": self.client_id,
            "departement": self.departement,
            "class_id": self.class_id,
            "password_prompt": self.password_prompt,
            "gender": self.gender,
            "signed_time": self.signed_time
        }

    def to_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "address": self.address,
            "birth_date": str(self.birth_date) if self.birth_date is not None else None,
            "role": self.role,
            "birth_place": self.birth_place,
            "picture": self.picture,
            # "activate": self.activate,
            "last_login": str(self.last_login) if self.last_login is not None else None,
            "hp": self.hp,
            "token": self.token,
            "description": self.description,
            "nip": self.nip,
            "tag": self.tag.split(',') if self.tag not in [None, ''] else [],
            "position": self.position,
            "agency": self.agency,
            "work_unit": self.work_unit,
            "city": self.city,
            "rank": self.rank,
            "npwp": self.npwp,
            "bank_name": self.bank_name,
            "bank_account": self.bank_account,
            "bank_in_name": self.bank_in_name,
            "bank_book_photo": self.bank_book_photo,
            "id_card": self.id_card,
            "signature": self.signature,
            "last_education": self.last_education,
            "client_id": self.client_id,
            "departement": self.departement,
            "class_id": self.class_id,
            "password_prompt": self.password_prompt,
            "gender": self.gender,
            "signed_time": str(self.signed_time) if self.signed_time is not None else None,
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
            "description": self.description
        }
    def to_response_participant_schedule(self):
        return {
            "name": self.name,
            "email": self.email,
            "hp": self.hp,
            "position": self.position,
            "work_unit": self.work_unit,
            "city": self.city
        }

    def to_response_managements_list(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "name": self.name,
            "email": self.email,
            "gender": self.gender,
            "departement": self.departement,
            "class_id": self.class_id,
            "password_prompt": self.password_prompt,
            "password": self.password,
        }
    def to_response_guru(self):
        return {
            "email": self.email,
            "password": self.password
        }



def to_response_menage(self):
    return {
        "id": self.id,
        "name": self.name,
        "email": self.email,
        "role": self.role,
        "class_id": self.class_id,
        "client_id": self.client_id,
        "gender": self.gender,
        "departement": self.departement,
        "password": self.password,
        "password_prompt": self.password_prompt,
        "last_login": str(self.last_login) if self.last_login is not None else None,
        "created_date": str(self.created_date) if self.created_date is not None else None,
        "updated_date": str(self.updated_date) if self.updated_date is not None else None,
    }


def to_response_get_sigin_student(self):
    return {
        "id": self.id,
        "name": self.name,
        "email": self.email,
        "password": self.password,
        "address": self.address,
        "client_id": self.client_id,
        "departement": self.departement,
        "class_id": self.class_id,
        "comment": self.comment,
        "password_prompt": self.password_prompt,
        "gender": self.gender,
        "signed_time": str(self.signed_time) if self.signed_time is not None else None,
        "created_date": str(self.created_date) if self.created_date is not None else None,
        "updated_date": str(self.updated_date) if self.updated_date is not None else None,
    }