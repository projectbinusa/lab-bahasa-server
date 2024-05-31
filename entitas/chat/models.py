class Chat:
    def __init__(
            self,
            id=0,
            name="",
            is_group=False,
            users=0,
            messages=0,
            class_id=0
    ):
        self.id = id
        self.name = name
        self.is_group = is_group
        self.users = users
        self.messages = messages
        self.class_id = class_id

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "is_group": self.is_group,
            "users": self.users,
            "messages": self.messages,
            "class_id": self.class_id
        }

    def to_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "is_group": self.is_group,
            "users": self.users,
            "messages": self.messages,
            "class_id": self.class_id
        }