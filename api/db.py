from pymongo import MongoClient


def createConnection(conn_url, conn_db):
    bookClient = MongoClient(conn_url)
    return bookClient, conn_db
