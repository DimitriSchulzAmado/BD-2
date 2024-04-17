import pymongo

from src.driver import Driver
from bson.objectid import ObjectId

from src.passenger import Passenger
from src.run import Run


class DriverModel:
    def __init__(self, collection: pymongo.collection.Collection):
        self._collection = collection

    def create(self, driver: Driver):
        driver_to_save = driver.to_dict()

        self._collection.insert_one(driver_to_save)
        print("Motorista Cadastrado!")

    def find_one(self, driver_id: str) -> Driver | None:
        driver_from_db = self._collection.find_one({
            "_id": ObjectId(driver_id)
        })

        if not driver_from_db:
            print("Motorista não encontrado!")
            return

        _driver = Driver()
        _driver.score = driver_from_db["score"]
        for run in driver_from_db["runs"]:
            _run = Run()
            _run.value = run["value"]
            _run.distance = run["distance"]
            _run.score = run["score"]

            if len(run["passengers"]) > 0:
                for passenger in run["passengers"]:
                    passenger = Passenger(
                        passenger["name"],
                        passenger["document"]
                    )

                    _run.passengers.append(passenger)
            _driver.runs.append(_run)

        return driver_from_db

    def update(self, driver_id: str, driver: Driver):
        self._collection.update_one({
            "_id": driver_id
        }, driver.to_dict())

        print("Motorista atualizado com sucesso!")

    def delete(self, driver_id: str):
        self._collection.delete_one({
            "_id": ObjectId(driver_id)
        })

        print("Motorista deletado com sucesso!")
        