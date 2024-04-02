class Schedule:
    def __init__(
            self,
            id=0,
            name='',
            training_id=0,
            training_name='',
            link='',
            other_link='',
            is_online=0,
            location='',
            active='',
            start_date='',
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.name = name
        self.training_id = training_id
        self.training_name = training_name
        self.link = link
        self.other_link = other_link
        self.is_online = is_online
        self.location = location
        self.active = active
        self.start_date = start_date
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "training_id": self.training_id,
            "training_name": self.training_name,
            "link": self.link,
            "full_link": 'https://dev-event.lynk2.co/roomMeet?id=' + self.link if self.link not in ['', None] else None,
            "other_link": self.other_link,
            "is_online": self.is_online,
            "location": self.location,
            "active": self.active,
            "start_date": str(self.start_date) if self.start_date is not None else None,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "training_id": self.training_id,
            "training_name": self.training_name,
            "link": self.link,
            "full_link": 'https://dev-event.lynk2.co/roomMeet?id=' + self.link if self.link not in ['', None] else None,
            "other_link": self.other_link,
            "is_online": self.is_online,
            "location": self.location,
            "active": self.active,
            "start_date": str(self.start_date) if self.start_date is not None else None,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response_calendar(self):
        return {
            "id": self.id,
            "name": self.name,
            "training_id": self.training_id,
            "training_name": self.training_name,
            "link": self.link,
            "full_link": 'https://dev-event.lynk2.co/roomMeet?id='+self.link if self.link not in ['', None] else None,
            "other_link": self.other_link,
            "is_online": self.is_online,
            "location": self.location,
            "active": self.active,
            "start_date": str(self.start_date) if self.start_date is not None else None,
            "day": self.start_date.day if self.start_date is not None else None,
            "hour": self.start_date.hour if self.start_date is not None else None
        }