from entitas.user.resources import *
from entitas.echo.resources import *
from entitas.material.resources import *
from entitas.instructur.resources import *

def core_routes(api):
    api.add_route("/api/echo", EchoResource())
    api.add_route("/api/python_version", PythonVersionResource())
    api.add_route("/api/test_error", TesstErrorResource())
    api.add_route("/api/test_env", TestEnvResource())
    api.add_route("/api/user/login", UserLoginResource())
    api.add_route("/api/user/register", UserSignupResource())
    api.add_route("/api/user/refresh_token", UserRefreshTokenResource())
    api.add_route("/api/user/password", UserUpdatePasswordWithResource())
    api.add_route("/api/user/profile", UserUpdateProfileWithIdResource())
    api.add_route("/api/user/logout", UserLogoutWithIdResource())
    api.add_route("/api/user/forgot_password", UserForgotPasswordWithResource())
    api.add_route("/api/user/reset_password/{token}", UserResetPasswordWithResource())
    api.add_route("/api/user/activation/{token}", UserActivationResource())
    api.add_route("/api/admin/material", MaterialResource())
    api.add_route("/api/admin/material/{material_id}", MaterialWithIdResource())
    api.add_route("/api/admin/instructur", InstructurResource)
    api.add_route("/api/admin/instructur/{instructur_id", InstructurWithIdResource)


