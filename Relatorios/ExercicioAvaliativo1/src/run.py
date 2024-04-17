from src.base import BaseEntity
from src.passenger import Passenger


class Run(BaseEntity):
    def __init__(self):
        self.score = 0
        self.distance = 0
        self.value = 0.0
        self.passengers: list[Passenger] = []

    def to_dict(self) -> dict:
        return {
            'score': self.score,
            'distance': self.distance,
            'value': self.value,
            'passengers': list(
                map(lambda passenger: passenger.to_dict(), self.passengers)
            ),
        }