# from falcon.app import req
import csv
import uuid

import pandas as pd
from openpyxl.workbook import Workbook
from pony.orm import *
from database.schema import KelasUserDB
from openpyxl.styles import Alignment, Font, PatternFill


@db_session
def get_all(to_model=True):
    result = []
    try:
        for item in select(s for s in KelasUserDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to.response())
    except Exception as e:
        print("error Kelas User getAll: ", e)
    return result


@db_session
def get_kelas_user_ids_by_user_id(user_id=0):
    result = []
    try:
        for item in select(s for s in KelasUserDB if s.user_id == user_id):
            result.append(item.id)
    except Exception as e:
        print("error get_schedule_ids_by_user_id: ", e)
    return result


@db_session
def get_all_with_pagination(page=1, limit=9, filters=[], to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in KelasUserDB).order_by(desc(KelasUserDB.id))
        for item in filters:
            if item["field"] == "id":
                data_in_db = data_in_db.filter(lambda d: item["value"] == d.id)
            elif item["field"] == "name":
                data_in_db = data_in_db.filter(lambda d: item["value"] in d.name)

        total_record = data_in_db.count()
        if limit > 0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            model_instance = item.to_model()
            if to_model:
                result.append(model_instance)
            else:
                if model_instance is not None:
                    result.append(model_instance.to_response())
                else:
                    # Handle case where to_model() returns None
                    print("Warning: to_model() returned None for item with id:", item.id)
    except Exception as e:
        print("error Absen getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


#
@db_session
def get_user_and_schedule_user_with_pagination(page=1, limit=9, filters=[], to_model=False):
    from database.schema import UserDB
    result = []
    total_record = 0
    # try:
    # data_in_db = select(s for s in KelasUserDB).order_by(desc(KelasUserDB.id))
    id = next((x["value"] for x in filters if x.get("field") == "id"), 0)
    data_in_db = select((s, u) for s in KelasUserDB for u in UserDB if s.id == id and s.user_id == u.id)
    for item in filters:
        if item["field"] == "id":
            data_in_db = data_in_db.filter(lambda d, i: item["value"] in d.id)
        elif item["field"] == "name":
            data_in_db = data_in_db.filter(lambda d, i: item["value"] in d.name)

    total_record = data_in_db.count()
    if limit > 0:
        data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
    else:
        data_in_db = data_in_db
    for item, user in data_in_db:
        # if to_model:
        #     result.append(item.to_model())
        # else:
        data = item.to_model().to_response_participant()
        data['user_profile'] = user.to_model().to_response_participant_schedule()
        result.append(data)

    # except Exception as e:
    #     print("error ScheduleUser getAllWithPagination: ", e)
    return result, {
        "total": total_record,
        "page": page,
        "total_page": (total_record + limit - 1) // limit if limit > 0 else 1,
    }


@db_session
def get_kelas_user_ids_by_user_id(user_id=0):
    result = []
    try:
        for item in select(s for s in KelasUserDB if s.user_id == user_id):
            result.append(item.id)
    except Exception as e:
        print("error get_schedule_ids_by_user_id: ", e)
    return result


@db_session
def find_by_id(id=None):
    data_in_db = select(s for s in KelasUserDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def find_by_kelas_user_id_and_user_id(id=None, user_id=0):
    data_in_db = select(s for s in KelasUserDB if s.id == id and s.user_id == user_id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()

@db_session
def find_by_kelas_user_id_and_user_id_and_role(id=None):
    data_in_db = select(s for s in KelasUserDB if s.id == id)
    if data_in_db.first() is None:
        return None
    return data_in_db.first().to_model()


@db_session
def update(json_object={}, to_model={}):
    try:
        updated_kelas_user = KelasUserDB[json_object["id"]]
        updated_kelas_user.name = json_object["name"]
        updated_kelas_user.description = json_object["description"]
        updated_kelas_user.file = json_object["file"]
        commit()
        if to_model:
            print(updated_kelas_user.to_model())
            return updated_kelas_user.to_model()
        else:
            print(updated_kelas_user.to_model().to_response())
            return updated_kelas_user.to_model().to_response()
    except Exception as e:
        print("error Kelas User update: ", e)
    return None


@db_session
def class_active(json_object={}, to_model={}):
    print("json object di repo ==> ", json_object)
    try:
        updated_kelas_user = KelasUserDB[json_object["id"]]
        updated_kelas_user.user_id = json_object["user_id"]
        updated_kelas_user.user_name = json_object["user_name"]
        if "is_active" in json_object:
            updated_kelas_user.is_active = json_object["is_active"]
        commit()
        if to_model:
            print(updated_kelas_user.to_model())
            return updated_kelas_user.to_model()
        else:
            print(updated_kelas_user.to_model().to_response())
            return updated_kelas_user.to_model().to_response()
    except Exception as e:
        print("error Kelas User active: ", e)
    return None


@db_session
def delete_by_id(id=None):
    try:
        KelasUserDB[id].delete()
        commit()
        return True
    except Exception as e:
        print("error Kelas User delete: ", e)
    return


@db_session
def insert(json_object={}, to_model=False):
    try:
        print("kelas user ==> ", json_object)
        json_object["kode_ruang"] = str(uuid.uuid4())
        new_kelas_user = KelasUserDB(
            name=json_object["name"],
            kode_ruang=json_object["kode_ruang"],
            description=json_object["description"],
            file=json_object["file"],
            is_active=json_object["is_active"]
            # is_deleted = json_object["is_deleted"],
        )
        commit()
        if to_model:
            return new_kelas_user.to_model()
        else:
            return new_kelas_user.to_model().to_response()
    except Exception as e:
        print("error Kelas User insert: ", e)
    return None


@db_session
def find_kelas_user_db_by_id(id=0, to_model=False):
    result = find_by_id(id=id)
    print("id ==>", id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


@db_session
def export_class():
    try:
        # Filter data based on class_id and role student
        users = select(u for u in KelasUserDB).order_by(desc(KelasUserDB.id))[:]

        # Create workbook and worksheet
        wb = Workbook()
        ws = wb.active
        ws.title = 'Kelas List'

        # Header row formatting
        header = ["#", "Gambar", "Nama Server", "Nama Kelas", "Deskripsi", "Aktif"]
        ws.append(header)
        for cell in ws[1]:
            cell.font = Font(bold=True)
            cell.fill = PatternFill(start_color="C0C0C0", end_color="C0C0C0", fill_type="solid")
            cell.alignment = Alignment(horizontal="center", vertical="center")

        # Data rows
        for index, user in enumerate(users, start=1):
            row = [
                index,
                user.file,
                user.user_name,
                user.name,
                user.description,
                user.is_active,
            ]
            ws.append(row)

        # Save workbook
        file_path = 'tmp/kelas_list.xlsx'
        wb.save(file_path)

        return True, None, file_path  # Return success and file path

    except Exception as e:
        return False, str(e), None  # Return error message


@db_session
def import_kelas_from_xlsx(file_path='kelas_list.xlsx', to_model=False):
    try:
        df = pd.read_excel(file_path)
        imported_users = []
        for index, row in df.iterrows():
            user = KelasUserDB(
                file=str(row['Gambar']),
                user_name=str(row['Nama Server']),
                name=str(row['Nama Kelas']),
                description=str(row['Deskripsi']),
                is_active=int(row['Aktif']),
            )
            imported_users.append(user)
        commit()

        if to_model:
            return [user.to_model() for user in imported_users]
        else:
            return [user.to_model().to_response() for user in imported_users]

    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        return None

    except Exception as e:
        print(f"Error importing from XLSX: {e}")
        return None