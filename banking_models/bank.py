import string
import random
from dataclasses import dataclass, field
from typing import List, Optional

from banking_models.account import Account


@dataclass
class Bank:
    accounts: List[Account] = field(default_factory=list)

    def create_account(self, account_name: str) -> Account:
        account_number = self._generate_account_number()
        account = Account(account_name, account_number)
        self.accounts.append(account)
        return account

    def get_account(self, account_number: str) -> Optional[Account]:
        for account in self.accounts:
            if account.number == account_number:
                return account
        raise ValueError('Account not found')

    def _generate_account_number(self):
        return ''.join(random.choices(string.digits, k=Account.number_length))
