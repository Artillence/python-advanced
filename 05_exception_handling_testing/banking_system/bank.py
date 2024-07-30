from .account import Account
from .transaction import Transaction

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, initial_balance=0):
        if account_id in self.accounts:
            raise ValueError("Account already exists")
        self.accounts[account_id] = Account(account_id, initial_balance)

    def get_account(self, account_id):
        return self.accounts.get(account_id)

    def process_transaction(self, account_id, amount, transaction_type):
        account = self.get_account(account_id)
        if not account:
            raise ValueError("Account not found")
        transaction = Transaction(account, amount, transaction_type)
        transaction.execute()
