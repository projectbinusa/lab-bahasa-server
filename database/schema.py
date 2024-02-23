from datetime import date, datetime
from pony.orm import *
from entitas.user.models import User
from entitas.material.models import Material
from util.db_util import db2
from config.config import DOMAIN_FILE_URL

class UserDB(db2.Entity):
    _table_ = "user"
    id = PrimaryKey(int, auto=True)
    name = Optional(str, nullable=True)
    address = Optional(str, nullable=True)
    hp = Optional(str, nullable=True)
    email = Optional(str, nullable=True)
    password = Optional(str, nullable=True)
    token = Optional(str, nullable=True)
    last_login = Optional(datetime, nullable=True)
    birth_date = Optional(datetime, nullable=True)
    birth_place = Optional(str, nullable=True)
    firebase_token = Optional(str, nullable=True)
    ws_id = Optional(str, nullable=True)
    active = Optional(int, nullable=True)
    picture = Optional(str, 1000, nullable=True)
    role = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = User()
        item.id = self.id
        item.name = self.name
        item.address = self.address
        item.hp = self.hp
        item.email = self.email
        item.password = self.password
        item.token = self.token
        item.last_login = self.last_login
        item.birth_date = self.birth_date
        item.birth_place = self.birth_place
        item.firebase_token = self.firebase_token
        item.ws_id = self.ws_id
        item.active = self.active
        item.picture = self.picture
        item.role = self.role
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item

class MaterialDB(db2.Entity):
    _table_ = "material"
    id = PrimaryKey(int, auto=True)
    user_id = Optional(int, nullable=True)
    filename = Optional(str, nullable=True)
    description = Optional(str, nullable=True)
    url_file = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Material()
        item.id = self.id
        item.user_id = self.user_id
        item.filename = self.filename
        item.description = self.description
        item.url_file = self.url_file
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item

if db2.schema is None:
    db2.generate_mapping(create_tables=False)
