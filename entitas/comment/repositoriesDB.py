from pony.orm import *

from database.schema import CommentDB, UserDB, RoomDB


@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in CommentDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error CommentDB getAll: ", e)
    return result


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in CommentDB).order_by(desc(CommentDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(id=item["value"])
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: d.name == item["value"])


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
        print("error CommentDB getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in CommentDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def update(json_object={}, to_model=False):
    try:
        updated_comment = CommentDB[json_object["id"]]
        updated_comment.comment_for_id = json_object["comment_for_id"]
        updated_comment.is_deleted = json_object["is_deleted"]
        updated_comment.message = json_object["message"]
        updated_comment.room_id = json_object["room_id"]
        updated_comment.room_id = json_object["room_id"]
        updated_comment.status = json_object["status"]
        updated_comment.user_avatar_url = json_object["user_avatar_url"]
        updated_comment.user_id = json_object["user_id"]
        updated_comment.user_name = json_object["user_name"]
        commit()
        if to_model:
            return updated_comment.to_model()
        else:
            return updated_comment.to_model().to_response()
    except Exception as e:
        print("error Material update: ", e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        CommentDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Material deleteById: ", e)
    return


@db_session
def insert(json_object={}, to_model=False):
    try:
        new_comment = CommentDB(
            name=json_object["name"],
            comment_for_id=json_object["comment_for_id"],
            is_deleted=json_object["is_deleted"],
            message=json_object["message"],
            room_id=RoomDB[json_object["room_id"]],
            room_name=RoomDB[json_object["room_name"]],
            status=json_object["status"],
            user_avatar_url=json_object["user_avatar_url"],
            user_id=UserDB[json_object["user_id"]],
            user_name=UserDB[json_object["user_name"]],
        )
        commit()
        if to_model:
            return new_comment.to_model()
        else:
            return new_comment.to_model().to_response()
    except Exception as e:
        print("error Material insert: ", e)
        return None