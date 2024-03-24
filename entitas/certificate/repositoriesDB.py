from pony.orm import *

from database.schema import CertificateDB, InstructurDB, TrainingDB


@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in CertificateDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error CertificateDB getAll: ", e)
    return result


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in CertificateDB).order_by(desc(CertificateDB.id))
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
        print("error CertificateDB getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in CertificateDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def update(json_object={}, to_model=False):
    try:
        updated_certificate = CertificateDB[json_object["id"]]
        updated_certificate.schedule_id = json_object["schedule_id"]
        updated_certificate.training_id = json_object["training_id"]
        updated_certificate.instructur_name = json_object["instructur_name"]
        updated_certificate.name = json_object["name"]
        updated_certificate.url_file = json_object["url_file"]
        updated_certificate.publish_date = json_object["publish_date"]
        updated_certificate.score = json_object["score"]
        updated_certificate.mark = json_object["mark"]
        commit()
        if to_model:
            return updated_certificate.to_model()
        else:
            return updated_certificate.to_model().to_response()
    except Exception as e:
        print("error Material update: ", e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        CertificateDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Material deleteById: ", e)
    return


@db_session
def insert(json_object={}, to_model=False):
    try:
        new_certificate = CertificateDB(
            sceduler_id=json_object["sceduler_id"],
            training_id=TrainingDB[json_object["training_id"]],
            user_id=TrainingDB[json_object["user_id"]],
            instructur_id=InstructurDB[json_object["instructur_id"]],
            instructur_name=InstructurDB[json_object["instructur_name"]],
            name=json_object["name"],
            url_file=json_object["url_file"],
            publish_date=json_object["publish_date"],
            score=json_object["score"],
            mark=json_object["mark"],
        )
        commit()
        if to_model:
            return new_certificate.to_model()
        else:
            return new_certificate.to_model().to_response()
    except Exception as e:
        print("error Material insert: ", e)
        return None