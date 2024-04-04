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


def admin_routes(api):
    api.add_route("/api/admin/user", UserSignupResource())
    api.add_route("/api/admin/user/getAll", UserResource())
    api.add_route("/api/admin/user/{user_id}/profile", AdminUserUpdateProfileWithIdResource())
    api.add_route("/api/admin/material", MaterialResource())
    api.add_route("/api/admin/material/{material_id}", MaterialWithIdResource())
    api.add_route("/api/admin/instructur", AdminInstructurResource())
    api.add_route("/api/admin/instructur/{instructur_id}", AdminUserUserIdResource())
    api.add_route("/api/admin/assignment/{assignment_id}", AssignmentWithIdResource())
    api.add_route("/api/admin/assignment", AssignmentResource())
    api.add_route("/api/admin/pathway/{pathway_id}", PathwayWithIdResource())
    api.add_route("/api/admin/pathway", PathwayResource())
    api.add_route("/api/admin/pathway_traning/{pathway_traning_id}", PathwayTrainingWithIdResource())
    api.add_route("/api/admin/pathway_traning", PathwayTrainingResource())
    api.add_route("/api/admin/room/{room_id}", RoomWithIdResource())
    api.add_route("/api/admin/room", RoomResource())
    api.add_route("/api/admin/room_user/{room_user_id}", RoomUserWithIdResource())
    api.add_route("/api/admin/room_user", RoomUserResource())
    api.add_route("/api/admin/schedule/{schedule_id}", ScheduleWithIdResource())
    api.add_route("/api/admin/schedule", ScheduleResource())
    api.add_route("/api/admin/training/{training_id}", TrainingWithIdResource())
    api.add_route("/api/admin/training", TrainingResource())
    api.add_route("/api/admin/training_material/{training_material_id}", TrainingMaterialWithIdResource())
    api.add_route("/api/admin/training_material", TrainingMaterialResource())
    api.add_route("/api/admin/absent", AdminAbsentResource())
    api.add_route("/api/admin/training/{training_id}/material", TrainingMaterialWithTrainingIdResource())
    api.add_route("/api/admin/training/{training_id}/material/{material_id}", MaterialWithIdResource())
    api.add_route("/api/admin/schedule/{schedule_id}/instructur/{instructur_id}", ScheduleInstructurByIdWithScheduleIdResource())
    api.add_route("/api/admin/schedule/{schedule_id}/instructur", ScheduleInstructurByScheduleResource())
    api.add_route("/api/admin/schedule_instructur/{schedule_instructur_id}", ScheduleInstructurWithIdResource())
    api.add_route("/api/admin/schedule_instructur", ScheduleInstructurResource())
    api.add_route("/api/admin/calendar", AdminCalendarResource())
    api.add_route("/api/admin/mytraining", AdminMytrainingResource())