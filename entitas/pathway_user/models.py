class Pathway_User:
    def __init__(
            self,
            id= 0,
            pathway_id= 0,
            pathway_name= '',
            user_id= 0,
            user_name='',
            created_date= None,
            updated_date= None,
    ):
        self.id= id
        self.pathway_id= pathway_id
        self.pathway_name= pathway_name
        self.user_id= user_id
        self.user_name = user_name
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "pathway_id": self.pathway_id,
            "pathway_name": self.pathway_name,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "pathway_id": self.pathway_id,
            "pathway_name": self.pathway_name,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }