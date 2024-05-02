# import socketio
# from flask_socketio import SocketIO, emit
# from flask import Flask, request
# import jwt
# from util.jwt_util import ekstrak_jwt
from datetime import datetime


# class SocketClient:
#     def __init__(
#             self,
#             socket_authorization='',
#             socket_server='',
#             without_init=False
#     ):
#         self.socket_authorization = socket_authorization
#         self.socket_server = socket_server
#         self.sio = socketio.Client()
#         if not without_init:
#             self.sio.connect(url=socket_server, headers={"Authorization": socket_authorization})
#         self.start_runnging12m = False
#         print("client socket is connected :", self.sio.connected)
#
#
#
#         @self.sio.event
#         def connect():
#             print("I'm connected!")
#
#
#         @self.sio.event
#         def connect_error():
#             print("The connection failed!")
#
#         @self.sio.on('running12m_status')
#         def on_message(data):
#             print('running12m_status ', data)
#             if data['status'] == 'start':
#                 self.start_runnging12m = True
#
#
#     def send_to_socketio(self, topic="", message={}):
#         try:
#             if self.sio.connected:
#                 self.sio.emit(topic, message)
#             else:
#                 self.sio.connect(
#                     url=self.socket_server, headers={"Authorization": self.socket_authorization}
#                 )
#                 self.sio.emit(topic, message)
#             return True
#         except Exception as e:
#             print("error send_to_sio ", e)
#         return

class SocketServer:
    def __init__(self, secret_jwt='', socket_port=0):
        self.secret_jwt = secret_jwt
        self.socket_port = socket_port
        self.start_runnging12m = False
        self.kegiatan_id = 0
        self.start_runnging10m = False
        self.start_swimming = False
        self.start_shuttlerun = False
        self.start_pushup = False
        self.start_pullup = False
        self.start_chinning = False
        self.rrns = {}
        self.last_distances = {}
        self.detected_dates = {}
        self.start_datetime = datetime.now()

    def rfid_detected_event(self, data):
        # print("data ------------------>", data)
        from entitas.rfid_receiver.services import find_rfid_receiver_db_by_id
        from entitas.rfid_number.services import find_rfid_number_db_by_values
        from entitas.rfid_receiver_number.services import insert_rfid_receiver_number_db
        from entitas.participant.services import find_participant_by_rfid_number_id_and_kegiatan_id

        # data_jwt = ekstrak_jwt(token=request.headers.get("Authorization"))
        # if data_jwt is None:
        #     return
        self.kegiatan_id = data['kegiatan_id']
        rfid_receiver = find_rfid_receiver_db_by_id(id=data['rfid_receiver_id'], to_model=True)
        if rfid_receiver is None:
            return
        rfid_number = find_rfid_number_db_by_values(values=data['value'], to_model=True)
        if rfid_number is None:
            return
        self.kegiatan_id = first_kegiatan_started()
        if rfid_number.id not in self.rrns:
            participant_id = 0
            participant_name = ''
            participant = find_participant_by_rfid_number_id_and_kegiatan_id(rfid_number_id=rfid_number.id, kegiatan_id=self.kegiatan_id)

            if participant is not None:
                participant_id = participant.id
                participant_name = participant.name
            self.rrns[rfid_number.id] = {
                "kegiatan_id": self.kegiatan_id,
                "participant_id": participant_id,
                "participant_name": participant_name,
                "rfid_receiver_id": rfid_receiver.id,
                "rfid_number_name": rfid_number.name,
                "rfid_number_id": rfid_number.id,
                "detected_date": self.start_datetime,
                "status": "detected",
                "last_speed": 0,
                "last_distance": 0,
                "distance": 0,
                "number_of_rounds": 0,
                "excess_distance": 0,
                "elapsted_time": 0
            }
        last_distance = rfid_receiver.get_distance_from_start(track_number=rfid_number.track_number)
        elapsted_time = (datetime.strptime(data['detected_date'],
                                           "%Y-%m-%d %H:%M:%S.%f") - self.start_datetime).total_seconds()
        last_speed = last_distance / elapsted_time
        rrn = {
            "kegiatan_id": self.rrns[rfid_number.id]['kegiatan_id'],
            "participant_id": self.rrns[rfid_number.id]['participant_id'],
            "participant_name": self.rrns[rfid_number.id]['participant_name'],
            "status": "detected",
            "rfid_receiver_id": rfid_receiver.id,
            "rfid_number_name": rfid_number.name,
            "rfid_number_id": rfid_number.id,
            "detected_date": data['detected_date'],
            "last_speed": last_speed,
            "last_distance": last_distance,
            "distance": last_distance,
            "number_of_rounds": 0,
            "excess_distance": 0,
            "elapsted_time": elapsted_time,
            "direction": None
        }
        self.rrns[rfid_number.id] = rrn
        result = insert_rfid_receiver_number_db(json_object=rrn)
        return result


    def shuttlerun_event(self, data):
        self.start_shuttlerun = data['status']
        self.start_datetime = datetime.now()
        self.kegiatan_id = data['kegiatan_id']
        self.participant_id = data['participant_id']
        started = False
        if data['status'].upper() == 'START':
            started = True
        # update_started(id=self.kegiatan_id, started=started)
        update_kegiatan_participant_for_started(kegiatan_id=self.kegiatan_id, participant_id=self.participant_id, started=started)
        return data

    def pushup_event(self, data):
        self.start_pushup = data['status']
        self.start_datetime = datetime.now()
        self.kegiatan_id = data['kegiatan_id']
        self.participant_id = data['participant_id']
        started = False
        if data['status'].upper() == 'START':
            started = True
        # update_started(id=self.kegiatan_id, started=started)
        update_kegiatan_participant_for_started(kegiatan_id=self.kegiatan_id, participant_id=self.participant_id, started=started)
        print('pushup_event')
        return data

    def situp_event(self, data):
        self.start_pushup = data['status']
        self.start_datetime = datetime.now()
        self.kegiatan_id = data['kegiatan_id']
        self.participant_id = data['participant_id']
        started = False
        if data['status'].upper() == 'START':
            started = True
        # update_started(id=self.kegiatan_id, started=started)
        update_kegiatan_participant_for_started(kegiatan_id=self.kegiatan_id, participant_id=self.participant_id, started=started)
        return data

    def pullup_event(self, data):
        self.start_pullup = data['status']
        self.start_datetime = datetime.now()
        self.kegiatan_id = data['kegiatan_id']
        self.participant_id = data['participant_id']
        started = False
        if data['status'].upper() == 'START':
            started = True
        # update_started(id=self.kegiatan_id, started=started)
        update_kegiatan_participant_for_started(kegiatan_id=self.kegiatan_id, participant_id=self.participant_id, started=started)
        return data

    def swimming_event(self, data):
        self.start_swimming = data['status']
        self.start_datetime = datetime.now()
        self.kegiatan_id = data['kegiatan_id']
        self.participants = data['participants']
        started = False
        if data['status'].upper() == 'START':
            started = True
        update_kegiatan_participant_running_for_started(kegiatan_id=self.kegiatan_id, started=started)
        # update_kegiatan_participant_for_started(kegiatan_id=self.kegiatan_id, participant_id=self.participant_id, started=started)
        return data

    def chinning_event(self, data):
        self.start_chinning = data['status']
        self.start_datetime = datetime.now()
        self.kegiatan_id = data['kegiatan_id']
        self.participant_id = data['participant_id']
        started = False
        if data['status'].upper() == 'START':
            started = True
        # update_started(id=self.kegiatan_id, started=started)
        update_kegiatan_participant_for_started(kegiatan_id=self.kegiatan_id, participant_id=self.participant_id, started=started)
        return data

    def pushup_detected_event(self, data):
        # data['kegiatan_id'] = first_kegiatan_started()
        if data['kegiatan_id'] == 0:
            return
        self.kegiatan_id = data['kegiatan_id']
        self.participant_id = data['participant_id']
        self.start_datetime = datetime.now()
        return data

    def pullup_detected_event(self, data):
#         data['kegiatan_id'] = first_kegiatan_started()
        if data['kegiatan_id'] == 0:
            return
        self.kegiatan_id = data['kegiatan_id']
        self.participant_id = data['participant_id']
        self.start_datetime = datetime.now()
        return data

    def chinning_detected_event(self, data):
#         data['kegiatan_id'] = first_kegiatan_started()
        if data['kegiatan_id'] == 0:
            return
        self.kegiatan_id = data['kegiatan_id']
        self.participant_id = data['participant_id']
        self.start_datetime = datetime.now()
        return data

    def shuttlerun_detected_event(self, data):
#         data['kegiatan_id'] = first_kegiatan_started()
        if data['kegiatan_id'] == 0:
            return
        self.kegiatan_id = data['kegiatan_id']
        self.participant_id = data['participant_id']
        self.start_datetime = datetime.now()
        return data

    def situp_detected_event(self, data):
#         data['kegiatan_id'] = first_kegiatan_started()
        if data['kegiatan_id'] == 0:
            return
        self.kegiatan_id = data['kegiatan_id']
        self.participant_id = data['participant_id']
        self.start_datetime = datetime.now()
        return data

    def swimming_detected_event(self, data):
#         data['kegiatan_id'] = first_kegiatan_started()
        if data['kegiatan_id'] == 0:
            return
        self.kegiatan_id = data['kegiatan_id']
        self.start_datetime = datetime.now()
        return data
