from pony.orm import *

from database.schema import PathwayDB


@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in PathwayDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error Pathway getAll: ", e)
    return result


@db_session
def get_all_with_pagination(page=0, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in PathwayDB).order_by(desc(PathwayDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filer(id=item["value"])
            elif item["field"] == "name":
                data_in_db = data_in_db.filters(lambda d: d.name == ["value"])

        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
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
    data_in_db = select(s for s in PathwayDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def update(json_object={}, to_model=False):
    try:
        updated_pathway = PathwayDB[json_object["id"]]
        updated_pathway.name = json_object["name"]
        updated_pathway.description = json_object["description"]
        commit()
        if to_model:
            return updated_pathway.to_model()
        else:
            return updated_pathway.to_model().to_response()

    except Exception as e:
        print("error Pathway update: ", e)
    return None

@db_session
def delete_by_id(id=None):
    try:
        PathwayDB.delete()
        commit()
        return True
    except Exception as e:
        print("error Pathway delete: ", e)
    return

@db_session
def insert(json_object={}, to_model=False):
    try:
        new_pathway = PathwayDB(
            name=json_object["name"],
            description=json_object["description"],
            deleted=False
        )
        commit()
        if to_model:
            return new_pathway.to_model()
        else:
            return new_pathway.to_model().to_response()

    except Exception as e:
        print("error Pathway insert: ", e)
    return None