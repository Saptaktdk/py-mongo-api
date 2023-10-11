from api.models import BookModel, BookQueryModel
from pymongo import ReturnDocument
from api.utils import getEntities, getEntity


class BookQuery():
    def __init__(self):
        print("Initialized BookQuery")

    @staticmethod
    async def getMany(model: BookModel, query: BookQueryModel):
        return getEntities(model.find(limit=10))

    @staticmethod
    async def getOne(model: BookModel, query: BookQueryModel):
        return getEntity(model.find_one(query))

    @staticmethod
    async def addOne(model: BookModel, book: BookModel):
        return model.insert_one(book)

    @staticmethod
    async def updateOne(model: BookModel,query: BookQueryModel, book: BookModel):
        return model.find_one_and_update(query, {"$set": book},  return_document = ReturnDocument.AFTER)

    @staticmethod
    async def deleteOne(model: BookModel, query: BookQueryModel):
        return model.delete_one(query)

    @staticmethod
    async def deleteMany(model: BookModel, query: BookQueryModel):
        return model.delete_many(query)