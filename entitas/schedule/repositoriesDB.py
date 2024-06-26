from pony.orm import *
from database.schema import ScheduleDB


@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in ScheduleDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error Schedule getAll ", e)
    return result

@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in ScheduleDB).order_by(desc(ScheduleDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.id)
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.name)
            elif item['field'] == "ids":
                data_in_db = data_in_db.filter(lambda d: d.id in item["value"])

        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            if to_model:
                result.append(item.to_model().to_response())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print("error Schedule getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }
@db_session
def get_training_ids_by_schedule_ids(schedule_ids=[]):
    result = []
    try:
        for item in select(s for s in ScheduleDB if s.id in schedule_ids):
            result.append(item.training_id)
    except Exception as e:
        print("error get_training_ids_by_schedule_ids: ", e)
    return result

@db_session
def get_all_by_time(year=0, month=0, ids=[]):
    result = []
    try:
        if len(ids) == 0:
            for item in select(s for s in ScheduleDB if s.active and s.start_date.year == year and s.start_date.month == month).order_by(ScheduleDB.start_date):
                result.append(item.to_model().to_response_calendar())
        else:
            for item in select(s for s in ScheduleDB if s.active and s.id in ids and s.start_date.year == year and s.start_date.month == month).order_by(ScheduleDB.start_date):
                result.append(item.to_model().to_response_calendar())

    except Exception as e:
        print("error Schedule get_all_by_time: ", e)
    return result

@db_session
def find_by_id(id=None):
    from database.schema import UserDB
    # data_in_db = select((s, u) for s in ScheduleDB for u in UserDB if s.id == id and u.user_id == u.id).first()
    data_in_db = select(s for s in ScheduleDB if s.id == id)
    # data_in_db = select((an, ac) for an in ScheduleDB for ac in UserDB if an.user_id == ac.id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def update(json_object={}, to_model=False):
    try:
        updated_schedule = ScheduleDB[json_object["id"]]
        updated_schedule.name = json_object["name"]
        updated_schedule.training_id = json_object["training_id"]
        updated_schedule.training_name = json_object["training_name"]
        updated_schedule.training_image_url = json_object['training_image_url']
        updated_schedule.is_online = json_object["is_online"]
        updated_schedule.location = json_object["location"]
        updated_schedule.active = json_object["active"]
        updated_schedule.other_link = json_object['other_link']
        updated_schedule.start_date = json_object["start_date"]
        updated_schedule.end_date = json_object["end_date"]
        if 'program' in json_object:
            updated_schedule.program = json_object["program"]

        if 'pic_wa' in json_object:
            updated_schedule.pic_wa = json_object['pic_wa']
        commit()
        if to_model:
            return updated_schedule.to_model()
        else:
            return updated_schedule.to_model().to_response()

    except Exception as e:
        print("error Schedule update: ", e)
    return None

@db_session
def update_link(id=0, link=''):
    try:
        updated_schedule = ScheduleDB[id]
        updated_schedule.link = link
        commit()
        return True

    except Exception as e:
        print("error Schedule update_link: ", e)
    return

@db_session
def update_is_finish(id=0, is_finish=False):
    try:
        updated_schedule = ScheduleDB[id]
        updated_schedule.is_finish = is_finish
        commit()
        return True

    except Exception as e:
        print("error Schedule update_is_finish: ", e)
    return

@db_session
def delete_by_id(id=None):
    try:
        ScheduleDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Schedule deleteById: ", e)
    return

@db_session
def insert(json_object={}, to_model=False):
    try:
        if 'pic_wa' not in json_object:
            json_object['pic_wa'] = ''
            json_object['is_online'] = 0
            json_object['other_link'] = ''
        if 'program' not in json_object:
            json_object['program'] = ''
        new_schedule = ScheduleDB(
            name=json_object["name"],
            training_id=json_object["training_id"],
            training_name=json_object["training_name"],
            training_image_url=json_object['training_image_url'],
            other_link=json_object["other_link"],
            is_online=json_object["is_online"],
            location=json_object["location"],
            active=json_object["active"],
            start_date=json_object["start_date"],
            end_date=json_object["end_date"],
            pic_wa=json_object['pic_wa'],
            program=json_object['program']
        )
        commit()
        if to_model:
            return new_schedule.to_model()
        else:
            return new_schedule.to_model().to_response()
    except Exception as e :
        print("error Schedule insert: ", e)
    return None
