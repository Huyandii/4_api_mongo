from fastapi import HTTPException # Como vamos a contarnos con base de datos: importamos la conexion => la coleccion 
from models.book_models import Book, BookCreate
from db.mongo import book_collection

# Crear una funcion que nos permita convertir el tipo mongo (objeto) en una class Books de python, Vamos a crear una funcion llamada book_helper que transforma los datos de python a Mongo, Nuestra propia funcion de parseo
def book_helper(book: dict) -> Book:
    return Book(

        id=str(book['_id']),
        title=book['title'],
        author=book['author'],
        year=book['year'],
        pages=book.get('pages')

    )


# controlar post para crear un libro en mongo
async def create_book(book: BookCreate):
    try:

        new_book = book.model_dump()#convierte el libro en un diccionario
        result = await book_collection.insert_one(new_book)

        book_created = await book_collection.find_one({'_id': result.inserted_id})
        return book_helper(book_created)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error{str(e)}')

# Controlador para la lista de libros

async def get_book_list():
    try:

        books = []
        result = book_collection.find({})

        async for item in result: 
            books.append(book_helper(item))
        return books
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error {str(e)}')