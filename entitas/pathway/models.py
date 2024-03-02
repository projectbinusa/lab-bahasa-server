
class Pathway:
    def __init__(
            self,
            id=0,
            name="",
            description="",
            deleted="",
            created_date=None,
            updated_date=None,
    ):
        self.id = id,
        self.name = name,
        self.description = description,
        self.deleted = deleted,
        self.created_date = created_date,
        self.updated_date = updated_date,

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "deleted": self.deleted,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "deleted": self.deleted,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }