from entitas.anggota_topic_chat.resources import *
from entitas.topic_chat.resources import *
from entitas.user.resources import *
from entitas.echo.resources import *
from entitas.message_chat.resources import *
from entitas.chat.resources import *
from entitas.group.resources import *
from entitas.anggota_group.resources import *

def core_routes(api):
    api.add_route("/api/echo", EchoResource())
    api.add_route("/api/python_version", PythonVersionResource())
    api.add_route("/api/test_error", TesstErrorResource())
    api.add_route("/api/test_env", TestEnvResource())
    api.add_route("/api/user/login", UserLoginResource())
    api.add_route("/api/user/signup", RegisterGuruResource())
    api.add_route("/api/forgot_password", ForgotPasswordResource())
    api.add_route('/api/verify-code', VerifyCodeResource())
    api.add_route('/api/reset-password', ResetPasswordResource())
    api.add_route('/api/chat/class/{class_id}', ChatResource())
    api.add_route('/api/chat/class/{class_id}/receiver/{receiver_id}', ChatByClassIdAndSenderIdAndReceiverId())
    api.add_route('/api/chat/{chat_id}/class/{class_id}', ChatWithIdResource())
    api.add_route('/api/message_chat', MessageChatResource())
    api.add_route('/api/message_chat/{message_chat_id}', MessageChatWithIdResource())
    api.add_route('/api/class/{class_id}/group', GroupResources())
    api.add_route('/api/group/{group_id}/class/{class_id}', GroupWithIdResources())
    api.add_route('/api/anggota_group/{group_id}/class/{class_id}', AnggotaGroupResources())
    api.add_route('/api/delete_anggota_group/{anggota_group_id}/class/{class_id}', AnggotaGroupWithIdResources())
    api.add_route('/api/class/{class_id}/topic_chat', TopicChatResources())
    api.add_route('/api/topic_chat/{topic_chat_id}/class/{class_id}', TopicChatWithIdResources())
    api.add_route('/api/anggota_topic_chat/{topic_chat_id}/class/{class_id}', AnggotaTopicChatResources())
    api.add_route('/api/delete_anggota_topic_chat/{anggota_topic_chat_id}/class/{class_id}', AnggotaTopicChatWithIdResources())
    api.add_route('/api/chat/class/{class_id}/topic_chat/{topic_chat_id}', ChatByClassIdAndTopicChatIdResource())
    api.add_route('/api/chat/class/{class_id}/group/{group_id}', ChatByClassIdAndGroupIdResource())
    api.add_route('/api/chat/chat/{chat_id}/class/{class_id}/group/{group_id}', ChatByClassIdAndGroupIdWithIdResource())
    api.add_route('/api/chat/{chat_id}/class-id/{class_id}/group-id{group_id}', ChatByClassIdAndByGroupIdResource())