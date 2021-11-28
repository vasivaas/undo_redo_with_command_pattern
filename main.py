from banking_models.bank import Bank
from banking_commands.commands import Deposit, Withdrawal, Transfer
from controllers.bank_controller import BankController


def main():
    # initialize Bank
    bank = Bank()

    # initialize Bank Controller for undo, redo operations
    bank_controller = BankController()

    # create accounts
    account1 = bank.create_account(account_name='Mike')
    account2 = bank.create_account(account_name='David')
    account3 = bank.create_account(account_name='William')

    # add deposit
    bank_controller.execute(transaction=Deposit(account=account1, amount=3000))
    bank_controller.execute(transaction=Deposit(account=account2, amount=8000.45))
    bank_controller.execute(transaction=Deposit(account=account3, amount=4500.56))
    bank_controller.undo()
    bank_controller.redo()

    # money transfers
    bank_controller.execute(transaction=Transfer(from_account=account2, to_account=account1, amount=2100))
    bank_controller.undo()
    bank_controller.redo()
    bank_controller.execute(transaction=Withdrawal(account=account3, amount=500))
    bank_controller.undo()

    print(bank)


if __name__ == '__main__':
    main()
