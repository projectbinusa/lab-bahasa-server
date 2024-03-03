from entitas.pathway import repositoriesDB
from util.other_util import raise_error

def get_pathway_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(
        page=page, limit=limit, filters=filters, to_model=to_model
    )


def find_pathway_db_by_id(id=0, to_model=False):
    from entitas.pathway_training.services import get_pathway_training_db_with_pagination
    result = repositoriesDB.find_by_id(id=id)
    if result is None:
        return None
    if to_model:
        return result
    if not to_model:
        result = result.to_response()
        filters = [{'field': 'pathway_id', 'value': id}]
        result['trainings'], _ = get_pathway_training_db_with_pagination(page=1, limit=1000, filters=filters)
    return result


def update_pathway_db(json_object={}):
    from entitas.pathway_training.services import get_pathway_training_db_with_pagination, delete_pathway_training_by_id, insert_pathway_training_db
    from entitas.training.services import find_training_db_by_id
    repositoriesDB.update(json_object=json_object)
    filters = [{'field': 'pathway_id', 'value': json_object['id']}]
    exiting_trainings, _ = get_pathway_training_db_with_pagination(page=1, limit=1000, filters=filters)
    for i in range(len(json_object['trainings'])):
        finded = False
        for j in range(len(exiting_trainings)):
            if json_object['trainings'][i]['training_id'] == exiting_trainings[j]['training_id']:
                finded = True
                break
        if not finded:
            training = find_training_db_by_id(id=json_object['trainings'][i]['training_id'], to_model=True)
            if training is None:
                raise_error(f"training id {json_object['trainings'][i]['training_id']} not found")
            insert_pathway_training_db(json_object={
                'pathway_id': json_object['id'],
                'training_id': json_object['trainings'][i]['training_id'],
                'training_name': training.name,
                'urut': json_object['trainings'][i]['urut']
            })
    for j in range(len(exiting_trainings)):
        finded = False
        for i in range(len(json_object['trainings'])):
            if json_object['trainings'][i]['training_id'] == exiting_trainings[j]['training_id']:
                finded = True
                break
        if not finded:
            delete_pathway_training_by_id(id=exiting_trainings[j]['id'])
    return True

def insert_pathway_db(json_object={}):
    from entitas.training.services import find_training_db_by_id
    from entitas.pathway_training.services import insert_pathway_training_db
    trainings = []
    for i in range(len(json_object['trainings'])):
        training = find_training_db_by_id(id=json_object['trainings'][i]['training_id'], to_model=True)
        if training is None:
            raise_error(f"training id {json_object['trainings'][i]['training_id']} not found")
        trainings.append({
            'training_id': json_object['trainings'][i]['training_id'],
            'training_name': training.name,
            'urut': json_object['trainings'][i]['urut']
        })

    data = repositoriesDB.insert(json_object=json_object, to_model=True)
    for i in range(len(trainings)):
        trainings[i]['pathway_id'] = data.id
        insert_pathway_training_db(json_object=trainings[i])

    return True


def delete_pathway_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

