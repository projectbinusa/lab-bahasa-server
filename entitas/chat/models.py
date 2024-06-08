class Chat:
    def __init__(
            self,
            id=0,
            content="",
            receiver_id=0,
            sender_id=0,
            is_group=0,
            group_id=0,
            topic_chat_id=0,
            gambar='',
            class_id=0,
            created_date=None,
            updated_date=None
    ):
        self.id = id
        self.content = content
        self.receiver_id = receiver_id
        self.sender_id = sender_id
        self.group_id = group_id
        self.topic_chat_id = topic_chat_id
        self.is_group = is_group
        self.gambar = gambar
        self.class_id = class_id
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "content": self.content,
            # "receiver_id": self.receiver_id,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "group_id": self.group_id,
            "topic_chat_id": self.topic_chat_id,
            "is_group": self.is_group,
            "gambar": self.gambar,
            "class_id": self.class_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "content": self.content,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "group_id": self.group_id,
            "topic_chat_id": self.topic_chat_id,
            "is_group": self.is_group,
            "gambar": self.gambar,
            "class_id": self.class_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }