class Material:
    def __init__(
            self,
            id=0,
            user_id=0,
            name="",
            filename='',
            description='',
            url_file='',
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.name = name
        self.user_id = user_id
        self.filename = filename
        self.description = description
        self.url_file = url_file
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "filename": self.filename,
            "description": self.description,
            "url_file": self.url_file,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

    def to_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "filename": self.filename,
            "description": self.description,
            "url_file": self.url_file,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

class Pathway:
    def __init__(
            self,
            id=0,
            name="",
            description="",
            created_date=None,
            updated_date=None,
    ):
        self.id = id,
        self.name = name,
        self.description = description,
        self.created_date = created_date,
        self.updated_date = updated_date,

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Pathway_Training:
    def __init__(
            self,
            id= 0,
            pathway_id= 0,
            training_id= 0,
            created_date= None,
            updated_date= None
    ):
        self.id= id
        self.pathway_id= pathway_id
        self.training_id= training_id
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "pathway_id": self.pathway_id,
            "training_id": self.training_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "pathway_id": self.pathway_id,
            "training_id": self.training_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Pathway_User:
    def __init__(
            self,
            id= 0,
            pathway_id= 0,
            user_id= 0,
            created_date= None,
            updated_date= None,
    ):
        self.id= id
        self.pathway_id= pathway_id
        self.user_id= user_id
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "pathway_id": self.pathway_id,
            "user_id": self.user_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "pathway_id": self.pathway_id,
            "user_id": self.user_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Tarining:
    def __init__(
            self,
            id=0,
            name="",
            description="",
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "update_date": str(self.updated_date) if self.updated_date is not None else None
        }

    def to_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "update_date": str(self.updated_date) if self.updated_date is not None else None
        }

