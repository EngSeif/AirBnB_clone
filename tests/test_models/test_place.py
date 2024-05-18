#!/usr/bin/python3
"""
    This Module Is To Make
    All Possible Test Cases
    For Place Class In
    Modules Class
"""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    TestPlace

    Contains Test cases for
    the Place class
    in the models module.
    """

    def test_attr_Place(self):
        """
        Test attribute assignments and retrieval.
        """
        P1 = Place()
        self.assertEqual(P1.city_id, "")
        self.assertEqual(P1.user_id, "")
        self.assertEqual(P1.name, "")
        self.assertEqual(P1.description, "")
        self.assertEqual(P1.number_rooms, 0)
        self.assertEqual(P1.number_bathrooms, 0)
        self.assertEqual(P1.max_guest, 0)
        self.assertEqual(P1.price_by_night, 0)
        self.assertEqual(P1.latitude, 0.0)
        self.assertEqual(P1.longitude, 0.0)
        self.assertEqual(P1.amenity_ids, [])
        P1.city_id = "HQ-S2004"
        P1.user_id = "1220325"
        P1.name = "Seif"
        P1.description = "The Best"
        P1.number_rooms = 5
        P1.number_bathrooms = 2
        P1.max_guest = 10
        P1.price_by_night = 10000000
        P1.latitude = 20.14
        P1.longitude = 60.45
        P1.amenity_ids = [124, 654]
        self.assertEqual(P1.city_id, "HQ-S2004")
        self.assertEqual(P1.user_id, "1220325")
        self.assertEqual(P1.name, "Seif")
        self.assertEqual(P1.description, "The Best")
        self.assertEqual(P1.number_rooms, 5)
        self.assertEqual(P1.number_bathrooms, 2)
        self.assertEqual(P1.max_guest, 10)
        self.assertEqual(P1.price_by_night, 10000000)
        self.assertEqual(P1.latitude, 20.14)
        self.assertEqual(P1.longitude, 60.45)
        self.assertEqual(P1.amenity_ids, [124, 654])

    def test_Attr_Unique_Place(self):
        """
        Test If ID is Unique
        """
        P1 = Place()
        P2 = Place()
        self.assertNotEqual(P1.id, P2.id)


if __name__ == '__main__':
    unittest.main()
