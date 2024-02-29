class Room:
    def __init__(
            self,
            id= 0,
            name= '',
            avatar_url='',
            is_removed= 0,
            last_comment= '',
            created_date= None,
            updated_date= None
    ):
        self.id= id
        self.name= name
        self.avatar_url= avatar_url
        self.is_removed= is_removed
        self.last_comment= last_comment
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "avatar_url": self.avatar_url,
            "is_removed": self.is_removed,
            "last_comment": self.last_comment,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None
        }