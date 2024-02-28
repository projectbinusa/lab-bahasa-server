from pony.orm import *

from database.schema import RoomDB

@db_session
def get_all(to_model=True):
    result= []
    try:
        for item in select(s for s in RoomDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to.response())
    except Exception as e:
        print("error Room getAll: ", e)
    return result

@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result= []
    total_record= 0
    try:
        data_in_db = select(s for s in RoomDB).order_by(desc(RoomDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(id=item["value"])
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: d.name == item["value"])


        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db(pagenum= page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_model())

    except Exception as e:
        print("error getAllWithPagination: ", e)
    return  result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }
