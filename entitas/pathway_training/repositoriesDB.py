from pony.orm import *

from database.schema import PathwayTrainingDB


@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in PathwayTrainingDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error PathwayTrainingDB getAll: ", e)
    return result

@db_session
def find_all_by_pathway_id(pathway_id=0):
    result = []
    try:
        for item in select(s for s in PathwayTrainingDB if s.pathway_id == pathway_id):
            result.append(item.to_model())
    except Exception as e:
        print("error PathwayTrainingDB find_all_by_pathway_id: ", e)
    return result


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in PathwayTrainingDB).order_by(PathwayTrainingDB.urut)
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.name)
            elif item["field"] == "pathway_id":
                data_in_db = data_in_db.filter(pathway_id=item["value"])


        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response_trainings())

    except Exception as e:
        print("error PathwayTrainingDB getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in PathwayTrainingDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def update(json_object={}, to_model=False):
    try:
        updated_pathway_training = PathwayTrainingDB[json_object["id"]]
        updated_pathway_training.pathway_id = json_object["pathway_id"]
        updated_pathway_training.training_id = json_object["training_id"]
        commit()
        if to_model:
            return updated_pathway_training.to_model()
        else:
            return updated_pathway_training.to_model().to_response()
    except Exception as e:
        print("error PathwayMaterial update: ", e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        PathwayTrainingDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error PathwayMaterial deleteById: ", e)
    return


@db_session
def insert(json_object={}, to_model=False):
    try:
        new_pathway_training = PathwayTrainingDB(
            pathway_id=json_object["pathway_id"],
            training_id=json_object["training_id"],
            training_name=json_object["training_name"],
            urut=json_object["urut"],
        )
        commit()
        if to_model:
            return new_pathway_training.to_model()
        else:
            return new_pathway_training.to_model().to_response()
    except Exception as e:
        print("error PathwayPathwayMaterial insert: ", e)
        return None