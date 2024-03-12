class Schedule_instuctur:
    def __init__(
            self,
            id= 0,
            schedule_id= 0,
            instructur_id= 0,
            instructur_name= '',
            is_deteted='',
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.schecule_id = schedule_id
        self.instructur_id = instructur_id
        self.instructur_name = instructur_name
        self.is_deteted = is_deteted
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "schedule_id": self.schecule_id,
            "instructur_id": self.instructur_id,
            "instructur_name": self.instructur_name,
            "is_deteted": self.is_deteted,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "schedule_id": self.schecule_id,
            "instructur_id": self.instructur_id,
            "instructur_name": self.instructur_name,
            "is_deteted": self.is_deteted,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }