from pony.orm import *

from database.schema import AnnouncementDB


@db_session
def get_all(to_model=True):
    result = []
    try:
        for item in select(s for s in AnnouncementDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to.response())
    except Exception as e:
        print("error Announcement getAll: ", e)
    return result


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in AnnouncementDB).order_by(desc(AnnouncementDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.name)
            elif item["field"] == "is_published":
                data_in_db = data_in_db.filter(lambda d: d.is_published == item["value"])

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
        print("error getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in AnnouncementDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def publish_by_id(id=None, is_published=False):
    data_in_db = select(s for s in AnnouncementDB if s.id == id)
    if data_in_db.first() is None:
        return
    data_in_db.first().is_published = is_published
    commit()
    return True


@db_session
def update(json_object={}, to_model={}):
    try:
        updated_announcement = AnnouncementDB[json_object["id"]]
        updated_announcement.name = json_object["name"]
        updated_announcement.description = json_object["description"]
        commit()
        if to_model:
            return updated_announcement.to_model()
        else:
            return updated_announcement.to_model().to_response()
    except Exception as e:
        print("error Announcement update: ", e)
    return None


@db_session
def delete_by_id(id=None):
    try:
        AnnouncementDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Announcement delete: ", e)
    return


@db_session
def insert(json_object={}, to_model=False):
    try:
        new_announcement = AnnouncementDB(
            name = json_object["name"],
            description = json_object["description"],
        )
        commit()
        if to_model:
            return new_announcement.to_model()
        else:
            return new_announcement.to_model().to_response()
    except Exception as e:
        print("error Announcement insert: ", e)
    return None