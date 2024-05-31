class Answer:
    def __init__(
            self,
            id=0,
            question_id=0,
            answer='',
            user_id=0,
            answer_time_user='',
            class_id=0,
            created_date=None,
            updated_date=None
    ):
        self.id = id
        self.question_id = question_id
        self.answer = answer
        self.user_id = user_id
        self.answer_time_user = answer_time_user
        self.class_id = class_id
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "question_id": self.question_id,
            "answer": self.answer,
            "user_id": self.user_id,
            "answer_time_user": self.answer_time_user,
            "class_id": self.class_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

    def to_response(self):
        return {
            "id": self.id,
            "question_id": self.question_id,
            "answer": self.answer,
            "user_id": self.user_id,
            "answer_time_user": self.answer_time_user,
            "class_id": self.class_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }