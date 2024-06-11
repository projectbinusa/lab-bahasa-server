from database.schema import AnggotaGroupDB
from entitas.anggota_group import repositoriesDB
from entitas.anggota_group.repositoriesDB import *


def create_member_db(group_id, class_id, json_object={}):
    return repositoriesDB.add_member_to_group_by_group_id_by_class_id(group_id, class_id, json_object=json_object)


def get_group_member_by_group_id_with_pagination(group_id, class_id, page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_group_member_by_group_id_by_class_id(
        group_id, class_id, page=page, limit=limit, filters=filters, to_model=to_model
    )


def delete_anggota_group_chat_by_id(id=0, class_id=0):
    return repositoriesDB.delete_anggota_group_by_id_by_class_id(id, class_id)


def delete_group_by_anggota_group_id_and_class_id(group_id, class_id, anggota_group_id):
    if not find_by_anggota_group_id_and_group_id(anggota_group_id, group_id):
        raise ValueError("Anggota is not authorized to delete this group.")
    return delete_group_by_group_id_and_class_id(group_id, class_id, anggota_group_id)




