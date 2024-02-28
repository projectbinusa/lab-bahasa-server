class Material:
    def __init__(
            self,
            id=0,
            user_id=0,
            name="",
            filename='',
            description='',
            url_file='',
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.name = name
        self.user_id = user_id
        self.filename = filename
        self.description = description
        self.url_file = url_file
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "filename": self.filename,
            "description": self.description,
            "url_file": self.url_file,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }

    def to_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "filename": self.filename,
            "description": self.description,
            "url_file": self.url_file,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }