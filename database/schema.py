from datetime import date, datetime
from pony.orm import *

from entitas.kelas_user.models import KelasUser
from entitas.log_book.models import LogBook
from entitas.material.models import Material
from entitas.absent.models import Absent
from entitas.assignment.models import Assignment
from entitas.assignment_user.models import Assignment_User
from entitas.certificate.models import Certificate
from entitas.comment.models import Comment
from entitas.instructur.models import Instructur
from entitas.notification.models import Notification
from entitas.pathway.models import Pathway
from entitas.pathway_user.models import Pathway_User
from entitas.pathway_training.models import Pathway_Training
from entitas.room.models import Room
from entitas.announcement.models import Announcement
from entitas.room_user.models import Room_User
from entitas.schedule.models import Schedule
from entitas.schedule_instructur.models import Schedule_instuctur
from entitas.schedule_user.models import Schedule_User
from entitas.training.models import Training
from entitas.training_user.models import Training_user
from entitas.user.models import User
from entitas.training_material.models import Training_Material
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
    birth_date = Optional(date, nullable=True)
    birth_place = Optional(str, nullable=True)
    firebase_token = Optional(str, nullable=True)
    ws_id = Optional(str, nullable=True)
    active = Optional(int, nullable=True)
    picture = Optional(str, 1000, nullable=True)
    role = Optional(str, nullable=True)
    description = Optional(str, 100000, nullable=True)
    nip = Optional(str, nullable=True)
    tag = Optional(str, nullable=True)
    position= Optional(str, nullable=True)
    agency= Optional(str, nullable=True)
    work_unit= Optional(str, nullable=True)
    city= Optional(str, nullable=True)
    rank= Optional(str, nullable=True)
    npwp= Optional(str, nullable=True)
    bank_name= Optional(str, nullable=True)
    bank_account= Optional(str, nullable=True)
    bank_in_name= Optional(str, nullable=True)
    bank_book_photo= Optional(str, nullable=True)
    id_card= Optional(str, nullable=True)
    signature= Optional(str, nullable=True)
    last_education= Optional(str, nullable=True)
    client_ID= Optional(str, nullable=True)
    departemen= Optional(str, nullable=True)
    class_id= Optional(str, nullable=True)
    password_prompt= Optional(str, nullable=True)
    gender= Optional(str, nullable=True)
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
        item.description = self.description
        item.nip = self.nip
        item.tag = self.tag
        item.position = self.position
        item.agency = self.agency
        item.work_unit = self.work_unit
        item.city = self.city
        item.rank = self.rank
        item.npwp = self.npwp
        item.bank_name = self.bank_name
        item.bank_in_name = self.bank_in_name
        item.bank_account = self.bank_account
        item.bank_book_photo = self.bank_book_photo
        item.id_card = self.id_card
        item.signature = self.signature
        item.last_education = self.last_education
        item.client_ID = self.client_ID
        item.departemen = self.departemen
        item.class_id = self.class_id
        item.password_prompt = self.password_prompt
        item.gender = self.gender
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


# end User


# start Material
class MaterialDB(db2.Entity):
    _table_ = "material"
    id = PrimaryKey(int, auto=True)
    name = Optional(str, nullable=True)
    user_id = Optional(int, nullable=True)
    filename = Optional(str, nullable=True)
    description = Optional(str, nullable=True)
    url_file = Optional(str, nullable=True)
    other_link = Optional(str, nullable=True)
    tag = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Material()
        item.id = self.id
        item.name = self.name
        item.user_id = self.user_id
        item.name = self.name
        item.filename = self.filename
        item.description = self.description
        item.url_file = self.url_file
        item.other_link = self.other_link
        item.tag = self.tag
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


# end Material

# start Pathway
class PathwayDB(db2.Entity):
    _table_ = "pathway"
    id = PrimaryKey(int, auto=True)
    name = Optional(str, nullable=True)
    description = Optional(str, nullable=True)
    deleted = Optional(bool, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Pathway()
        item.id = self.id
        item.name = self.name
        item.description = self.description
        item.deleted = self.deleted
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


# end Pathway

# start Absent
class AbsentDB(db2.Entity):
    _table_ = "absent"
    id = PrimaryKey(int, auto=True)
    training_id = Optional(int, nullable=True)
    training_name = Optional(str, nullable=True)
    schedule_id = Optional(int, nullable=True)
    absent_date = Optional(datetime, nullable=True)
    user_id = Optional(int, nullable=True)
    user_name = Optional(str, nullable=True)
    status = Optional(int, nullable=True)
    description = Optional(str, nullable=True)
    location = Optional(str, nullable=True)
    signature = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Absent()
        item.id = self.id
        item.training_id = self.training_id
        item.training_name = self.training_name
        item.schedule_id = self.schedule_id
        item.absent_date = self.absent_date
        item.user_id = self.user_id
        item.user_name = self.user_name
        item.status = self.status
        item.description = self.description
        item.location = self.location
        item.signature = self.signature
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


# end Absent

class AssignmentDB(db2.Entity):
    _table_ = "assignment"
    id = PrimaryKey(int, auto=True)
    schedule_id = Optional(int, nullable=True)
    training_id = Optional(int, nullable=True)
    instructur_id = Optional(int, nullable=True)
    name = Optional(str, nullable=True)
    description = Optional(str, nullable=True)
    max_date = Optional(datetime, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Assignment()
        item.id = self.id
        item.schedule_id = self.schedule_id
        item.training_id = self.training_id
        item.instructur_id = self.instructur_id
        item.name = self.name
        item.description = self.description
        item.max_date = self.max_date
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


class Assignment_UserDB(db2.Entity):
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
        item = Assignment_User()
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
        return item


class CertificateDB(db2.Entity):
    _table_ = "certificate"
    id = PrimaryKey(int, auto=True)
    schedule_id = Optional(int, nullable=True)
    training_id = Optional(int, nullable=True)
    user_id = Optional(int, nullable=True)
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
        item = Certificate()
        item.id = self.id
        item.schedule_id = self.schedule_id
        item.training_id = self.training_id
        item.instructur_id = self.instructur_id
        item.user_id = self.user_id
        item.training_name = self.training_name
        item.name = self.name
        item.url_file = self.url_file
        item.publish_date = self.publish_date
        item.score = self.score
        item.mark = self.mark
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


class CommentDB(db2.Entity):
    _table_ = "comment"
    id = PrimaryKey(int, auto=True)
    comment_for_id = Optional(int, nullable=True)
    is_deleted = Optional(int, nullable=True)
    message = Optional(str, nullable=True)
    room_id = Optional(int, nullable=True)
    room_name = Optional(str, nullable=True)
    status = Optional(str, nullable=True)
    user_avatar_url = Optional(str, nullable=True)
    user_id = Optional(int, nullable=True)
    user_name = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Comment()
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
        return item


class InstructurDB(db2.Entity):
    _table_ = "instructur"
    id = PrimaryKey(int, auto=True)
    name = Optional(str, nullable=True)
    email = Optional(str, nullable=True)
    address = Optional(str, nullable=True)
    birth_date = Optional(date, nullable=True)
    birth_place = Optional(str, nullable=True)
    avatar_url = Optional(str, nullable=True)
    is_facilitator = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Instructur()
        item.id = self.id
        item.name = self.name
        item.email = self.email
        item.address = self.address
        item.birth_date = self.birth_date.isoformat() if self.birth_date else None
        item.birth_place = self.birth_place
        item.avatar_url = self.avatar_url
        item.is_facilitator = self.is_facilitator
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


class NotificationDB(db2.Entity):
    _table_ = "notification"
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
        item = Notification()
        item.id = self.id
        item.fcm_token = self.fcm_token
        item.email = self.email
        item.user_id = self.user_id
        item.title = self.title
        item.message = self.message
        item.status_id = self.status_id
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


class PathwayTrainingDB(db2.Entity):
    _table_ = "pathway_training"
    id = PrimaryKey(int, auto=True)
    pathway_id = Optional(int, nullable=True)
    training_id = Optional(int, nullable=True)
    training_name = Optional(str, nullable=True)
    urut = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Pathway_Training()
        item.id = self.id
        item.pathway_id = self.pathway_id
        item.training_id = self.training_id
        item.training_name = self.training_name
        item.urut = self.urut
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


class PathwayUserDB(db2.Entity):
    _table_ = "pathway_user"
    id = PrimaryKey(int, auto=True)
    pathway_id = Optional(int, nullable=True)
    pathway_name = Optional(str, nullable=True)
    user_id = Optional(int, nullable=True)
    user_name = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Pathway_User()
        item.id = self.id
        item.pathway_id = self.pathway_id
        item.pathway_name = self.pathway_name
        item.user_id = self.user_id
        item.user_name = self.user_name
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


class RoomDB(db2.Entity):
    _table_ = "room"
    id = PrimaryKey(int, auto=True)
    name = Optional(str, nullable=True)
    avatar_url = Optional(str, nullable=True)
    is_removed = Optional(int, nullable=True)
    last_comment = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Room()
        item.id = self.id
        item.name = self.name
        item.avatar_url = self.avatar_url
        item.is_removed = self.is_removed
        item.last_comment = self.last_comment
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item

class AnnouncementDB(db2.Entity):
    _table_ = "announcement"
    id = PrimaryKey(int, auto=True)
    name = Optional(str, nullable=True)
    is_published = Optional(bool, nullable=True)
    description = Optional(str, 10000, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Announcement()
        item.id = self.id
        item.name = self.name
        item.is_published = self.is_published
        item.description = self.description
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


class RoomUserDB(db2.Entity):
    _table_ = "room_user"
    id = PrimaryKey(int, auto=True)
    room_id = Optional(int, nullable=True)
    user_id = Optional(int, nullable=True)
    last_comment_user_id = Optional(str, nullable=True)
    last_comment_text = Optional(str, nullable=True)
    last_comment_date = Optional(datetime, nullable=True)
    avatar_url = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Room_User()
        item.id = self.id
        item.user_id = self.user_id
        item.room_id = self.room_id
        item.last_comment_user_id = self.last_comment_user_id
        item.last_comment_text = self.last_comment_text
        item.last_comment_date = self.last_comment_date
        item.avatar_url = self.avatar_url
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item

class ScheduleDB(db2.Entity):
    _table_ = "schedule"
    id = PrimaryKey(int, auto=True)
    name = Optional(str, nullable=True)
    training_id = Optional(int, nullable=True)
    training_name = Optional(str, nullable=True)
    training_image_url = Optional(str, nullable=True)
    link = Optional(str, nullable=True)
    other_link = Optional(str, nullable=True)
    is_online = Optional(int, nullable=True)
    location = Optional(str, nullable=True)
    active = Optional(int, nullable=True)
    is_finish = Optional(bool, nullable=True)
    start_date = Optional(datetime, nullable=True)
    end_date = Optional(datetime, nullable=True)
    pic_wa = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Schedule()
        item.id = self.id
        item.name = self.name
        item.training_id = self.training_id
        item.training_name = self.training_name
        item.training_image_url = self.training_image_url
        item.link = self.link
        item.other_link = self.other_link
        item.is_online = self.is_online
        item.location = self.location
        item.active = self.active
        item.start_date = self.start_date
        item.end_date = self.end_date
        item.is_finish = self.is_finish
        item.pic_wa = self.pic_wa
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item

class ScheduleInstructurDB(db2.Entity):
    _table_ = "schedule_instructur"
    id = PrimaryKey(int, auto=True)
    schedule_id = Optional(int, nullable=True)
    user_id = Optional(int, nullable=True)
    user_name = Optional(str, nullable=True)
    is_deleted = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Schedule_instuctur()
        item.id = self.id
        item.schedule_id = self.schedule_id
        item.user_id = self.user_id
        item.user_name = self.user_name
        item.is_deleted = self.is_deleted
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


class ScheduleUserDB(db2.Entity):
    _table_ = "schedule_user"
    id = PrimaryKey(int, auto=True)
    schedule_id = Optional(int, nullable=True)
    user_id = Optional(int, nullable=True)
    user_name = Optional(str, nullable=True)
    in_absent = Optional(str, nullable=True)
    out_absent = Optional(str, nullable=True)
    is_deleted = Optional(bool, nullable=True)
    score = Optional(int, nullable=True)
    certificate_url = Optional(str, nullable=True)
    confirmed = Optional(bool, nullable=True)
    kritik = Optional(str, nullable=True)
    saran = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Schedule_User()
        item.id = self.id
        item.schedule_id = self.schedule_id
        item.user_id = self.user_id
        item.user_name = self.user_name
        item.in_absent = self.in_absent
        item.out_absent = self.out_absent
        item.is_deleted = self.is_deleted
        item.score = self.score
        item.certificate_url = self.certificate_url
        item.confirmed = self.confirmed
        item.kritik = self.kritik
        item.saran = self.saran
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


class TrainingDB(db2.Entity):
    _table_ = "training"
    id = PrimaryKey(int, auto=True)
    name = Optional(str, nullable=True)
    description = Optional(str, nullable=True)
    image_url = Optional(str, nullable=True)
    tag = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Training()
        item.id = self.id
        item.name = self.name
        item.description = self.description
        item.image_url = self.image_url
        item.tag = self.tag
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


class TrainingMaterialDB(db2.Entity):
    _table_ = "training_material"
    id = PrimaryKey(int, auto=True)
    training_id = Optional(int, nullable=True)
    material_id = Optional(int, nullable=True)
    is_user_access = Optional(int, nullable=True)
    material_name = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Training_Material()
        item.id = self.id
        item.training_id = self.training_id
        item.material_id = self.material_id
        item.material_name = self.material_name
        item.is_user_access = self.is_user_access
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


class TrainingUserDB(db2.Entity):
    _table_ = "training_user"
    id = PrimaryKey(int, auto=True)
    training_id = Optional(int, nullable=True)
    user_id = Optional(int, nullable=True)
    is_active = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = Training_user()
        item.id = self.id
        item.training_id = self.training_id
        item.user_id = self.user_id
        item.is_active = self.is_active
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item

class LogBookDB(db2.Entity):
    _table_ = "logbook"
    id = PrimaryKey(int, auto=True)
    schedule_id = Optional(int, nullable=True)
    user_id = Optional(int, nullable=True)
    user_name = Optional(str, nullable=True)
    periode_date = Optional(date, nullable=True)
    periode_start_time = Optional(str, nullable=True)
    periode_end_time = Optional(str, nullable=True)
    topic = Optional(str, nullable=True)
    materi = Optional(str, nullable=True)
    training_proof_start = Optional(str, nullable=True)
    bukti_start = Optional(str, nullable=True)
    bukti_end = Optional(str, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = LogBook()
        item.id = self.id
        item.schedule_id = self.schedule_id
        item.user_id = self.user_id
        item.user_name = self.user_name
        item.periode_date = self.periode_date
        item.periode_start_time = self.periode_start_time
        item.periode_end_time = self.periode_end_time
        item.topic = self.topic
        item.materi = self.materi
        item.training_proof_start = self.training_proof_start
        item.bukti_start = self.bukti_start
        item.bukti_end = self.bukti_end
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item

class KelasUserDB(db2.Entity):
    _table_ = "class_user"
    id = PrimaryKey(int, auto=True)
    user_id = Optional(int, nullable=True)
    name = Optional(str, nullable=True)
    is_active = Optional(int, nullable=True)
    created_date = Optional(datetime, nullable=True)
    updated_date = Optional(datetime, nullable=True)

    def to_model(self):
        item = KelasUser()
        item.id = self.id
        item.user_id = self.user_id
        item.is_active = self.is_active
        item.name = self.name
        item.created_date = self.created_date
        item.updated_date = self.updated_date
        return item


if db2.schema is None:
    db2.generate_mapping(create_tables=False)


