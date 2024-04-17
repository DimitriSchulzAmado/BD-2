from src.base import BaseEntity
from src.run import Run


class Driver(BaseEntity):
    def __init__(self):
        self.runs: list[Run] = []
        self.score = 0

    def to_dict(self) -> dict:
        return {
            "runs": list(
                map(lambda run: run.to_dict(), self.runs)
            ),
            "score": self.score
        }

    def add_run(self, run: Run):
        self.runs.append(run)
        self.score += run.score