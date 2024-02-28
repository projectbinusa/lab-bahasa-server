class Notification:
    def __init__(
            self,
            id= 0,
            fcm_token= '',
            email= '',
            user_id= 0,
            title= '',
            message= '',
            created_date= None,
            updated_date= None
    ):
        self.id= id
        self.fcm_token= fcm_token
        self.email= email
        self.user_id= user_id
        self.title= title
        self.message= message
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "fcm_token": self.fcm_token,
            "email": self.email,
            "user_id": self.user_id,
            "title": self.title,
            "message": self.message,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "fcm_token": self.fcm_token,
            "email": self.email,
            "user_id": self.user_id,
            "title": self.title,
            "message": self.message,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }