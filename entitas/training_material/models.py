class Training_Material:
    def __init__(
            self,
            id= 0,
            training_id= 0,
            material_id= 0,
            material_name= 0,
            is_user_access= 0,
            created_date=None,
            updated_date=None
    ):
        self.id = id,
        self.training_id = training_id
        self.material_id = material_id
        self.material_name = material_name
        self.is_user_access = is_user_access
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "material_id": self.material_id,
            "material_name": self.material_name,
            "is_user_access": self.is_user_access,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "training_id": self.training_id,
            "material_id": self.material_id,
            "material_name": self.material_name,
            "is_user_access": self.is_user_access,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }