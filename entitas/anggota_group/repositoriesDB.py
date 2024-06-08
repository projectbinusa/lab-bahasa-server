from pony.orm import *
from database.schema import AnggotaGroupDB, GroupDB
from entitas.group.repositoriesDB import find_by_group_id_and_class_id


@db_session
def add_member_to_group_by_group_id_by_class_id(group_id, class_id, json_object={}, to_model=False):
    try:
        new_member = AnggotaGroupDB(
            group_id=group_id,
            class_id=class_id,
            user_id=json_object["user_id"],
            role=json_object["role"],
        )
        commit()
        if to_model:
            return new_member.to_model()
        else:
            return new_member.to_model().to_json()
    except Exception as e:
        print("error anggotaGroup insert: ", e)
    return None


@db_session
def get_group_member_by_group_id_by_class_id(group_id, class_id, page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(
            s for s in AnggotaGroupDB if (s.group_id == group_id) and (s.class_id == class_id)).order_by(
            desc(AnggotaGroupDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(id=item["value"])
            elif item["field"] == "role":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.role)

        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error AnggotaGroup getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_anggota_topic_chat_id_and_group_id(id=None, group_id=0):
    data_in_db = select(s for s in AnggotaGroupDB if s.id == id and s.group_id == group_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def delete_anggota_group_by_id_by_class_id(id=None, class_id=None):
    try:
        AnggotaGroupDB.get(id=id, class_id=class_id).delete()
        commit()
        return True
    except Exception as e:
        print("error Chat delete: ", e)
        return False


@db_session
def delete_group_by_group_id_and_class_id(group_id, class_id, anggota_group_id):
    try:
        group = GroupDB.get(id=group_id, class_id=class_id)
        if not group:
            print(f"Group with id {group_id} and class_id {class_id} does not exist.")
            return False

        # Check if the requesting member is authorized and exists in this group
        member = AnggotaGroupDB.get(id=anggota_group_id, group_id=group_id)
        if not member:
            print(f"Member with id {anggota_group_id} is not authorized or does not exist in this group.")
            return False

        # Delete all members associated with this group
        members_to_delete = select(m for m in AnggotaGroupDB if m.group_id == group_id)
        members_to_delete.delete(bulk=True)

        # Now, delete the group
        group.delete()
        commit()

        print(f"Group with id {group_id} and class_id {class_id} and all associated members have been deleted.")
        return True
    except Exception as e:
        print("Error deleting group by group id and class id:", e)
        return False
