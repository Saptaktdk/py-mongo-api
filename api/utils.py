from api.models import BookModelResponse


def getEntities(dbResponses):
    entityList = []
    for dbResponse in dbResponses:
        entityModel = getEntity(dbResponse)
        entityList.append(entityModel)
    return entityList

def getEntity(dbResponse):
    if dbResponse is not None:
        entityModel = BookModelResponse(
            id = str(dbResponse['_id']),
            title = dbResponse['title'],
            author = dbResponse['author'],
            publication_year=dbResponse['publication_year']
        )
        return entityModel.model_dump()
    return None