class Absent:
    def __init__(
            self,
            id= 0,
            training_id= 0,
            absent_date= '',
            user_id= 0,
            status= 0,
            description= '',
            created_date= None,
            updated_date= None,
    ):
        self.id= id
        self.training_id= training_id
        self.absent_date= absent_date
        self.user_id= user_id
        self.status= status
        self.description= description
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "absent_date": self.absent_date,
            "user_id": self.user_id,
            "status": self.status,
            "description": self.description,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "absent_date": self.absent_date,
            "user_id": self.user_id,
            "status": self.status,
            "description": self.description,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }