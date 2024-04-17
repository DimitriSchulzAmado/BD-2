from abc import abstractmethod, ABC


class BaseEntity(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError()