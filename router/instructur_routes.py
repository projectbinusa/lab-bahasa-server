from entitas.schedule.resources import *
from entitas.schedule_user.resources import *
from entitas.material.resources import *
from entitas.training.resources import *
from entitas.assignment.resources import *


def instructur_routes(api):
    api.add_route("/api/instructur/training/{training_id}", InstructurTrainingWithIdResource())
    api.add_route("/api/instructur/training", InstructurTrainingResource())
    api.add_route("/api/instructur/training/{training_id}/material", InstructurTrainingMaterialWithTrainingIdResource())
    api.add_route("/api/instructur/training/{training_id}/material/{material_id}", InstructurMaterialWithIdResource())
    api.add_route("/api/instructur/calendar", InstructurCalendarResource())
    api.add_route("/api/instructur/calendar/{schedule_id}/participant", InstructurCalendarScheduleParticipantResource())
    api.add_route("/api/instructur/calendar/{schedule_id}/assignment", InstructurCalendarScheduleAssignmentResource())
    api.add_route("/api/instructur/calendar/{schedule_id}/assignment/{assignment_id}", InstructurCalendarScheduleAssignmentByAssignmentIdResource())
    api.add_route("/api/instructur/calendar/{schedule_id}/participant/generate_certificate", InstructurCalendarScheduleParticipantGenerateCertificateResource())
    api.add_route("/api/instructur/calendar/{schedule_id}/participant/{schedule_user_id}/score", InstructurCalendarScheduleParticipantScoreResource())