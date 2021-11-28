from dataclasses import dataclass

from banking_models.account import Account


@dataclass
class Deposit:
    account: Account
    amount: float

    @property
    def transaction_info(self) -> str:
        return f"{self.amount:.2f}$ to account {self.account.name}"

    def execute(self) -> None:
        self.account.deposit(self.amount)
        print('Deposited {details}'.format(details=self.transaction_info))

    def redo(self) -> None:
        self.account.deposit(self.amount)
        print('Repeated deposit of {details}'.format(details=self.transaction_info))

    def undo(self) -> None:
        self.account.withdraw(self.amount)
        print('Canceled deposit of {details}'.format(details=self.transaction_info))


@dataclass
class Withdrawal:
    account: Account
    amount: float

    @property
    def transaction_info(self) -> str:
        return f"{self.amount:.2f}$ from account {self.account.name}"

    def execute(self) -> None:
        self.account.withdraw(self.amount)
        print('Withdrawn {details}'.format(details=self.transaction_info))

    def redo(self) -> None:
        self.account.withdraw(self.amount)
        print('Repeated withdraw of {details}'.format(details=self.transaction_info))

    def undo(self) -> None:
        self.account.deposit(self.amount)
        print('Canceled withdraw of {details}'.format(details=self.transaction_info))


@dataclass
class Transfer:
    from_account: Account
    to_account: Account
    amount: float

    @property
    def transaction_info(self) -> str:
        return f"{self.amount:.2f}$ from account {self.from_account.name} to account {self.to_account.name}"

    def execute(self) -> None:
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        print('Transferred {details}'.format(details=self.transaction_info))

    def redo(self) -> None:
        self.from_account.withdraw(self.amount)
        self.to_account.deposit(self.amount)
        print('Repeated transfer of {details}'.format(details=self.transaction_info))

    def undo(self) -> None:
        self.to_account.withdraw(self.amount)
        self.from_account.deposit(self.amount)
        print('Canceled transfer of {details}'.format(details=self.transaction_info))
