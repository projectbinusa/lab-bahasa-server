from pony.orm import *

from database.schema import TrainingDB

@db_session
def get_all(to_model=False):
    result= []
    try:
        for item in select(s for s in TrainingDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error TrainingDB getAll: ", e)
    return result

@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result= []
    total_record = 0
    try:
        data_in_db = select(s for s in TrainingDB).order_by(desc(TrainingDB.id))
        for item in filters:
            if item["filed"] == "id":
                data_in_db = data_in_db.filter(id=item["value"])
            elif item["filed"] == "name":
                data_in_db = data_in_db.filters(lambda  d: d.name == item["value"])

        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response)

    except Exception as e:
        print("error TrainingDB getAllWithPagination ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }