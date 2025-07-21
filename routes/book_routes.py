from fastapi import APIRouter
from models.book_models import BookCreate, Book
from controllers import book_controller

router = APIRouter()





# POST crear un libro
@router.post('/', status_code=201)
async def create_book(book: BookCreate):
    return await book_controller.create_book(book)


# GET ALL obtener lista de libro
@router.get('/', status_code=200)
async def get_book_list():
    return await book_controller.get_book_list()



# GET BY ID obter un libro por id 
@router.get('/{book_id}', status_code=200)
async def get_book_by_id(book_id: str):
    return await book_controller.get_book_by_id(book_id)


# PUT BY ID para actualizar libros
@router.put('/{book_id}', status_code=200)
async def update_book(book_id:str, book_data: BookCreate):
    return await book_controller.update_book(book_id, book_data)