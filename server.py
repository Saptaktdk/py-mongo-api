from typing import Union
from fastapi import FastAPI
from api.db import createConnection
from dotenv import load_dotenv
from api.routes import book_router
import os


load_dotenv()
app = FastAPI()

@app.on_event("startup")
def startup_db_connection():
    connection,db = createConnection(
        conn_url=os.getenv("MONGO_CONN_URL"),
        conn_db=os.getenv("MONGO_CONN_DB_NAME")
    )   
    app.connection = connection
    app.db = app.connection[db]
    print("Connected to the book database!")

@app.on_event("shutdown")
def shutdown_db_connection():
    app.connection.close()
    print("Disconnected from the AOT_WIKI database!")

app.include_router(book_router)

