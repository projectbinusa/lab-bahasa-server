class Announcement:
    def __init__(
            self,
            id= 0,
            name= '',
            is_published=False,
            description= '',
            created_date= None,
            updated_date= None
    ):
        self.id= id
        self.name= name
        self.is_published= is_published
        self.description= description
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "is_published": self.is_published,
            "description": self.description,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

    def to_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "is_published": self.is_published,
            "description": self.description,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }