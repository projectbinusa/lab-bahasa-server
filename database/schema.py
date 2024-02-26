from datetime import date, datetime
from pony.orm import *
from entitas.user.models import User
from entitas.material.models import *
from util.db_util import db2
from config.config import DOMAIN_FILE_URL

# start User
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
# end User

# start Material
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
# end Material

# start Pathway
class PathwayDB(db2.entity):
    _table_ = "pathway"
    id = PrimaryKey(int, auto=True)
    name = Optional(str, nulllabel=True)
    description = Optional(str, nulllabel=True)
    created_date = Optional(datetime, nulllabel=True)
    updated_date = Optional(datetime, nulllabel=True)

    def to_model(self):
        item = Pathway()
        item.id = self.id
        item.name = self.name
        item.description = self.description
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item
# end Pathway

# start Absent
class AbsentDB(db2.entity):
    _table_ = "absent"
    id= PrimaryKey(int, auto=True)
    training_id= Optional(int, nullable=True)
    absent_date= Optional(datetime, nullable=True)
    user_id= Optional(str, nullable=True)
    status= Optional(str, nullable=True)
    description= Optional(str, nullable=True)
    created_date= Optional(datetime, nullable=True)
    updated_date= Optional(datetime, nullable=True)

    def to_model(self):
        item = Absent()
        item.id = self.id
        item.training_id = self.training_id
        item.absent_date = self.absent_date
        item.user_id = self.user_id
        item.status = self.status
        item.description = self.description
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item
# end Absent

class AssignmentDB(db2.entity):
    _table_ = "assignment"
    id= PrimaryKey (int, auto=True)
    scheduler_id= Optional(int, nullable=True)
    training_id= Optional(int, nullable=True)
    instructur_id= Optional(int, nullable=True)
    name= Optional(str, nullable=True)
    description= Optional(str, nullable=True)
    max_date= Optional(datetime, nullable=True)
    created_date= Optional(datetime, nullable=True)
    updated_date= Optional(datetime, nullable=True)

    def to_model(self):
        item = Assignment
        item.id = self.id
        scheduler_id = self.scheduler_id
        training_id = self.training_id
        instructur_id = self.instructur_id
        item.name = self.name
        item.description = self.description
        item.max_date = self.max_date
        item.created_date = self.created_date
        item.updated_date = self.updated_date

class Assignment_UserDB(db2.entity):
    _table_ = "assignment_user"
    id = PrimaryKey(int, auto=True)
    assignment_id = Optional(int, nullable=True)
    user_id = Optional(int, nullable=True)
    training_id = Optional(int, nullable=True)
    instructur_id = Optional(int, nullable=True)
    url_file = Optional(str, nullable=True)
    description = Optional(str, nullable=True)
    score = Optional(int, nullable=True)
    comment = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Assignment_User
        item.id = self.id
        item.assignment_id = self.assignment_id
        item.user_id = self.user_id
        item.training_id = self.training_id
        item.instructur_id = self.instructur_id
        item.url_file = self.url_file
        item.description = self.description
        item.score = self.score
        item.comment = self.comment
        item.created_date = self.created_date
        item.updated_date = self.updated_date

class CertificateDB(db2.entity):
    _table_ = "certificate"
    id = PrimaryKey(int, auto=True)
    scheduler_id = Optional(int, nullable=True)
    training_id = Optional(int, nullable=True)
    instructur_id = Optional(int, nullable=True)
    training_name = Optional(str, nullable=True)
    name = Optional(str, nullable=True)
    url_file = Optional(str, nullable=True)
    publish_date = Optional(datetime, nullable=True)
    score = Optional(int, nullable=True)
    mark = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Certificate
        item.id = self.id
        item.scheduler_id = self.scheduler_id
        item.training_id = self.training_id
        item.instructur_id = self.instructur_id
        item.training_name = self.training_name
        item.name = self.name
        item.url_file = self.url_file
        item.publish_date = self.publish_date
        item.score = self.score
        item.mark = self.mark
        item.created_date = self.created_date
        item.updated_date = self.updated_date

class CommentDB(db2.entity):
    _tale_ = "comment"
    id = PrimaryKey(int, auto=True)
    comment_for_id = Optional(int, nullable=True)
    is_deleted = Optional(int, nullable=True)
    message = Optional(str, nullable=True)
    room_id = Optional(id, nullable=True)
    room_meet = Optional(str, nullable=True)
    status = Optional(str, nullable=True)
    user_avatar_url = Optional(str, nullable=True)
    user_id = Optional(int, nullable=True)
    user_name = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Comment
        item.id = self.id
        item.comment_for_id = self.comment_for_id
        item.is_deleted = self.is_deleted
        item.message = self.message
        item.room_id = self.room_id
        item.room_name = self.room_name
        item.status = self.status
        item.user_avatar_url = self.user_avatar_url
        item.user_id = self.user_id
        item.user_name = self.user_name
        item.created_date = self.created_date
        item.updated_date = self.updated_date

class InstructurDB(db2.entity):
    _table_ = "instructur"
    id = PrimaryKey(int, auto=True)
    name = Optional(str, nullable=True)
    email = Optional(str, nullable=True)
    address = Optional(str, nullable=True)
    birth_date = Optional(datetime, nullable=True)
    birth_place = Optional(str, nullable=True)
    avatar_url = Optional(str, nullable=True)
    is_facilitator = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Instructur
        item.id = self.id
        item.name = self.name
        item.email = self.email
        item.address = self.address
        item.birth_date = self.birth_date
        item.birth_place = self.birth_place
        item.avatar_url = self.avatar_url
        item.is_facilitator = self.is_facilitator
        item.created_date = self.created_date
        item.updated_date = self.updated_date

