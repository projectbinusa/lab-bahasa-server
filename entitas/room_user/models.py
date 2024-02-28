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