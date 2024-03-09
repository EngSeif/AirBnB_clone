#!/usr/bin/python3
"""
    This Module Is To Make
    All Possible Test Cases
    For Review Class In
    Modules Class
"""


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    TestReview

    Contains Test cases for
    the Place class
    in the models module.
    """

    def test_attr_Review(self):
        """
        Test attribute assignments and retrieval.
        """
        R = Review()
        self.assertEqual(R.place_id, "")
        self.assertEqual(R.user_id, "")
        self.assertEqual(R.text, "")
        R.place_id = "HQ-HyperActive-124"
        R.user_id = "TheBest-1220325"
        R.text = "Seif Is The Best"
        self.assertEqual(R.place_id, "HQ-HyperActive-124")
        self.assertEqual(R.user_id, "TheBest-1220325")
        self.assertEqual(R.text, "Seif Is The Best")

    def test_Attr_Unique_Review(self):
        """
        Test If ID is Unique
        """
        R1 = Review()
        R2 = Review()
        self.assertNotEqual(R1.id, R2.id)


if __name__ == '__main__':
    unittest.main()
