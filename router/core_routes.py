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
    api.add_route("/api/admin/instructur/{instructur_id}", InstructurWithIdResource)
    api.add_route("/api/user/absent/{absent_id}", AbsentWithIdResource)
    api.add_route("/api/user/absent", AbsentResource)
    api.add_route("/api/admin/assignment/{assignment_id}", AssignmentWithIdResource)
    api.add_route("/api/admin/assignment", AssignmentResource)
    api.add_route("/api/user/assignment_user/{assignment_user_id}", AssignmentUserWithIdResource)
    api.add_route("/api/user/assignment_user", AssignmentUserResource)
    api.add_route("/api/user/certificate/{certificate_id}", CertificateWithIdResource)
    api.add_route("/api/user/certificate", CertificateResource)
    api.add_route("/api/notification/{notification_id}", NotificationWithIdResource)
    api.add_route("/api/notification", NotificationResource)
    api.add_route("/api/admin/pathway/{pathway_id}", PathwayWithIdResource)
    api.add_route("/api/admin/pathway", PathwayResource)
    api.add_route("/api/admin/pathway_traning/{pathway_traning_id}", PathwayTrainingWithIdResource)
    api.add_route("/api/admin/pathway_traning", PathwayTrainingResource)
    api.add_route("/api/user/pathway_user/{pathway_user_id}", PathwayUserWithIdResource)
    api.add_route("/api/user/pathway_user", PathwayUserResource)
    api.add_route("/api/admin/room/{room_id}", RoomWithIdResource)
    api.add_route("/api/admin/room", RoomResource)
    api.add_route("/api/admin/room_user/{room_user_id}", RoomUserWithIdResource)
    api.add_route("/api/admin/room_user", RoomUserResource)
    api.add_route("/api/admin/schedule/{schedule_id}", ScheduleWithIdResource)
    api.add_route("/api/admin/schedule", ScheduleResource)
    api.add_route("/api/admin/scheduler_instructur/{scheduler_instructur_id}", SchedulerInstructurWithIdResource)
    api.add_route("/api/admin/scheduler_instructur", SchedulerInstructurResource)
    api.add_route("/api/user/scheduler_user/{scheduler_user_id}", SchedulerUserWithIdResource)
    api.add_route("/api/user/scheduler_user", SchedulerUserResource)
    api.add_route("/api/admin/training/{training_id}", TrainingWithIdResource)
    api.add_route("/api/admin/training", TrainingResource)
    api.add_route("/api/admin/training_material/{training_material_id}", TrainingMaterialWithIdResource)
    api.add_route("/api/admin/training_material", TrainingMaterialResource)
    api.add_route("/api/user/training_user/{training_user_id}", TrainingUserWithIdResource)
    api.add_route("/api/user/training_user", TrainingUserResource)
