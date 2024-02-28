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