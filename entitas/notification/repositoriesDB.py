from pony.orm import *

from database.schema import NotificationDB


@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in NotificationDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error NotificationDB getAll: ", e)
    return result


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in NotificationDB).order_by(desc(NotificationDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
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
        print("error NotificationDB getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in NotificationDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def update(json_object={}, to_model=False):
    try:
        updated_notification = NotificationDB[json_object["id"]]
        updated_notification.fcm_token = json_object["fcm_token"]
        updated_notification.email = json_object["email"]
        updated_notification.user_id = json_object["user_id"]
        updated_notification.title = json_object["title"]
        updated_notification.message = json_object["message"]
        commit()
        if to_model:
            return updated_notification.to_model()
        else:
            return updated_notification.to_model().to_response()
    except Exception as e:
        print("error Material update: ", e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        NotificationDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Material deleteById: ", e)
    return


@db_session
def insert(json_object={}, to_model=False):
    try:
        new_notification = NotificationDB(
            fcm_token=json_object["fcm_token"],
            email=json_object["email"],
            user_id=json_object["user_id"],
            title=json_object["title"],
            message=json_object["message"],
        )
        commit()
        if to_model:
            return new_notification.to_model()
        else:
            return new_notification.to_model().to_response()
    except Exception as e:
        print("error Material insert: ", e)
        return None