class Pathway_Training:
    def __init__(
            self,
            id= 0,
            pathway_id= 0,
            training_id= 0,
            training_name='',
            urut=0,
            created_date= None,
            updated_date= None
    ):
        self.id= id
        self.pathway_id= pathway_id
        self.training_id= training_id
        self.training_name = training_name
        self.urut = urut
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "pathway_id": self.pathway_id,
            "training_id": self.training_id,
            "training_name": self.training_name,
            "urut": self.urut,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "pathway_id": self.pathway_id,
            "training_id": self.training_id,
            "training_name": self.training_name,
            "urut": self.urut,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }
    def to_response_simple(self):
        return {
            "training_id": self.training_id,
            "training_name": self.training_name,
            "urut": self.urut
        }
    def to_response_trainings(self):
        return {
            "training_id": self.training_id,
            "name": self.training_name,
            "urut": self.urut
        }
