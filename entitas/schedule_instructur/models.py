class Schedule_instuctur:
    def __init__(
            self,
            id= 0,
            schedule_id= 0,
            user_id= 0,
            user_name= '',
            is_deleted='',
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.schedule_id = schedule_id
        self.user_id = user_id
        self.user_name = user_name
        self.is_deleted = is_deleted
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "schedule_id": self.schedule_id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "is_deleted": self.is_deleted,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "schedule_id": self.schedule_id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "is_deleted": self.is_deleted,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }