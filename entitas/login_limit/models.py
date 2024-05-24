class LoginLimits:
    def __init__(
            self,
            id=0,
            class_id='',
            end_time='',
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.class_id = class_id
        self.end_time = end_time
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "class_id": self.class_id,
            "end_time": self.end_time,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "class_id": self.class_id,
            "end_time": self.end_time,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }
