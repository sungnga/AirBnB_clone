#!/usr/bin/python3
"""
Module for unittests for the FileStorage class
"""
import unittest
import os
import datetime
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models


class TestFileStorageClassCreation(unittest.TestCase):
    """Test class for Storage class instantiation tests"""

    def setUp(self):
        self.file = 'file.json'
        try:
            os.remove(self.file)
        except:
            pass
        self.x = BaseModel()
        self.fs = FileStorage()
        self.storage = models.storage

    def tearDown(self):
        try:
            os.remove(self.file)
        except:
            pass

    def test_inheritance(self):
        self.assertIsInstance(self.fs, FileStorage)

    def test_fs_has_class_attributes(self):
        self.assertIsInstance(self.fs._FileStorage__file_path, str)
        self.assertIsInstance(self.fs._FileStorage__objects, dict)

    def test_all_method(self):
        count = len(self.storage.all())
        self.assertTrue(count != 0)

    def test_new_method(self):
        count = len(self.storage.all())
        y = BaseModel()
        new_count = len(self.storage.all())
        self.assertEqual(count + 1, new_count)
        self.assertEqual(y.__class__.__name__, 'BaseModel')
        self.assertTrue(hasattr(y, 'created_at'))
        self.assertTrue(hasattr(y, 'updated_at'))

    def test_save_method(self):
        self.assertIsInstance(self.storage._FileStorage__objects, dict)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file))
        self.assertTrue(os.stat(self.file).st_size != 0)

    def test_reload_method(self):
        x_id = self.x.id
        x_id_key = "{}.{}".format(self.x.__class__.__name__, self.x.id)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(x_id,
                         self.storage._FileStorage__objects[x_id_key].id)

    def test_str_method(self):
        string = "[{}] ({}) {}".format(self.x.__class__.__name__,
                                       self.x.id,
                                       self.x.__dict__)
        self.assertEqual(string, str(self.x))
