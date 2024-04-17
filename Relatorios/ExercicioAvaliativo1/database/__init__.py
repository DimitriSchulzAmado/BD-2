import pymongo
import pymongo.database

from pymongo.server_api import ServerApi


class Database:
    def __init__(self, url_connection: str, database_name: str):
        self.url_connection = url_connection
        self.connection = None
        self.database_name = database_name
        self.current_collection = None

    def connect(self) -> pymongo.database.Database:
        print("Conectando ao banco de dados no MongoDB Atlas")
        con = pymongo.MongoClient(
            self.url_connection,
            server_api=ServerApi('1')
        )

        tries = 1
        while True:
            try:
                print("Tentativa de conexão: {}".format(tries))
                con.admin.command("ping")

                print("Conectado com sucesso! Números dde tentativas: {}".format(tries))
                break
            except Exception as e:
                print(e)
                tries += 1

        self.connection = con[self.database_name]
        return con[self.database_name]

    def load_collection(self, collection_name: str) -> pymongo.collection.Collection:
        collection = self.connection[collection_name]
        self.current_collection = collection

        return collection