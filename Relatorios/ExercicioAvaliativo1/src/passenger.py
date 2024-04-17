from src.base import BaseEntity


class Passenger(BaseEntity):
    def __init__(self, name, document):
        self.name = name
        self.document = document

    def to_dict(self):
        return {
            "name": self.name,
            "document": self.document
        }