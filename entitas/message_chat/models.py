class MessageChat:
    def __init__(
            self,
            id=0,
            chat=0,
            content="",
            sender=0,
            class_id=0,
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.chat = chat
        self.content = content
        self.sender = sender
        self.class_id = class_id
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "chat": self.chat,
            "content": self.content,
            "sender": self.sender,
            "clas_id": self.class_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

    def to_response(self):
        return {
            "id": self.id,
            "chat": self.chat,
            "content": self.content,
            "sender": self.sender,
            "clas_id": self.class_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }