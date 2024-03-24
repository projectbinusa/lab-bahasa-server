class Certificate:
    def __init__(
            self,
            id= 0,
            schedule_id= 0,
            training_id= 0,
            instructur_id= 0,
            user_id=0,
            instructur_name= '',
            name= '',
            url_file= '',
            publish_date= '',
            score= 0,
            mark= '',
            created_date= None,
            updated_date= None,
    ):
        self.id= id
        self.schedule_id= schedule_id
        self.training_id= training_id
        self.instructur_id= instructur_id
        self.user_id = user_id
        self.instructur_name= instructur_name
        self.name= name
        self.url_file= url_file
        self.publish_date= publish_date
        self.score= score
        self.mark= mark
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return {
            "id": self.id,
            "schedule_id": self.schedule_id,
            "training_id": self.training_id,
            "instructur_name": self.instructur_name,
            "user_id": self.user_id,
            "name": self.name,
            "url_file": self.url_file,
            "publish_date": self.publish_date,
            "score": self.score,
            "mark": self.mark,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "schedule_id": self.schedule_id,
            "training_id": self.training_id,
            "user_id": self.user_id,
            "instructur_name": self.instructur_name,
            "name": self.name,
            "url_file": self.url_file,
            "publish_date": self.publish_date,
            "score": self.score,
            "mark": self.mark,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }