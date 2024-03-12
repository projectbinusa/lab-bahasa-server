from entitas.pathway_user import repositoriesDB

def get_pathway_user_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_pathway_user_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()


def update_pathway_user_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)

def update_pathway_user_by_user(pathway_ids=[], user_id=0, user_name=''):
    existing = repositoriesDB.get_all_by_user_id(user_id=user_id)
    print('pathway_ids ', pathway_ids)
    for i in range(len(existing)):
        founded = False
        for j in range(len(pathway_ids)):
            if existing[i] == pathway_ids[j]:
                founded = True
                break
        if not founded:
            repositoriesDB.delete_by_user_and_pathway(user_id=user_id, pathway_id=existing[i])

    for j in range(len(pathway_ids)):
        founded = False
        for i in range(len(existing)):
            if existing[i] == pathway_ids[j]:
                founded = True
                break
        if not founded:
            from entitas.pathway.services import find_pathway_db_by_id
            pathway = find_pathway_db_by_id(id=pathway_ids[j], to_model=True)
            if pathway is not None:
                repositoriesDB.insert(json_object={
                    'pathway_id': pathway_ids[j],
                    'pathway_name': pathway.name,
                    'user_id': user_id,
                    'user_name': user_name
                }, to_model=True)

    return True

def insert_pathway_user_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)


def delete_pathway_user_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

