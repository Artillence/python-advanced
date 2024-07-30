import unittest
from banking_system.transaction import Transaction
from banking_system.account import Account

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.account = Account("123", 1000)

    def test_execute_deposit(self):
        transaction = Transaction(self.account, 500, 'deposit')
        transaction.execute()
        self.assertEqual(self.account.get_balance(), 1500)

    def test_execute_withdraw(self):
        transaction = Transaction(self.account, 300, 'withdraw')
        transaction.execute()
        self.assertEqual(self.account.get_balance(), 700)

    def test_execute_invalid_transaction_type(self):
        transaction = Transaction(self.account, 500, 'invalid_type')
        with self.assertRaises(ValueError):
            transaction.execute()

if __name__ == '__main__':
    unittest.main()
