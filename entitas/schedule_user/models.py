from config.config import DOMAIN_FILE_URL
class Schedule_User:
    def __init__(
            self,
            id= 0,
            schedule_id= 0,
            user_id= 0,
            user_name='',
            is_deleted=False,
            score=0,
            certificate_url='',
            confirmed=False,
            created_date= None,
            updated_date= None
    ):
        self.id= id
        self.schedule_id= schedule_id
        self.user_id= user_id
        self.user_name= user_name
        self.is_deleted= is_deleted
        self.score = score
        self.certificate_url = certificate_url
        self.confirmed = confirmed
        self.created_date= created_date
        self.updated_date= updated_date

    def to_json(self):
        return  {
            "id": self.id,
            "schedule_id": self.schedule_id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "is_deleted": self.is_deleted,
            "score": self.score,
            "certificate_url": self.certificate_url,
            "confirmed": self.confirmed,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return  {
            "id": self.id,
            "schedule_id": self.schedule_id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "is_deleted": self.is_deleted,
            "score": self.score,
            "certificate_url": DOMAIN_FILE_URL + '/files/' + self.certificate_url if self.certificate_url not in [None, ''] else self.certificate_url,
            "confirmed": self.confirmed,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response_participant(self):
        return  {
            "id": self.id,
            "schedule_id": self.schedule_id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "score": self.score,
            "certificate_url": DOMAIN_FILE_URL + '/files/' + self.certificate_url if self.certificate_url not in [None, ''] else self.certificate_url,
            "confirmed": self.confirmed,
        }