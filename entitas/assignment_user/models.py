class Assignment_User:
    def __init__(
            self,
            id= 0,
            assignment_id= 0,
            user_id= 0,
            training_id= 0,
            instructur_id= 0,
            url_file= '',
            description= '',
            score= 0,
            comment= '',
            created_date= None,
            updated_date= None,
    ):
        self.id= id
        self.assignment_id= assignment_id
        self.user_id= user_id
        self.training_id= training_id
        self.instructur_id= instructur_id
        self.url_file= url_file
        self.description= description
        self.score= score
        self.comment= comment
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "assignment_id": self.assignment_id,
            "user_id": self.user_id,
            "training_id": self.training_id,
            "instructur_id": self.instructur_id,
            "url_file": self.url_file,
            "description": self.description,
            "score": self.score,
            "comment": self.comment,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "assignment_id": self.assignment_id,
            "user_id": self.user_id,
            "training_id": self.training_id,
            "instructur_id": self.instructur_id,
            "url_file": self.url_file,
            "description": self.description,
            "score": self.score,
            "comment": self.comment,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response_simple(self):
        return {
            "id": self.id,
            "url_file": self.url_file,
            "description": self.description,
            "score": self.score,
            "comment": self.comment
        }