class Instructur:
    def __init__(
            self,
            id= 0,
            name= '',
            email= '',
            address= '',
            birth_date= '',
            birth_place= '',
            avatar_url= '',
            is_facilitator= '',
            created_date= None,
            updated_date= None,
    ):
        self.id= id
        self.name= name
        self.email= email
        self.address= address
        self.birth_date= birth_date
        self.birth_place= birth_place
        self.avatar_url= avatar_url
        self.is_facilitator= is_facilitator
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
         return {
             "id": self.id,
             "name": self.name,
             "email": self.email,
             "address": self.address,
             "birth_date": self.birth_date,
             "birth_place": self.birth_place,
             "avatar_url": self.avatar_url,
             "is_facilitator": self.is_facilitator,
             "created_date": str(self.created_date) if self.created_date is not None else None,
             "updated_date": str(self.updated_date) if self.updated_date is not None else None,
         }

    def to_response(self):
         return {
             "id": self.id,
             "name": self.name,
             "email": self.email,
             "address": self.address,
             "birth_date": self.birth_date,
             "birth_place": self.birth_place,
             "avatar_url": self.avatar_url,
             "is_facilitator": self.is_facilitator,
             "created_date": str(self.created_date) if self.created_date is not None else None,
             "updated_date": str(self.updated_date) if self.updated_date is not None else None,
         }