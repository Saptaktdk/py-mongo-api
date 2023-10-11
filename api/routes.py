from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from api.models import BookModel,ResponseBody, ResponseError, ResponseSuccessMany, ResponseSuccessOne
from api.query import BookQuery
from bson import ObjectId


BOOK_MODEL = "book"

book_router = APIRouter(
    prefix='/api/books'
)

@book_router.get('/all')
async def getAllBooks(request: Request):
    bookModel: BookModel = request.app.db["book"]
    bookList = await BookQuery.getMany(bookModel, {})
    print("bookList: ", bookList)

    if(len(bookList) == 0):
        return ResponseError(
            status = 404,
            error = "No books found"
        )
         
    return ResponseSuccessMany(
        status = 200,
        message = "{} books found".format(len(bookList)),
        data = bookList 
    )

@book_router.get('/{id}')
async def getCharacterById( id: str,request: Request):
    bookModel: BookModel = request.app.db["book"]
    book = await BookQuery.getOne(bookModel, {"_id": ObjectId(id)})

    if(book is None):
        return ResponseError(
            status = 404,
            error = "No book found for id: {}".format(id)
        )
         
        
    return ResponseSuccessOne (
        status = 200,
        message = "Book found with id {}".format(id),
        data = book
    )

@book_router.post('/add')
async def addCharacter(request: Request, book: BookModel = Body(...)):
    bookModel: BookModel = request.app.db["book"]
    bookToBeAdded  = jsonable_encoder(book)
    addedBookResponse = await BookQuery.addOne(bookModel, bookToBeAdded)
    print(addedBookResponse)
    addedCharacterId = str(addedBookResponse.inserted_id)

   
    if(addedCharacterId == None):
        return ResponseError (
            status = 500,
            error = "Something went wrong while adding"

        )
    elif(addedCharacterId):
        return ResponseSuccessOne (
            status = 201,
            message = "Character added successfully",
            data = book.model_dump()
        )
    
@book_router.put('/update/{id}')
async def updateBook(id:str,request: Request, book: BookModel = Body(...)):
    bookModel: BookModel = request.app.db["book"]
    bookToBeUpdated  = jsonable_encoder(book)

    updatedBookResponse = await BookQuery.updateOne(bookModel, {"_id": ObjectId(id)}, bookToBeUpdated)

    if(updatedBookResponse is None):
        return ResponseError (
            status = 404,
            error = "Book with the given id not found"
    )


    return ResponseSuccessOne(
        status = 201,
        message = "Book updated successfully",
        data = book.model_dump()
    )

@book_router.delete('/delete/{id}')
async def deleteBook(id:str,request: Request):
    bookModel: BookModel = request.app.db["book"]
    deletedBookResponse = await BookQuery.deleteOne(bookModel, {"_id": ObjectId(id)})

    if(deletedBookResponse.deleted_count == 0):
        return ResponseError (
            status = 500,
            error = "Something went wrong while deleting"
        )

    elif (deletedBookResponse.deleted_count == 1):
        return ResponseSuccessOne (
            status = 200,
            message = "Book deleted successfully",
            data = {}
        )