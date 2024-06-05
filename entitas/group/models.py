class Group:
    def __init__(
            self,
            id=0,
            name='',
            description='',
            is_removed=0,
            class_id=0,
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.is_removed = is_removed
        self.class_id = class_id
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_removed": self.is_removed,
            "class_id": self.class_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

    def to_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_removed": self.is_removed,
            "class_id": self.class_id,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

