from abc import abstractmethod
from typing import Protocol


class Transaction(Protocol):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def redo(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass
