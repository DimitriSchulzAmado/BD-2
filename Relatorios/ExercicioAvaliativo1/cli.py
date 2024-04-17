import os

from random import randint, randrange

import typer

from src.driver import Driver
from src.passenger import Passenger
from src.run import Run
from database import Database
from database.models import DriverModel

from dotenv import load_dotenv


load_dotenv()


class DriverCLI:
    def __init__(self, driver_model: DriverModel) -> None:
        self.model = driver_model

    def create(self):
        driver = Driver()

        while True:
            run = Run()
            run.score = randint(1, 10)
            run.value = randrange(1, 100)
            run.distance = randrange(1, 1000)

            while True:
                passenger_name = input("Nome do passageiro: ")
                passenger_document = input("Documento do passageiro: ")

                passenger = Passenger(passenger_name, passenger_document)

                run.passengers.append(passenger)

                option = input("Deseja adicionar mais um passageiro? [S/N] ").upper()
                match option:
                    case "S":
                        pass
                    case _:
                        break
            driver.add_run(run)
            option = input("Deseja adicionar mais uma corrida? [S/N] ").upper()
            match option:
                case "S":
                    pass
                case _:
                    break
        self.model.create(driver)

    def find_by_id(self):
        driver_id = input("Digite o id do motorista: ")
        driver = self.model.find_one(driver_id)

        print("Motorista: {}".format(driver))

    def delete(self):
        driver_id = input("Digite o id do motorista: ")
        self.model.delete(driver_id)

    def update(self):
        driver_id = input("Digite o id do motorista: ")
        driver = self.model.find_one(driver_id)

        if driver is None:
            return

        option = input("Deseja adicionar uma corrida? [S/N] ").upper()
        match option:
            case "S":
                while True:
                    run = Run()
                    run.score = randint(1, 10)
                    run.value = randrange(1, 100)
                    run.distance = randrange(1, 1000)

                    while True:
                        passenger_name = input("Nome do passageiro: ")
                        passenger_document = input("Documento do passageiro: ")

                        passenger = Passenger(
                            passenger_name,
                            passenger_document
                        )

                        run.passengers.append(passenger)

                        option = input("Deseja adicionar mais um passageiro? [S/N] ").upper()
                        match option:
                            case "S":
                                pass
                            case _:
                                break
                    driver.add_run(run)
                    option = input("Deseja adicionar mais uma corrida? [S/N] ").upper()
                    match option:
                        case "S":
                            pass
                        case _:
                            break
            case _:
                return


class CLI:
    def __init__(self):
        self.database = Database(
            url_connection=os.getenv("CONNECTION_URL"),
            database_name=os.getenv("DATABASE_NAME"),
        )

        self.database.connect()
        self.collection = self.database.load_collection(
            os.getenv("COLLECTION_NAME")
        )

        self.driver = DriverModel(self.collection)
        self.cli = DriverCLI(self.driver)

    def run(self, func_name: str):
        if func_name == "quit":
            print("Até mais!")

        func = getattr(self.cli, func_name)
        func()


if __name__ == '__main__':
    cli = CLI()
    while True:
        print("Comandos disponíveis: ")
        print("1- Create")
        print("2- Find by id")
        print("3- Delete")
        print("4- Update")
        print("5- Quit")
        print()

        command = input("Entre com o comando: ")
        if command == "Quit":
            print("Até mais!")
            break

        callable_func_command = getattr(cli.cli, command)
        if callable_func_command is not None and callable(callable_func_command):
            callable_func_command()
        else:
            print("Comando inválido, insira outro")
        print("=" * 32)