class Training:
    def __init__(
            self,
            id= 0,
            name= '',
            description= '',
            created_date= None,
            updated_date= None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Training_Material:
    def __init__(
            self,
            id= 0,
            training_id= 0,
            material_id= 0,
            is_user_access= 0,
            created_date=None,
            updated_date=None
    ):
        self.id = id,
        self.training_id = training_id
        self.material_id = material_id
        self.is_user_access = is_user_access
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "material_id": self.material_id,
            "is_user_access": self.is_user_access,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "material_id": self.material_id,
            "is_user_access": self.is_user_access,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Training_user:
    def __init__(
            self,
            id=0,
            training_id=0,
            user_id=0,
            is_active=0,
            created_date=None,
            updated_date=None
    ):
        self.id = id
        self.training_id = training_id
        self.user_id = user_id
        self.is_active = is_active
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "user_id": self.user_id,
            "is_active": self.is_active,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "user_id": self.user_id,
            "is_active": self.is_active,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Schedule:
    def __init__(
            self,
            id=0,
            training_id=0,
            link='',
            is_online=0,
            location='',
            start_date='',
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.training_id = training_id
        self.link = link
        self.is_online = is_online
        self.location = location
        self.start_date = start_date
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "link": self.link,
            "is_online": self.is_online,
            "location": self.location,
            "start_date": self.start_date,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "link": self.link,
            "is_online": self.is_online,
            "location": self.location,
            "start_date": self.start_date,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Schedule_instuctur:
    def __init__(
            self,
            id= 0,
            scheduler_id= 0,
            instructur_id= 0,
            instructur_name= '',
            is_deteted='',
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.scheculer_id = scheduler_id
        self.instructur_id = instructur_id
        self.instructur_name = instructur_name
        self.is_deteted = is_deteted
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "scheduler_id": self.scheculer_id,
            "instructur_id": self.instructur_id,
            "instructur_name": self.instructur_name,
            "is_deteted": self.is_deteted,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "scheduler_id": self.scheculer_id,
            "instructur_id": self.instructur_id,
            "instructur_name": self.instructur_name,
            "is_deteted": self.is_deteted,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Schedule_User:
    def __init__(
            self,
            id= 0,
            scheduler_id= 0,
            instructur_id= 0,
            instructur_name='',
            is_deteted= 0,
            created_date= None,
            updated_date= None
    ):
        self.id= id
        self.scheduler_id= scheduler_id
        self.instructur_id= instructur_id
        self.instructur_name= instructur_name
        self.is_deteted= is_deteted
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return  {
            "id": self.id,
            "scheduler_id": self.scheduler_id,
            "instructur_id": self.instructur_id,
            "instructur_name": self.instructur_name,
            "is_deteted": self.is_deteted,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return  {
            "id": self.id,
            "scheduler_id": self.scheduler_id,
            "instructur_id": self.instructur_id,
            "instructur_name": self.instructur_name,
            "is_deteted": self.is_deteted,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Room_User:
    def __init__(
            self,
            id= 0,
            room_id= 0,
            user_id= 0,
            last_comment_user_id= 0,
            last_comment_text= '',
            last_comment_date= '',
            avatar_url= '',
            created_date=None,
            updated_date=None,
    ):
        self.id= id
        self.room_id= room_id
        self.user_id= user_id
        self.last_comment_user_id= last_comment_user_id
        self.last_comment_text= last_comment_text
        self.last_comment_date= last_comment_date
        self.avatar_url= avatar_url
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "room_id": self.room_id,
            "user_id": self.user_id,
            "last_comment_user_id": self.last_comment_user_id,
            "last_comment_text": self.last_comment_text,
            "last_comment_date": self.last_comment_date,
            "avatar_url": self.avatar_url,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "room_id": self.room_id,
            "user_id": self.user_id,
            "last_comment_user_id": self.last_comment_user_id,
            "last_comment_text": self.last_comment_text,
            "last_comment_date": self.last_comment_date,
            "avatar_url": self.avatar_url,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Room:
    def __init__(
            self,
            id= 0,
            name= '',
            is_removed= 0,
            last_comment= '',
            created_date= None,
            updated_date= None
    ):
        self.id= id
        self.name= name
        self.is_removed= is_removed
        self.last_comment= last_comment
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "is_removed": self.is_removed,
            "last_comment": self.last_comment,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

class Notification:
    def __init__(
            self,
            id= 0,
            fcm_token= '',
            email= '',
            user_id= 0,
            title= '',
            message= '',
            created_date= None,
            updated_date= None
    ):
        self.id= id
        self.fcm_token= fcm_token
        self.email= email
        self.user_id= user_id
        self.title= title
        self.message= message
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "fcm_token": self.fcm_token,
            "email": self.email,
            "user_id": self.user_id,
            "title": self.title,
            "message": self.message,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "fcm_token": self.fcm_token,
            "email": self.email,
            "user_id": self.user_id,
            "title": self.title,
            "message": self.message,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Instructur:
    def __init__(
            self,
            id= 0,
            name= '',
            email= '',
            address= '',
            birth_date= '',
            birth_place= '',
            avatar_url= '',
            is_facilitator= '',
            created_date= None,
            updated_date= None,
    ):
        self.id= id
        self.name= name
        self.email= email
        self.address= address
        self.birth_date= birth_date
        self.birth_place= birth_place
        self.avatar_url= avatar_url
        self.is_facilitator= is_facilitator
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
         return {
             "id": self.id,
             "name": self.name,
             "email": self.email,
             "address": self.address,
             "birth_date": self.birth_date,
             "birth_place": self.birth_place,
             "avatar_url": self.avatar_url,
             "is_facilitator": self.is_facilitator,
             "created_date": str(self.created_date) if self.created_date is not None else None,
             "updated_date": str(self.updated_date) if self.updated_date is not None else None,
         }

    def to_response(self):
         return {
             "id": self.id,
             "name": self.name,
             "email": self.email,
             "address": self.address,
             "birth_date": self.birth_date,
             "birth_place": self.birth_place,
             "avatar_url": self.avatar_url,
             "is_facilitator": self.is_facilitator,
             "created_date": str(self.created_date) if self.created_date is not None else None,
             "updated_date": str(self.updated_date) if self.updated_date is not None else None,
         }

class Comment:
    def __init__(
            self,
            id= 0,
            comment_for_id= 0,
            is_deleted= 0,
            message= '',
            room_id= 0,
            room_name= 0,
            status= '',
            user_avatar_url= '',
            user_id= 0,
            user_name= '',
            created_date= None,
            updated_date= None
    ):
        self.id= id
        self.comment_for_id= comment_for_id
        self.is_deleted= is_deleted
        self.message= message
        self.room_id= room_id
        self.room_name= room_name
        self.status= status
        self.user_avatar_url= user_avatar_url
        self.user_id= user_id
        self.user_name= user_name
        self.created_date= created_date
        self.updated_date= updated_date


    def to_json(self):
        return {
            "id": self.id,
            "comment_for_id": self.comment_for_id,
            "is_deleted": self.is_deleted,
            "message": self.message,
            "room_id": self.room_id,
            "room_name": self.room_name,
            "status": self.status,
            "user_avatar_url": self.user_avatar_url,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "comment_for_id": self.comment_for_id,
            "is_deleted": self.is_deleted,
            "message": self.message,
            "room_id": self.room_id,
            "room_name": self.room_name,
            "status": self.status,
            "user_avatar_url": self.user_avatar_url,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Certificate:
    def __init__(
            self,
            id= 0,
            scheduler_id= 0,
            training_id= 0,
            instructur_id= 0,
            instructur_name= '',
            name= '',
            url_file= '',
            publish_date= '',
            score= 0,
            mark= '',
            created_date= None,
            updated_date= None,
    ):
        self.id= id
        self.scheduler_id= scheduler_id
        self.training_id= training_id
        self.instructur_id= instructur_id
        self.instructur_name= instructur_name
        self.name= name
        self.url_file= url_file
        self.publish_date= publish_date
        self.score= score
        self.mark= mark
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "scheduler_id": self.scheduler_id,
            "training_id": self.training_id,
            "instructur_name": self.instructur_name,
            "name": self.name,
            "url_file": self.url_file,
            "publish_date": self.publish_date,
            "score": self.score,
            "mark": self.mark,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "scheduler_id": self.scheduler_id,
            "training_id": self.training_id,
            "instructur_name": self.instructur_name,
            "name": self.name,
            "url_file": self.url_file,
            "publish_date": self.publish_date,
            "score": self.score,
            "mark": self.mark,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Assignment:
    def __init_(
            self,
            id= 0,
            scheduler_id= 0,
            training_id= 0,
            instructur_id= 0,
            name= '',
            description= '',
            max_date= '',
            created_date= None,
            updated_date= None,
    ):
        self.id= id
        self.scheduler_id= scheduler_id
        self.training_id= training_id
        self.instructur_id= instructur_id
        self.name= name
        self.description= description
        self.max_date= max_date
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "scheduler_id": self.scheduler_id,
            "training_id": self.training_id,
            "instructur_id": self.instructur_id,
            "name": self.name,
            "description": self.description,
            "max_date": self.max_date,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "scheduler_id": self.scheduler_id,
            "training_id": self.training_id,
            "instructur_id": self.instructur_id,
            "name": self.name,
            "description": self.description,
            "max_date": self.max_date,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Assignment_User:
    def __init__(
            self,
            id= 0,
            assignment_id= 0,
            user_id= 0,
            training_id= 0,
            instructur_id= 0,
            url_file= '',
            description= '',
            score= 0,
            comment= '',
            created_date= None,
            updated_date= None,
    ):
        self.id= id
        self.assignment_id= assignment_id
        self.user_id= user_id
        self.training_id= training_id
        self.instructur_id= instructur_id
        self.url_file= url_file
        self.description= description
        self.score= score
        self.comment= comment
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "assignment_id": self.assignment_id,
            "user_id": self.user_id,
            "training_id": self.training_id,
            "instructur_id": self.instructur_id,
            "url_file": self.url_file,
            "description": self.description,
            "score": self.score,
            "comment": self.comment,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "assignment_id": self.assignment_id,
            "user_id": self.user_id,
            "training_id": self.training_id,
            "instructur_id": self.instructur_id,
            "url_file": self.url_file,
            "description": self.description,
            "score": self.score,
            "comment": self.comment,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

class Absent:
    def __init__(
            self,
            id= 0,
            training_id= 0,
            absent_date= '',
            user_id= 0,
            status= 0,
            description= '',
            created_date= None,
            updated_date= None,
    ):
        self.id= id
        self.training_id= training_id
        self.absent_date= absent_date
        self.user_id= user_id
        self.status= status
        self.description= description
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "absent_date": self.absent_date,
            "user_id": self.user_id,
            "status": self.status,
            "description": self.description,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "absent_date": self.absent_date,
            "user_id": self.user_id,
            "status": self.status,
            "description": self.description,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }