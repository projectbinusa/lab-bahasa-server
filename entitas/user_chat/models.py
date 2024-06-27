class UserChat:
    def __init__(
            self,
            id=0,
            user_id='',
            user_name='',
            class_id=0,
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.user_id = user_id
        self.user_name = user_name
        self.class_id = class_id
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "class_id": self.class_id,
            "user_name": self.user_name,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

    def to_response(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "class_id": self.class_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

