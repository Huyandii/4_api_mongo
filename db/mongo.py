import motor.motor_asyncio
import os
from dotenv import load_dotenv

# Cargamos la variable de entorno

load_dotenv()

MONGO_URL= os.getenv('MONGO_URL')
MONGO_DB_NAME=os.getenv('MONGO_DB_NAME')

# Cagamos el cliente mongoDB asincrono.
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client['MONGO_DB_NAME']


# Cargar la coleccion de libros BBDD books
book_collection = db['books']