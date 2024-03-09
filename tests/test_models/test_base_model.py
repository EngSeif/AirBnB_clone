#!/usr/bin/python3
"""
    This Module Is To Make
    All Possible Test Cases
    For Amenity Class In
    Modules Class
"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for
    the Amenity class
    in the models module.
    """

    def test_attributes(self):
        """
        Test attribute assignments and retrieval.
        """
        B1 = BaseModel()
        B2 = BaseModel()
        self.assertNotEqual(B1.id, B2.id)

if __name__ == '__main__':
    unittest.main()
