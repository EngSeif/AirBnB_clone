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
    def Test_Initalization(self):
        """
        Test attribute assignments and retrieval.
        """
        U1 = User(
            email="WooaH@Gmail.com",
            password="HQBTQ-1547",
            first_name="Seif",
            last_name="Bellingham"
            )
        self.assertTrue(U1.email, "WooaH@Gmail.com")
        self.assertTrue(U1.password, "HQBTQ-1547")
        self.assertTrue(U1.first_name, "Seif")
        self.assertTrue(U1.last_name, "Bellingham")

        self.assertIsInstance(U1.id, str)
        self.assertIsInstance(U1.created_at, datetime.datetime)
        self.assertIsInstance(U1.updated_at, datetime.datetime)

    def Test_Unique_User(self):
        """
        Test If ID is Unique
        """
        U1 = User()
        U2 = User()
        self.assertNotEqual(U1.id, U2.id)

    def Test_Dict_Method(self):
        """
        Test To_Dict Method
        """
        U1 = User(
            email="WooaH@Gmail.com",
            password="HQBTQ-1547",
            first_name="Seif",
            last_name="Bellingham"
            )

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
