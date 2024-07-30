import unittest
from unittest.mock import patch
from banking_system.bank import Bank

class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.bank.create_account("123", 1000)

    def test_create_account(self):
        self.bank.create_account("456", 2000)
        self.assertIsNotNone(self.bank.get_account("456"))

    def test_create_account_existing(self):
        with self.assertRaises(ValueError):
            self.bank.create_account("123", 500)

    def test_process_transaction(self):
        self.bank.process_transaction("123", 500, "deposit")
        self.assertEqual(self.bank.get_account("123").get_balance(), 1500)

    def test_process_invalid_transaction(self):
        with self.assertRaises(ValueError):
            self.bank.process_transaction("123", 500, "invalid_type")

if __name__ == '__main__':
    unittest.main()
