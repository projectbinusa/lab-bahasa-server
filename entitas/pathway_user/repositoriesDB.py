from pony.orm import *

from database.schema import PathwayUserDB


@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in PathwayUserDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error PathwayUserDB getAll: ", e)
    return result


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in PathwayUserDB).order_by(desc(PathwayUserDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(id=item["value"])
            elif item["field"] == "pathway_id":
                data_in_db = data_in_db.filter(pathway_id=item["value"])
            elif item["field"] == "user_id":
                data_in_db = data_in_db.filter(user_id=item["value"])
            elif item["field"] == "pathway_name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.pathway_name)


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
        print("error PathwayUserDB getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in PathwayUserDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def update(json_object={}, to_model=False):
    try:
        updated_pathway_user = PathwayUserDB[json_object["id"]]
        updated_pathway_user.pathway_id = json_object["pathway_id"]
        updated_pathway_user.pathway_name = json_object["pathway_name"]
        updated_pathway_user.user_id = json_object["user_id"]
        commit()
        if to_model:
            return updated_pathway_user.to_model()
        else:
            return updated_pathway_user.to_model().to_response()
    except Exception as e:
        print("error Material update: ", e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        PathwayUserDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Material deleteById: ", e)
    return


@db_session
def insert(json_object={}, to_model=False):
    try:
        new_pathway_user = PathwayUserDB(
            pathway_id=json_object["pathway_id"],
            pathway_name=json_object["pathway_name"],
            user_id=json_object["user_id"],
            user_name=json_object['user_name']
        )
        commit()
        if to_model:
            return new_pathway_user.to_model()
        else:
            return new_pathway_user.to_model().to_response()
    except Exception as e:
        print("error Material insert: ", e)
        return None

@db_session
def get_all_by_user_id(user_id=0):
    result = []
    for item in select(s for s in PathwayUserDB if s.user_id == user_id):
        result.append(item.pathway_id)
    return result

@db_session
def delete_by_user_and_pathway(user_id=0, pathway_id=0):
    delete(s for s in PathwayUserDB if s.user_id == user_id and s.pathway_id == pathway_id)
    commit()