class Notification(db2.entity):
    id = PrimaryKey(int, auto=True)
    fcm_token = Optional(str, nullable=True)
    email = Optional(str, nullable=True)
    user_id = Optional(int, nullable=True)
    title = Optional(str, nullable=True)
    message = Optional(int, nullable=True)
    status_id = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Notification
        item.id = self.id
        item.fcm_token = self.fcm_token
        item.email = self.email
        item.user_id = self.user_id
        item.title = self.title
        item.message = self.message
        item.status_id = self.status_id
        item.created_date = self.created_date
        item.updated_date = self.updated_date

class PathwayTrainingDB(db2.entity):
    _table_ = "pathway_training"
    id = PrimaryKey(int, auto=True)
    pathway_id = Optional(int, nullable=True)
    training_id = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    update_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Pathway_Training
        item.id = self.id
        item.pathway_id = self.pathway_id
        item.training_id = self.training_id
        item.created_date = self.created_date
        item.update_date = self.update_date

class PathwayUserDB(db2.entity):
    _table_ = "pathway_user"
    id = PrimaryKey(int, auto=True)
    pathway_id = Optional(int, nullable=True)
    user_id = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    update_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Pathway_Training
        item.id = self.id
        item.pathway_id = self.pathway_id
        item.user_id = self.user_id
        item.created_date = self.created_date
        item.update_date = self.update_date

class RoomDB(db2.entity):
    _table_ = "room"
    id = PrimaryKey(int, auto=True)
    name = Optional(str, nullable=True)
    avatar_url = Optional(str, nullable=True)
    is_removed = Optional(int, nullable=True)
    last_commment = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Room
        item.id = self.id
        item.name = self.name
        item.avatar_url = self.avatar_url
        item.is_removed = self.is_removed
        item.last_commment = self.last_commment
        item.created_date = self.created_date
        item.updated_date = self.updated_date

class RoomUSerDB(db2.entity):
    _table_ = "room_user"
    id = PrimaryKey(int, auto=True)
    room_id = Optional(int, nullable=True)
    user_id = Optional(int, nullable=True)
    last_comment_user = Optional(str, nullable=True)
    last_comment_text = Optional(str, nullable=True)
    last_comment_date = Optional(datetime, nullable=True)
    avatar_url = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Room_User
        item.id = self.id
        item.user_id = self.user_id
        item.room_id = self.room_id
        item.last_comment_user = self.last_comment_user
        item.last_comment_text = self.last_comment_text
        item.last_comment_date = self.last_comment_date
        item.avatar_url = self.avatar_url
        item.created_date = self.created_date
        item.updated_date = self.updated_date

class ScheduleDB(db2.entity):
    _table_ = "schedule"
    id = PrimaryKey(int, auto=True)
    training_id = Optional(int, nullable=True)
    link = Optional(str, nullable=True)
    is_online = Optional(int, nullable=True)
    location = Optional(str, nullable=True)
    start_date = Optional(datetime, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Schedule
        item.id = self.id
        item.training_id = self.training_id
        item.link = self.link
        item.is_online = self.is_online
        item.location = self.location
        item.start_date = self.start_date
        item.created_date = self.created_date
        item.updated_date = self.updated_date

class ScheduleInstructurDB(db2.entity):
    _table_ = "schedule_instructur"
    id = PrimaryKey(int, auto=True)
    schedule_id = Optional(int, nullable=True)
    instructur_id = Optional(int, nullable=True)
    instructur_name = Optional(str, nullable=True)
    is_deteted = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Schedule_instuctur
        item.id = self.id
        item.schedule_id = self.schedule_id
        item.instructur_id = self.instructur_id
        item.instructur_name = self.instructur_name
        item.is_deteted = self.is_deteted
        item.created_date = self.created_date
        item.updated_date = self.updated_date

class ScheduleUserDB(db2.entity):
    _table_ = "schedule_user"
    id = PrimaryKey(int, auto=True)
    schedule_id = Optional(int, nullable=True)
    user_id = Optional(int, nullable=True)
    user_name = Optional(str, nullable=True)
    is_deteted = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Schedule_User
        item.id = self.id
        item.schedule_id = self.schedule_id
        item.user_id = self.user_id
        item.user_name = self.user_name
        item.is_deteted = self.is_deteted
        item.created_date = self.created_date
        item.updated_date = self.updated_date

class TrainingDB(db2.entity):
    _table_ = "training"
    id = PrimaryKey(int, auto=True)
    name = Optional(str, nullable=True)
    description = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Training
        item.id = self.id
        item.name = self.name
        item.description = self.description
        item.created_date = self.created_date
        item.updated_date = self.updated_date

class TrainingMaterialDB(db2.entity):
    _table_ = "training_material"
    id = PrimaryKey(int, auto =True)
    training_id = Optional(int, nullable=True)
    material_id = Optional(int, nullable=True)
    is_user_access = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Training_Material
        item.id = self.id
        item.training_id = self.training_id
        item.material_id = self.material_id
        item.is_user_access = self.is_user_access
        item.created_date = self.created_date
        item.updated_date = self.updated_date

class TrainingUserDB(db2.entity):
    _table_ = "training_user"
    id = PrimaryKey(int, auto =True)
    training_id = Optional(int, nullable=True)
    user_id = Optional(int, nullable=True)
    is_active = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Training_user
        item.id = self.id
        item.training_id = self.training_id
        item.user_id = self.user_id
        item.is_active = self.is_active
        item.created_date = self.created_date
        item.updated_date = self.updated_date

if db2.schema is None:
    db2.generate_mapping(create_tables=False)