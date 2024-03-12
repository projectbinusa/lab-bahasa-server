class Assignment:
    def __init_(
            self,
            id= 0,
            schedule_id= 0,
            training_id= 0,
            instructur_id= 0,
            name= '',
            description= '',
            max_date= '',
            created_date= None,
            updated_date= None,
    ):
        self.id= id
        self.schedule_id= schedule_id
        self.training_id= training_id
        self.instructur_id= instructur_id
        self.name= name
        self.description= description
        self.max_date= max_date
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "schedule_id": self.schedule_id,
            "training_id": self.training_id,
            "instructur_id": self.instructur_id,
            "name": self.name,
            "description": self.description,
            "max_date": self.max_date,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "schedule_id": self.schedule_id,
            "training_id": self.training_id,
            "instructur_id": self.instructur_id,
            "name": self.name,
            "description": self.description,
            "max_date": self.max_date,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }