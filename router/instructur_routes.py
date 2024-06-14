from entitas.schedule.resources import *
from entitas.schedule_user.resources import *
from entitas.material.resources import *
from entitas.training.resources import *
from entitas.assignment.resources import *
from entitas.assignment_user.resources import *
from entitas.announcement.resources import *
from entitas.log_book.resources import *
from entitas.kelas_user.resources import *
from entitas.user.resources import *
from entitas.question.resources import *
from entitas.login_limit.resources import *
from entitas.whiteboard.resources import *
from entitas.answer.resources import *


def instructur_routes(api):
    api.add_route("/api/instructur/training/{training_id}", InstructurTrainingWithIdResource())
    api.add_route("/api/instructur/training", InstructurTrainingResource())
    api.add_route("/api/instructur/training/{training_id}/material", InstructurTrainingMaterialWithTrainingIdResource())
    api.add_route("/api/instructur/training/{training_id}/material/{material_id}", InstructurMaterialWithIdResource())
    api.add_route("/api/instructur/calendar", InstructurCalendarResource())
    api.add_route("/api/instructur/mytraining", InstructurMytrainingResource())
    api.add_route("/api/instructur/mytraining/{schedule_id}", InstructurMytrainingScheduleIdResource())
    api.add_route("/api/instructur/calendar/{schedule_id}/participant", InstructurCalendarScheduleParticipantResource())
    api.add_route("/api/instructur/calendar/{schedule_id}/assignment", InstructurCalendarScheduleAssignmentResource())
    api.add_route("/api/instructur/calendar/{schedule_id}/assignment/{assignment_id}", InstructurCalendarScheduleAssignmentByAssignmentIdResource())
    api.add_route("/api/instructur/calendar/{schedule_id}/assignment/{assignment_id}/user",
                  InstructurCalendarScheduleAssignmentByAssignmentIdUserResource())
    api.add_route("/api/instructur/calendar/{schedule_id}/assignment/{assignment_id}/user/{assignment_user_id}",
                  InstructurCalendarScheduleAssignmentByAssignmentIdUserIdResource())
    api.add_route("/api/instructur/calendar/{schedule_id}/participant/generate_certificate", InstructurCalendarScheduleParticipantGenerateCertificateResource())
    api.add_route("/api/instructur/calendar/{schedule_id}/participant/{schedule_user_id}/score", InstructurCalendarScheduleParticipantScoreResource())
    api.add_route("/api/instructur/calendar/{schedule_id}/confirmed",
                  InstructurCalendarScheduleParticipantConfirmedResource())
    api.add_route("/api/instructur/mytrain/{schedule_id}/confirmed",
                  InstructurCalendarScheduleParticipantConfirmedResource())
    api.add_route("/api/instructur/mytraining/{schedule_id}/participant", InstructurCalendarScheduleParticipantResource())
    api.add_route("/api/instructur/mytraining/{schedule_id}/assignment", InstructurCalendarScheduleAssignmentResource())
    api.add_route("/api/instructur/mytraining/{schedule_id}/assignment/{assignment_id}",
                  InstructurCalendarScheduleAssignmentByAssignmentIdResource())
    api.add_route("/api/instructur/mytraining/{schedule_id}/assignment/{assignment_id}/user",
                  InstructurCalendarScheduleAssignmentByAssignmentIdUserResource())
    api.add_route("/api/instructur/mytraining/{schedule_id}/assignment/{assignment_id}/user/{assignment_user_id}",
                  InstructurCalendarScheduleAssignmentByAssignmentIdUserIdResource())
    api.add_route("/api/instructur/mytraining/{schedule_id}/participant/generate_certificate",
                  InstructurCalendarScheduleParticipantGenerateCertificateResource())
    api.add_route("/api/instructur/mytraining/{schedule_id}/participant/{schedule_user_id}/score",
                  InstructurCalendarScheduleParticipantScoreResource())
    api.add_route("/api/instructur/announcement", AnnouncementInstructurResource())
    api.add_route("/api/instructur/schedule/{schedule_id}/logbook", LogBookResource())
    api.add_route("/api/instructur/schedule/{schedule_id}/logbook/{log_book_id}", LogBookWithIdResource())
    api.add_route("/api/instructur/class", KelasUserResource())
    api.add_route("/api/instructur/class/{class_id}", KelasUserWithIdResource())
    api.add_route("/api/instructur/class/{class_id}/management_name_list", ManagementListResource())
    # api.add_route("/api/instructur/class/{class_id}/management_name_list/{management_name_list_id}", ManagementListWithByIdResources())
    api.add_route("/api/instructur/management_name_list", UserDeleteByIds())
    api.add_route("/api/instructur/class/{class_id}/response_competition", QuestionResource())
    api.add_route("/api/instructur/response_competition/{response_competition_id}", QuestionWithIdResource())
    api.add_route("/api/instructur/class/{class_id}/login_limits", LoginLimitResource())
    api.add_route("/api/instructur/class/{class_id}/login_limits/{login_limits_id}", LoginLimitWithIdResource())
    api.add_route("/api/instructur/whiteboard/{whiteboard_id}", WhiteboardWithIdResource())
    api.add_route("/api/instructur/class/{class_id}/whiteboard", WhiteboardResource())
    api.add_route("/api/instructur/class/{class_id}/whiteboard/{whiteboard_id}", WhiteboardWithIdResource())
    api.add_route("/api/instructur/class/{class_id}/management_name_list/{management_list_id}", ManagementListWithByIdResources())
    api.add_route('/api/instructur/class/{class_id}/start-competition', StartCompetitionResource())
    # api.add_route('/api/instructur/class/{class_id}/first-to-answer', FirstToAnswerResource())
    # api.add_route('/api/instructur/class/{class_id}/enter-answer', EnterAnswerResource())
    # api.add_route('/api/instructur/class/{class_id}/demo-to-answer', DemoToAnswerResource())
    api.add_route("/api/instructur/update_class_id_user", EditClassIdUserResource())
    api.add_route("/api/instructur/class/{class_id}/answer/{answer_id}", AnswerWithIdResource())
    api.add_route("/api/instructur/class/{class_id}/answer", AnswerResource())
    api.add_route("/api/instructur/class/{class_id}/export/management_name_list", ExportManagementList())
    api.add_route("/api/instructur/class/{class_id}/import/management_name_list", ImportManagementNameList())
    api.add_route("/api/instructur/class_active/{class_id}", KelasUserActive())
    api.add_route("/api/instructur/class_not_active/{class_id}", KelasUserNotActive())
    api.add_route('/api/instructur/class/export', KelasUserExportResource())
    api.add_route('/api/instructur/class/import', KelasUserImportResource())
