class Absent:
    def __init__(
            self,
            id= 0,
            training_id= 0,
            training_name= '',
            schedule_id= 0,
            absent_date= '',
            user_id= 0,
            user_name= '',
            status= 0,
            description= '',
            location='',
            signature='',
            created_date= None,
            updated_date= None,
    ):
        self.id= id
        self.training_id= training_id
        self.training_name= training_name
        self.schedule_id= schedule_id
        self.absent_date= absent_date
        self.user_id= user_id
        self.user_name= user_name
        self.status= status
        self.description= description
        self.location = location
        self.signature = signature
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "training_name": self.training_name,
            "schedule_id": self.schedule_id,
            "absent_date": str(self.absent_date) if self.absent_date is not None else None,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "status": self.status,
            "description": self.description,
            "location": self.location,
            "signature": self.signature,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "training_name": self.training_name,
            "schedule_id": self.schedule_id,
            "absent_date": str(self.absent_date) if self.absent_date is not None else None,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "status": self.status,
            "description": self.description,
            "location": self.location,
            "signature": self.signature,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }