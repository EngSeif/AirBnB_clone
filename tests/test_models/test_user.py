#!/usr/bin/python3
"""
    This Module Is To Make
    All Possible Test Cases
    For User Class In
    Modules Class
"""

import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """
    Test cases for
    the User class
    in the models module.
    """
    def test_Initalization_User(self):
        """
        Test attribute assignments and retrieval.
        """
        U1 = User()
        self.assertEqual(U1.email, "")
        self.assertEqual(U1.password, "")
        self.assertEqual(U1.first_name, "")
        self.assertEqual(U1.last_name, "")
        U1.email = "WooaH@Gmail.com",
        U1.password = "HQBTQ-1547",
        U1.first_name = "Seif",
        U1.last_name = "Bellingham"
        self.assertTrue(U1.email, "WooaH@Gmail.com")
        self.assertTrue(U1.password, "HQBTQ-1547")
        self.assertTrue(U1.first_name, "Seif")
        self.assertTrue(U1.last_name, "Bellingham")

        self.assertIsInstance(U1.id, str)
        self.assertIsInstance(U1.created_at, datetime.datetime)
        self.assertIsInstance(U1.updated_at, datetime.datetime)

    def test_Unique_User(self):
        """
        Test If ID is Unique
        """
        U1 = User()
        U2 = User()
        self.assertNotEqual(U1.id, U2.id)

    def test_Dict_Method_User(self):
        """
        Test To_Dict Method
        """
        U1 = User()
        U1.email = "WooaH@Gmail.com",
        U1.password = "HQBTQ-1547",
        U1.first_name = "Seif",
        U1.last_name = "Bellingham"

        Dict_U = U1.to_dict()
        self.assertIn('id', Dict_U)
        self.assertIn('created_at', Dict_U)
        self.assertIn('updated_at', Dict_U)
        self.assertIn('email', Dict_U)
        self.assertIn('password', Dict_U)
        self.assertIn('first_name', Dict_U)
        self.assertIn('last_name', Dict_U)

        self.assertTrue(U1.id, Dict_U['id'])
        self.assertTrue(U1.updated_at, Dict_U['created_at'])
        self.assertTrue(U1.created_at, Dict_U['updated_at'])
        self.assertTrue(U1.email, Dict_U['email'])
        self.assertTrue(U1.password, Dict_U['password'])
        self.assertTrue(U1.first_name, Dict_U['first_name'])
        self.assertTrue(U1.last_name, Dict_U['last_name'])


if __name__ == '__main__':
    unittest.main()
