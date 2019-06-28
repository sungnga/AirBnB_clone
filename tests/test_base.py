#!/usr/bin/python3
"""
Module for unittests for the BaseModel class
"""
import unittest
import os
import datetime
from  models.base_model import BaseModel

class TestBaseModelClassCreation(unittest.TestCase):
    """Test class for Base class instantiation tests"""

    def setUp(self):
        self.x = BaseModel()

    def test_id_creation(self):
        self.assertIsNotNone(self.x.id)
        self.assertEqual(36, len(self.x.id))
        self.assertIsInstance(self.x.id, str)
        self.assertFalse(" " in self.x.id)

    def test_created_at(self):
        self.assertIsNotNone(self.x.created_at)
        self.assertIsInstance(self.x.created_at, datetime.datetime)

    def test_updated_at(self):
        self.assertIsNotNone(self.x.updated_at)
        self.assertIsInstance(self.x.updated_at, datetime.datetime)

    def test_updated_created_sametime(self):
        self.assertEqual(self.x.updated_at, self.x.created_at)

    def test_save_method(self):
        old_time = self.x.updated_at
        self.x.save()
        self.assertNotEqual(old_time, self.x.updated_at)
        self.assertIsInstance(self.x.updated_at, datetime.datetime)

    def test_to_dict_method(self):
        dict_ = self.x.to_dict()
        self.assertIsInstance(dict_, dict)
        self.assertIsInstance(dict_['updated_at'], str)
        self.assertIsInstance(dict_['created_at'], str)
        self.assertEqual(dict_['__class__'],
                                 self.x.__class__.__name__)
