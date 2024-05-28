from pony.orm import db_session, select, commit, desc
from database.schema import WhiteboardDB


@db_session
def get_all(to_model=True):
    result = []
    try:
        for item in select(s for s in WhiteboardDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())
    except Exception as e:
        print("error Room getAll: ", e)
    return result


@db_session
def get_all_by_class_id(class_id, to_model=True):
    result = []
    try:
        for item in select(s for s in WhiteboardDB if s.class_id == class_id):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_response())
    except Exception as e:
        print("error get_all_by_class_id: ", e)
    return result


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in WhiteboardDB)

        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
            elif item["field"] == "user_id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.user_id)

        total_record = data_in_db.count()

        data_in_db = data_in_db.order_by(lambda s: desc(s.id))[(page - 1) * limit: page * limit]

        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_response())

    except Exception as e:
        print("error getAllWithPagination: ", e)

    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def get_all_with_pagination_by_class(class_id, page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in WhiteboardDB if s.class_id == class_id).order_by(desc(WhiteboardDB.id))

        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
            elif item["field"] == "user_id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.user_id)

        total_record = data_in_db.count()

        if limit > 0:
            data_in_db = data_in_db[(page - 1) * limit: page * limit]

        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_response())

    except Exception as e:
        print("error get_all_with_pagination_by_class: ", e)

    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in WhiteboardDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def find_by_whiteboard_id_and_class_id(class_id=0):
    try:
        data_in_db = select(s for s in WhiteboardDB if s.class_id == class_id)
        return data_in_db.first().to_model() if data_in_db.first() else None
    except Exception as e:
        print("Error:", e)
        return None


@db_session
def update(json_object={}, to_model=False):
    try:
        updated_whiteboard = WhiteboardDB[json_object["id"]]
        updated_whiteboard.user_id = json_object["user_id"]
        updated_whiteboard.username = json_object["username"]
        updated_whiteboard.class_id = json_object["class_id"]
        updated_whiteboard.class_name = json_object["class_name"]
        commit()
        if to_model:
            return updated_whiteboard.to_model()
        else:
            return updated_whiteboard.to_model().to_response()
    except Exception as e:
        print("error Whiteboard updated: ", e)
        return None


@db_session
def delete_by_id(id=None):
    try:
        WhiteboardDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Room delete: ", e)
    return


@db_session
def update_delete_by_id(id=None, is_deleted=False):
    try:
        WhiteboardDB[id].is_deleted = is_deleted
        commit()
        return True
    except Exception as e:
        print('error user delete: ', e)
    return


@db_session
def delete_whiteboard_by_id(id=None):
    try:
        WhiteboardDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Whiteboard delete: ", e)
    return


@db_session
def create_profile_manage_student_list(json_object=None, to_model=False):
    try:
        # Create new user with the generated class_id
        new_user = WhiteboardDB(
            user_id=json_object['user_id'],
            username=json_object['username'],
            class_id=json_object['class_id'],
            class_name=json_object['class_name']
        )

        commit()

        if to_model:
            return new_user.to_model()
        else:
            return new_user.to_model().to_response()
    except Exception as e:
        print("error creating profile: " + str(e))
        return None

@db_session
def insert(json_object={}, to_model=False):
    try:
        new_whiteboard = WhiteboardDB(
            user_id=json_object["user_id"],
            username=json_object["username"],
            class_id=json_object["class_id"],
            class_name=json_object["class_name"],
        )
        commit()
        if to_model:
            return new_whiteboard.to_model()
        else:
            return new_whiteboard.to_model().to_response()
    except Exception as e:
        print("error Room insert: ", e)
    return None
