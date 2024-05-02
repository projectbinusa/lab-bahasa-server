import os
userDB = os.environ["userDB"]
passwordDB = os.environ["passwordDB"]
hostDB = os.environ["hostDB"]
portDB = int(os.environ["portDB"])
dbName = os.environ["dbName"]
dbDebug = False
if os.environ["dbDebug"].strip().upper() == "TRUE":
    dbDebug = True

secret_jwt = os.environ["secret_jwt"]
driverDB = os.environ["driverDB"]
TYPE_TOKEN_USER = 'user'
DOMAIN_FILE_URL = 'https://file-event.lynk2.co'
SALT_SORTER = 'rahasiademak'
MATERIAL_FOLDER = 'files/'
LOG_BOOK_FOLDER = 'files/'
CERTIFICATE_FOLDER = 'files/'
ASSIGNMENT_FOLDER = 'files/'
SIGNATURE_FOLDER = 'files/'
LINK_MEET = os.environ["LINK_MEET"]