class Whiteboard:
    def __init__(
            self,
            id=0,
            user_id=0,
            username=0,
            class_id=0,
            class_name=0,
            created_date=None,
            updated_date=None
    ):
        self.id = id
        self.username = username
        self.user_id = user_id
        self.class_id = class_id
        self.class_name = class_name
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "username": self.username,
            "class_id": self.class_id,
            "class_name": self.class_name,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "username": self.username,
            "class_id": self.class_id,
            "class_name": self.class_name,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }
