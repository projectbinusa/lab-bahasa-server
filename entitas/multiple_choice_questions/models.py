class MultipleChoiceQuestions:
    def __init__(self, id=0, user_id=0, user_name='', chosen=0, class_id=0, question_text="", options=None, correct_answer=0):
        self.id = id
        self.user_id = user_id
        self.user_name = user_name
        self.chosen = chosen
        self.class_id = class_id
        self.question_text = question_text
        self.options = options or []
        self.correct_answer = correct_answer

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "chosen": self.chosen,
            "class_id": self.class_id,
            "question_text": self.question_text,
            "options": self.options,
            "correct_answer": self.correct_answer
        }

    def to_response(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "chosen": self.chosen,
            "class_id": self.class_id,
            "question_text": self.question_text,
            "options": self.options,
            "correct_answer": self.correct_answer
        }
