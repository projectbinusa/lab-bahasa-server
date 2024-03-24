from entitas.pathway_training import repositoriesDB

def get_pathway_training_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_pathway_training_db_by_id(id=0, to_model=False):
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    return result.to_response()

def find_all_pathway_training_by_pathway_id(pathway_id=0):
    return repositoriesDB.find_all_by_pathway_id(pathway_id=pathway_id)

def update_pathway_training_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)

def insert_pathway_training_db(json_object={}):
    return repositoriesDB.insert(json_object=json_object)


def delete_pathway_training_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

