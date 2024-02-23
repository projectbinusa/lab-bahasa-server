from pony.orm import *

from config import config


def db():
    db = Database()
    db.bind(
        config.driverDB,
        host=config.hostDB,
        user=config.userDB,
        passwd=config.passwordDB,
        db=config.dbName,
    )

    sql_debug(config.dbDebug)
    return db


def dbcon():
    db3 = Database()
    db3.bind(
        config.driverDB,
        host=config.hostDB,
        user=config.userDB,
        passwd=config.passwordDB,
        db=config.dbName,
        charset="utf8mb4",
    )
    return db3


db2 = Database()
db2.bind(
    config.driverDB,
    host=config.hostDB,
    user=config.userDB,
    passwd=config.passwordDB,
    db=config.dbName,
    charset="utf8mb4",
)
sql_debug(config.dbDebug)

mysql_config = {
    'user': config.userDB,
    'password': config.passwordDB,
    'host': config.hostDB,
    'charset': "utf8mb4",
    'raise_on_warnings': True,

}
