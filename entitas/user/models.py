class User:
    def __init__(
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
            last_login='',
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
            bank_in_name='',
            bank_photo_book='',
            id_card='',
            signature='',
            last_education='',
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
        self.bank_photo_book = bank_photo_book
        self.id_card = id_card
        self.signature = signature
        self.last_education = last_education
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
            "activate": self.activate,
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
            "bank_book_photo": self.bank_photo_book,
            "id_card": self.id_card,
            "signature": self.signature,
            "last_education": self.last_education,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response_login(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
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
            "activate": self.activate,
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
            "bank_book_photo": self.bank_photo_book,
            "id_card": self.id_card,
            "signature": self.signature,
            "last_education": self.last_education
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
            "activate": self.activate,
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
            "bank_book_photo": self.bank_photo_book,
            "id_card": self.id_card,
            "signature": self.signature,
            "last_education": self.last_education,
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
