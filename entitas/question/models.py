class Question:
    def __init__(
            self,
            id=0,
            think_time='',
            answer_time='',
            class_id=0,
            user_id=0,
            user_name='',
            score='',
            answer_time_client='',
            answer='',
            type='',
            created_date=None,
            updated_date=None
    ):
        self.id= id
        self.think_time = think_time
        self.answer_time = answer_time
        self.class_id = class_id
        self.user_id = user_id
        self.user_name = user_name
        self.score = score
        self.answer_time_client = answer_time_client
        self.answer = answer
        self.type = type
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "think_time": self.think_time,
            "answer_time": self.answer_time,
            "class_id": self.class_id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "score": self.score,
            "answer_time_client": self.answer_time_client,
            "answer": self.answer,
            "type": self.type,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

    def to_response(self):
        return {
            "id": self.id,
            "think_time": self.think_time,
            "answer_time": self.answer_time,
            "class_id": self.class_id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "score": self.score,
            "answer_time_client": self.answer_time_client,
            "answer": self.answer,
            "type": self.type,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }