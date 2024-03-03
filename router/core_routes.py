from entitas.absent.resources import *
from entitas.assignment.resources import *
from entitas.assignment_user.resources import *
from entitas.certificate.resources import *
from entitas.notification.resources import *
from entitas.pathway.resources import *
from entitas.pathway_training.resources import *
from entitas.pathway_user.resources import *
from entitas.room.resources import *
from entitas.room_user.resources import *
from entitas.schedule.resources import *
from entitas.schedule_instructur.resources import *
from entitas.schedule_user.resources import *
from entitas.training_material.resources import *
from entitas.training_user.resources import *
from entitas.user.resources import *
from entitas.echo.resources import *
from entitas.material.resources import *
from entitas.training.resources import *
from entitas.instructur.resources import *


def core_routes(api):
    api.add_route("/api/echo", EchoResource())
    api.add_route("/api/python_version", PythonVersionResource())
    api.add_route("/api/test_error", TesstErrorResource())
    api.add_route("/api/test_env", TestEnvResource())
    api.add_route("/api/user/login", UserLoginResource())
    api.add_route("/api/user/signup", UserSignupResource())
