class KelasUser:
    def __init__(
            self,
            id=0,
            name="",
            description="",
            file="",
            is_active=0,
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.file = file
        self.is_active = is_active
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "file": self.file,
            "is_active": self.is_active,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

    def to_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "file": self.file,
            "is_active": self.is_active,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }