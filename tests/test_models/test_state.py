#!/usr/bin/python3
"""
    This Module Is To Make
    All Possible Test Cases
    For State Class In
    Modules Class
"""


import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for
    the State class
    in the models module.
    """

    def test_attr_State(self):
        """
        Test attribute assignments and retrieval.
        """
        S1 = State()
        self.assertEqual(S1.name, "")
        S1.name = "Berlin"
        self.assertEqual(S1.name, "Berlin")

    def test_Attr_Unique_State(self):
        """
        Test If ID is Unique
        """
        S1 = State()
        S2 = State()
        self.assertNotEqual(S1.id, S2.id)


if __name__ == '__main__':
    unittest.main()
