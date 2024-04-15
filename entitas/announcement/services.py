from entitas.announcement import repositoriesDB


def get_announcement_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_announcement_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


def update_announcement_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)

def insert_announcement_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)


def delete_announcement_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

def update_announcement_for_publish_by_id(id=None, is_published=False):
    return repositoriesDB.publish_by_id(id=id, is_published=is_published)
