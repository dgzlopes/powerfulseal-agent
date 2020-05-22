from abc import ABC, abstractmethod

class AbstractAttack(ABC):
    @abstractmethod
    def run(self):
        pass  # pragma: no cover

    @abstractmethod
    def remove(self):
        pass  # pragma: no cover
