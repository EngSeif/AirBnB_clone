#!/usr/bin/python3
"""
    This Module Is To Make
    All Possible Test Cases
    For FileStorage Class In
    Engine Package
"""


import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """
    Test_FileStorage Class:

    Contains Test cases for
    the FileStorgae class
    in the Engine module.
    """

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_All_and_New(self):
        """
        Test All And New Methods
        """
        B = BaseModel()
        self.storage.new(B)
        St_Obj = self.storage.all()
        self.assertIn('BaseModel.' + B.id, St_Obj)

    def test_save_reload(self):
        """
        Test Save And Reload Methods
        """
        B1 = BaseModel()
        B2 = BaseModel()
        self.storage.new(B1)
        self.storage.new(B2)
        self.storage.save()
        self.storage = FileStorage()
        self.storage.reload()
        St_Obj = self.storage.all()
        self.assertIn('BaseModel.' + B1.id, St_Obj)
        self.assertIn('BaseModel.' + B2.id, St_Obj)

    def test_with_an_existing_file(self):
        """
        Test Reload With An Existing File
        """
        B = BaseModel()
        self.storage.new(B)
        self.storage.save()
        self.storage.reload()
        St_Obj = self.storage.all()
        self.assertIn('BaseModel.' + B.id, St_Obj)

    def test_with_an_existing_file(self):
        """
        Test Reload WithOut An Existing File
        """
        self.storage.reload()
        St_Obj = self.storage.all()
        self.assertTrue(len(St_Obj) > 0)

    def test_save_to_read_only(self):
        """
        Test Save WithIn To ReadOnly Path
        """
        file_path = '/usr/bin/file.json'
        storage = FileStorage()
        storage._FileStorage__file_path = file_path
        B = BaseModel()
        storage.new(B)
        with self.assertRaises(PermissionError):
            storage.save()


if __name__ == '__main__':
    unittest.main()
