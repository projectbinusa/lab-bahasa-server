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


def user_routes(api):
    api.add_route("/api/user/refresh_token", UserRefreshTokenResource())
    api.add_route("/api/user/password", UserUpdatePasswordWithResource())
    api.add_route("/api/user/profile", UserUpdateProfileWithIdResource())
    api.add_route("/api/user/logout", UserLogoutWithIdResource())
    api.add_route("/api/user/forgot_password", UserForgotPasswordWithResource())
    api.add_route("/api/user/reset_password/{token}", UserResetPasswordWithResource())
    api.add_route("/api/user/activation/{token}", UserActivationResource())
    api.add_route("/api/user/absent/{absent_id}", AbsentWithIdResource())
    api.add_route("/api/user/absent", AbsentResource())
    api.add_route("/api/user/assignment_user/{assignment_user_id}", AssignmentUserWithIdResource())
    api.add_route("/api/user/assignment_user", AssignmentUserResource())
    api.add_route("/api/user/certificate/{certificate_id}", CertificateWithIdResource())
    api.add_route("/api/user/certificate", CertificateResource())
    api.add_route("/api/notification/{notification_id}", NotificationWithIdResource())
    api.add_route("/api/notification", NotificationResource())
    api.add_route("/api/user/pathway", PathwayResource())
    api.add_route("/api/user/pathway_user", UserPathwayUserResource())
    api.add_route("/api/user/scheduler_user/{scheduler_user_id}", SchedulerUserWithIdResource())
    api.add_route("/api/user/scheduler_user", SchedulerUserResource())
    api.add_route("/api/user/training_user/{training_user_id}", TrainingUserWithIdResource())
    api.add_route("/api/user/training_user", TrainingUserResource())


