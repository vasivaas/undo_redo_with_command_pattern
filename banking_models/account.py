from dataclasses import dataclass
from typing import ClassVar, Union


@dataclass
class Account:
    name: str
    number: str
    number_length: ClassVar[int] = 15
    balance: float = 0.

    def deposit(self, amount: Union[int, float]) -> None:
        if amount < 1:
            raise ValueError('You can deposit only positive amount')
        self.balance += amount

    def withdraw(self, amount: Union[int, float]) -> None:
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount
