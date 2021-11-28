from dataclasses import dataclass, field
from typing import List

from banking_commands.transaction import Transaction


@dataclass
class BankController:
    repeat_stack: List[Transaction] = field(default_factory=list)
    cancel_stack: List[Transaction] = field(default_factory=list)

    def execute(self, transaction: Transaction) -> None:
        transaction.execute()
        self.repeat_stack.clear()
        self.cancel_stack.append(transaction)

    def redo(self) -> None:
        if not self.repeat_stack:
            return None

        last_transaction = self.repeat_stack.pop()
        last_transaction.redo()
        self.cancel_stack.append(last_transaction)

    def undo(self) -> None:
        if not self.cancel_stack:
            return None

        last_transaction = self.cancel_stack.pop()
        last_transaction.undo()
        self.repeat_stack.append(last_transaction)
