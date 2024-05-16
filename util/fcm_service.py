import requests
import json
from config import config
from pyfcm import FCMNotification

class FcmService:
    def __init__(self):
        self.push_service = FCMNotification(api_key=config.firebase_server_key)

    def broadcast(self, topic_name='', message='',title=''):
        self.push_service.notify_topic_subscribers(topic_name=topic_name, message_body=message,
                                                   message_title=title)

    def send_message(self, registration_id='', message='', title=''):
        self.push_service.notify_single_device(registration_id=registration_id, message_body=message,
                                               message_title=title)
