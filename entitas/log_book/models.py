class LogBook:
    def __init__(
            self,
            id=0,
            schedule_id='',
            user_id='',
            user_name='',
            periode_date='',
            periode_start_time='',
            periode_end_time='',
            topic='',
            materi='',
            training_proof_start='',
            bukti_start='',
            bukti_end='',
            created_date=None,
            updated_date=None,
    ):
        self.id = id
        self.schedule_id = schedule_id
        self.user_id = user_id
        self.user_name = user_name
        self.periode_date = periode_date
        self.periode_start_time = periode_start_time
        self.periode_end_time = periode_end_time
        self.topic = topic
        self.materi = materi
        self.training_proof_start = training_proof_start
        self.bukti_start = bukti_start
        self.bukti_end = bukti_end
        self.created_date = created_date
        self.updated_date = updated_date

    def to_json(self):
        return {
            "id": self.id,
            "schedule_id": self.schedule_id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "periode_date": self.periode_date.strftime("%Y-%m-%d") if self.periode_date else None,
            "periode_start_time": str(self.periode_start_time),  # Ubah timedelta menjadi string
            "periode_end_time": str(self.periode_end_time),  # Ubah timedelta menjadi string
            "topic": self.topic,
            "materi": self.materi,
            "training_proof_start": self.training_proof_start,
            "bukti_start": self.bukti_start,
            "bukti_end": self.bukti_end,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }

    def to_response(self):
        return {
            "id": self.id,
            "schedule_id": self.schedule_id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "periode_date": self.periode_date.strftime("%Y-%m-%d") if self.periode_date else None,
            "periode_start_time": str(self.periode_start_time),
            "periode_end_time": str(self.periode_end_time),
            "topic": self.topic,
            "materi": self.materi,
            "training_proof_start": self.training_proof_start,
            "bukti_start": self.bukti_start,
            "bukti_end": self.bukti_end,
            "created_date": str(self.created_date) if self.created_date is not None else None,
            "updated_date": str(self.updated_date) if self.updated_date is not None else None,
        }
