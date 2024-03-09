#!/usr/bin/python3
"""
    This Module Is To Make
    All Possible Test Cases
    For City Class In
    Modules Class
"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    TestCity

    Contains Test cases for
    the City class
    in the models module.
    """

    def test_attr_city(self):
        """
        Test attribute assignments and retrieval.
        """
        C1 = City()
        self.assertEqual(C1.state_id, "")
        self.assertEqual(C1.name, "")
        C1.state_id = "HQ-1234"
        C1.name = "Madrid"
        self.assertEqual(C1.state_id, "HQ-1234")
        self.assertEqual(C1.name, "Madrid")

    def test_Attr_Unique_City(self):
        """
        Test If ID is Unique
        """
        C1 = City()
        C2 = City()
        self.assertNotEqual(C1.id, C2.id)


if __name__ == '__main__':
    unittest.main()
