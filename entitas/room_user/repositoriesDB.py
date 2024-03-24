from pony.orm import *

from database.schema import RoomUserDB


@db_session
def get_all(to_model=True):
    result = []
    try:
        for item in select(s for s in RoomUserDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to.response())
    except Exception as e:
        print("error Room getAll: ", e)
    return result


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in RoomUserDB).order_by(desc(RoomUserDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.name)

        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_model())

    except Exception as e:
        print("error getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in RoomUserDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def update(json_object={}, to_model={}):
    try:
        updated_room_user = RoomUserDB[json_object["id"]]
        updated_room_user.room_id = json_object["room_id"]
        updated_room_user.user_id = json_object["user_id"]
        updated_room_user.last_comment_user_id = json_object["last_comment_user_id"]
        updated_room_user.last_comment_text = json_object["last_comment_text"]
        updated_room_user.last_comment_date = json_object["last_comment_date"]
        updated_room_user.user_id = json_object["user_id"]
        updated_room_user.avatar_url = json_object["avatar_url"]
        commit()
        if to_model:
            return updated_room_user.to_model()
        else:
            return updated_room_user.to_model().to_response()
    except Exception as e:
        print("error Room update: ", e)
    return None


@db_session
def delete_by_id(id=None):
    try:
        RoomUserDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Room delete: ", e)
    return


@db_session
def insert(json_object={}, to_model=False):
    try:
        new_room_user = RoomUserDB(
            room_id = json_object["room_id"],
            user_id = json_object["user_id"],
            avatar_url = json_object["avatar_url"],
        )
        commit()
        if to_model:
            return new_room_user.to_model()
        else:
            return new_room_user.to_model().to_response()
    except Exception as e:
        print("error Room insert: ", e)
    return None