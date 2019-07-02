#!/usr/bin/python3
"""
Module for unittests for the Review class
"""
import unittest
import os
import json
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestStateClassCreation(unittest.TestCase):
    """Test class for Review class instantiation tests"""

    def setUp(self):
        self.x = Review()
        self.x.place_id = "Place.id"
        self.x.user_id = "User.id"
        self.x.text = "text"
        self.x.save()
        self.fp = open('file.json', 'r', encoding="utf-8")
        self.dict_ = json.load(self.fp)

    def tearDown(self):
        try:
            self.fp.close()
        except:
            pass

    def test_state_creation(self):
        self.assertIsInstance(self.x, BaseModel)

    def test_attr_type(self):
        self.assertIsInstance(self.x.place_id, str)
        self.assertIsInstance(self.x.user_id, str)
        self.assertIsInstance(self.x.text, str)

    def test_attr_values(self):
        self.assertEqual(self.x.place_id, "Place.id")
        self.assertEqual(self.x.user_id, "User.id")
        self.assertEqual(self.x.text, "text")

    def test_attr_is_saved(self):
        old_updated_at = self.x.updated_at
        self.x.save()
        self.assertNotEqual(old_updated_at, self.x.updated_at)

    def test_instance_is_in_storage(self):
        key = "{}.{}".format(self.x.__class__.__name__, self.x.id)
        self.assertTrue(key in self.dict_)

    def test_str_method(self):
        string = "[{}] ({}) {}".format(self.x.__class__.__name__,
                                       self.x.id,
                                       self.x.__dict__)
        self.assertEqual(string, str(self.x))
