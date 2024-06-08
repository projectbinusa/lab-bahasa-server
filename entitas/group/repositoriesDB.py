from pony.orm import *
from database.schema import GroupDB


@db_session
def create_group_by_class_id(class_id, json_object={}, to_model=False):
    try:
        new_group = GroupDB(
            class_id=class_id,
            name=json_object["name"],
            description=json_object["description"],
            is_removed=json_object["is_removed"],
        )
        commit()
        if to_model:
            return new_group.to_model()
        else:
            return new_group.to_model().to_json()
    except Exception as e:
        print("error group insert: ", e)
    return


@db_session
def get_all_with_pagination_by_class_id(class_id, page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in GroupDB if (s.class_id == class_id)).order_by(desc(GroupDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(id=item["value"])
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.name)

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
        print("error Group getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def update_group_chat(class_id=None, json_object=None, to_model=False):
    try:
        updated_group = GroupDB.get(id=json_object["id"], class_id=class_id)
        if "name" in json_object:
            updated_group.name = json_object["name"]
        if "description" in json_object:
            updated_group.description = json_object["description"]
        if "is_removed" in json_object:
            updated_group.is_removed = json_object["is_removed"]

        commit()

        if to_model:
            return updated_group.to_model()
        else:
            return updated_group.to_model().to_response()
    except Exception as e:
        print("error MessageChatDB update_chat " + str(e))
        return


@db_session
def delete_anggota_group_by_id_by_class_id(id=None, class_id=None):
    try:
        GroupDB.get(id=id, class_id=class_id).delete()
        commit()
        return True
    except Exception as e:
        print("error Group delete: ", e)
        return False


@db_session
def find_by_group_id_and_class_id(id=None, class_id=0):
    data_in_db = select(s for s in GroupDB if s.id == id and s.class_id == class_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

