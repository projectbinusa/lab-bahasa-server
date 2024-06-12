from datetime import timedelta


class Question:
    def __init__(
            self,
            id=0,
            name='',
            think_time='',
            answer_time='',
            class_id=0,
            user_id=0,
            user_name='',
            type='',
            created_date=None,
            updated_date=None
    ):
        self.id = id
        self.name = name
        self.think_time = think_time
        self.answer_time = answer_time
        self.class_id = class_id
        self.user_id = user_id
        self.user_name = user_name
        self.type = type
        self.created_date = created_date
        self.updated_date = updated_date

    # def _convert_timedelta_to_str(self, td):
    #     if isinstance(td, timedelta):
    #         total_seconds = int(td.total_seconds())
    #         hours = total_seconds // 3600
    #         minutes = (total_seconds % 3600) // 60
    #         return f"{hours:02}:{minutes:02}"
    #     return td

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "think_time": self.think_time,
            "answer_time": self.answer_time,
            "class_id": self.class_id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "type": self.type,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

    def to_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "class_id": self.class_id,
            "think_time": self.think_time,
            "answer_time": self.answer_time,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "type": self.type,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

    def to_response_competition(self):
        return {
            "id": self.id,
            "name": self.name,
            "class_id": self.class_id,
            "think_time": self.think_time,
            "answer_time": self.answer_time,
            # "think_time": self._convert_timedelta_to_str(self.think_time),
            # "answer_time": self._convert_timedelta_to_str(self.answer_time),
            "user_id": self.user_id,
            "user_name": self.user_name,
            "type": self.type,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

    # def to_response_competition_answer(self):
    #     return {
    #         "id": self.id,
    #         "class_id": self.class_id,
    #         "user_id": self.user_id,
    #         "answer": self.answer,
    #         "created_date": str(self.created_date) if self.created_date is not None else None,
    #         "updated_date": str(self.updated_date) if self.updated_date is not None else None
    #     }
