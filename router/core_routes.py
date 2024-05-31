from entitas.user.resources import *
from entitas.echo.resources import *
from entitas.message_chat.resources import *
from entitas.chat.resources import *

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
    api.add_route('/api/chat', ChatResource())
    api.add_route('/api/chat/{chat_id}', ChatWithIdResource())
    api.add_route('/api/message_chat', MessageChatResource())
    api.add_route('/api/message_chat/{message_chat_id}', MessageChatWithIdResource())
