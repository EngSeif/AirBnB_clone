#!/usr/bin/python3
"""
    This Module Is To Make
    All Possible Test Cases
    For BaseModel Class In
    Modules Class
"""


import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel Class:

    Contains Test cases for
    the Base class
    in the models module.
    """

    def test_Has_atr(self):
        """
        Test If BaseModel Has Expected
        Attributes And Their True Types
        """
        B = BaseModel()
        self.assertTrue(hasattr(B, 'id'))
        self.assertTrue(hasattr(B, 'created_at'))
        self.assertTrue(hasattr(B, 'updated_at'))
        self.assertIsInstance(B.id, str)
        self.assertIsInstance(B.created_at, datetime.datetime)
        self.assertIsInstance(B.updated_at, datetime.datetime)

    def test_Base_Uniquness(self):
        """
        Test Uniquness Of BaseModel
        """
        B1 = BaseModel()
        B2 = BaseModel()
        self.assertNotEqual(B1.id, B2.id)

    def test_Created_At(self):
        """
        See If Creation Time Is Assigned True
        """
        B = BaseModel()
        self.assertAlmostEqual(B.created_at, datetime.datetime.now(),
                               delta=datetime.timedelta(seconds=1))

    def test_Base_str(self):
        """
        Test String Representation
        """
        B1 = BaseModel()
        At1 = B1.__class__.__name__
        At2 = B1.id
        At3 = B1.__dict__
        self.assertIsInstance(str(B1), str)
        self.assertEqual(str(B1), f"[{At1}] ({At2}) {At3}")

    def test_Dict_Method(self):
        """
        Test Dictionary Representation
        Returned Bt To_Dict() Method
        """
        B = BaseModel()
        B_Dict = B.to_dict()
        self.assertIsInstance(B_Dict, dict)
        self.assertEqual(B_Dict['__class__'], 'BaseModel')
        self.assertIsInstance(B_Dict['created_at'], str)
        self.assertIsInstance(B_Dict['updated_at'], str)
        self.assertEqual(B_Dict['created_at'], B.created_at.isoformat())
        self.assertEqual(B_Dict['updated_at'], B.updated_at.isoformat())

    def test_SaveMethod(self):
        """
        Test If Save Method
        Saves The Update Time
        Or Not
        """
        B = BaseModel()
        Original_Upd = B.updated_at
        B.save()
        self.assertNotEqual(B.updated_at, Original_Upd)

    def test_Init_WithArgs(self):
        """
        Test Initialization
        With Arguments
        """
        id_N = "12345"
        created_N = datetime.datetime(2004, 4, 29)
        updated_N = datetime.datetime(2023, 9, 25)
        created_N_adjusted = (datetime.datetime(2004, 4, 29)
                              .isoformat(timespec='microseconds'))
        updated_N_adjusted = (datetime.datetime(2023, 9, 25)
                              .isoformat(timespec='microseconds'))
        B = (BaseModel(id=id_N,
                       created_at=created_N_adjusted,
                       updated_at=updated_N_adjusted))
        self.assertEqual(B.id, id_N)
        self.assertEqual(B.created_at, created_N)
        self.assertEqual(B.updated_at, updated_N)


if __name__ == '__main__':
    unittest.main()
