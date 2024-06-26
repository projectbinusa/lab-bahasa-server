from entitas.absent.resources import *
from entitas.answer.resources import AnswerResource
from entitas.assignment.resources import *
from entitas.assignment_user.resources import *
from entitas.certificate.resources import *
from entitas.notification.resources import *
from entitas.pathway.resources import *
from entitas.pathway_training.resources import *
from entitas.pathway_user.resources import *
from entitas.announcement.resources import *
from entitas.question.resources import QuestionByClassIdAndUserIdResource, QuestionResource
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
    api.add_route("/api/user/absent/signature", AbsentWithIdSignatureResource())
    api.add_route("/api/user/absent", AbsentResource())
    api.add_route("/api/user/assignment_user/{assignment_user_id}", AssignmentUserWithIdResource())
    api.add_route("/api/user/assignment_user", AssignmentUserResource())
    api.add_route("/api/user/certificate/{certificate_id}", CertificateWithIdResource())
    api.add_route("/api/user/certificate", CertificateResource())
    api.add_route("/api/notification/{notification_id}", NotificationWithIdResource())
    api.add_route("/api/notification", NotificationResource())
    api.add_route("/api/user/pathway", PathwayUserResource())
    api.add_route("/api/user/pathway_user", UserPathwayUserResource())
    api.add_route("/api/user/pathway_user/{pathway_user_id}", UserPathwayByIdResuorce())
    api.add_route("/api/user/schedule_user/{schedule_user_id}", ScheduleUserWithIdResource())
    api.add_route("/api/user/mytraining/{schedule_id}", ScheduleUserWithIdResource())
    api.add_route("/api/user/mytraining/{schedule_id}/feedback", ScheduleUserWithIdFeedbackResource())
    api.add_route("/api/user/schedule_user", ScheduleUserResource())
    api.add_route("/api/user/calendar", UserCalendarResource())
    api.add_route("/api/user/mytraining", UserCalendarResource())
    api.add_route("/api/user/calendar/{schedule_id}/assignment/{assignment_id}",
                  UserCalendarScheduleAssignmentByAssignmentIdResource())
    api.add_route("/api/user/training_user/{training_user_id}", TrainingUserWithIdResource())
    api.add_route("/api/user/training_user", TrainingUserResource())
    api.add_route("/api/user/pathway_training", PathwayTrainingResource())
    api.add_route("/api/user/calendar/{schedule_id}/confirmed",
                  InstructurCalendarScheduleParticipantConfirmedResource())
    api.add_route("/api/user/mytrain/{schedule_id}/confirmed",
                  InstructurCalendarScheduleParticipantConfirmedResource())
    api.add_route("/api/api/user/mytrain/{schedule_id}/confirmed",
                  InstructurCalendarScheduleParticipantConfirmedResource())
    api.add_route("/api/user/announcement", AnnouncementStudentResource())
    api.add_route("/api/user/class/{class_id}/answer", AnswerResource())
    api.add_route("/api/user/class/{class_id}/question", QuestionResource())
