class Comment:
    def __init__(
            self,
            id=0,
            comment_for_id=0,
            is_deleted=0,
            message='',
            room_id=0,
            room_name=0,
            status='',
            user_avatar_url='',
            user_id=0,
            user_name='',
            created_date=None,
            updated_date=None
    ):
        self.id = id
        self.comment_for_id = comment_for_id
        self.is_deleted = is_deleted
        self.message = message
        self.room_id = room_id
        self.room_name = room_name
        self.status = status
        self.user_avatar_url = user_avatar_url
        self.user_id = user_id
        self.user_name = user_name
        self.created_date = created_date
        self.updated_date = updated_date

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
