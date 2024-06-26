class Material:
    def __init__(
            self,
            id=0,
            user_id=0,
            name="",
            filename='',
            description='',
            tag='',
            url_file='',
            other_link='',
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.name = name
        self.user_id = user_id
        self.filename = filename
        self.description = description
        self.tag = tag
        self.url_file = url_file
        self.other_link = other_link
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "filename": self.filename,
            "description": self.description,
            "tag": self.tag,
            "url_file": self.url_file,
            "other_link": self.other_link,
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
            "tag": self.tag,
            "url_file": self.url_file,
            "other_link": self.other_link,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }