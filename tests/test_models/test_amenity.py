#!/usr/bin/python3
"""
    This Module Is To Make
    All Possible Test Cases
    For Amenity Class In
    Modules Class
"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    TestAmenity Class:

    Contains Test cases for
    the Amenity class
    in the models module.
    """

    def test_attr_Amenity(self):
        """
        Test attribute assignments and retrieval.
        """
        A1 = Amenity()
        self.assertEqual(A1.name, "")
        A1.name = "Comfort"
        self.assertEqual(A1.name, "Comfort")

    def test_Attr_Unique_Amenity(self):
        """
        Test If ID is Unique
        """
        A1 = Amenity()
        A2 = Amenity()
        self.assertNotEqual(A1.id, A2.id)


if __name__ == '__main__':
    unittest.main()
