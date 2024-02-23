from pony.orm import *

from config import config

db_traffic = Database()
db_traffic.bind(
    config.driverDB,
    host=config.hostDB,
    user=config.userDB,
    passwd=config.passwordDB,
    db=config.TraficdbName,
    charset="utf8mb4",
)

from datetime import date, datetime

from entitas.traffic.models import Traffic
from entitas.log_error.models import LogError


class TrafficDB(db_traffic.Entity):
    _table_ = "traffic"
    id = PrimaryKey(int, auto=True)
    timestamp = Optional(datetime, nullable=True)
    sessionId = Optional(str, nullable=True)
    user = Optional(str, nullable=True)
    isRequest = Optional(bool, nullable=True)
    url = Optional(str, nullable=True)
    host = Optional(str, nullable=True)
    method = Optional(str, nullable=True)
    statusCode = Optional(str, nullable=True)
    payload = Optional(str, 1000000, nullable=True)
    duration = Optional(float, nullable=True)
    url_page = Optional(str, 255, nullable=True)
    action = Optional(str, 255, nullable=True)
    mem_usage = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Traffic()
        item.id = self.id
        item.timestamp = self.timestamp
        item.sessionId = self.sessionId
        item.user = self.user
        item.isRequest = self.isRequest
        item.url = self.url
        item.host = self.host
        item.method = self.method
        item.statusCode = self.statusCode
        item.payload = self.payload
        item.duration = self.duration
        item.url_page = self.url_page
        item.action = self.action
        item.mem_usage = self.mem_usage
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item

class LogErrorDB(db_traffic.Entity):
    _table_ = "log_error"
    id = PrimaryKey(int, auto=True)
    timestamp = Optional(datetime, nullable=True)
    user = Optional(str,nullable=True)
    url = Optional(str,nullable=True)
    host = Optional(str,nullable=True)
    method = Optional(str,nullable=True)
    statusCode = Optional(str,nullable=True)
    payload = Optional(str, 1000000, nullable=True)
    duration = Optional(float,nullable=True)
    url_page = Optional(str,nullable=True)
    action = Optional(str,nullable=True)
    token_jwt = Optional(str, 100000, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = LogError()
        item.id = self.id
        item.timestamp = self.timestamp
        item.user = self.user
        item.url = self.url
        item.host = self.host
        item.method = self.method
        item.statusCode = self.statusCode
        item.payload = self.payload
        item.duration = self.duration
        item.url_page = self.url_page
        item.action = self.action
        item.token_jwt = self.token_jwt
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item

if db_traffic.schema is None:
    db_traffic.generate_mapping(create_tables=False)
