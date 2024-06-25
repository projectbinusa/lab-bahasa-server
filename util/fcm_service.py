from pyfcm import FCMNotification
from config import config

class FcmService:
    def init(self):
        self.push_service = FCMNotification(config.firebase_server_key, project_id=config.firebase_project_id)

    def broadcast(self, topic_name='', message='', title=''):
        self.push_service.notify_topic_subscribers(topic_name=topic_name, message_body=message, message_title=title)

    def send_message(self, registration_id='', message='', title=''):
        self.push_service.notify_single_device(registration_id=registration_id, message_body=message, message_title=title)