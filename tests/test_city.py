#!/usr/bin/python3
"""
Module for unittests for the City class
"""
import unittest
import os
import json
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestStateClassCreation(unittest.TestCase):
    """Test class for City class instantiation tests"""

    def setUp(self):
        self.x = City()
        self.x.state_id = "state.id"
        self.x.name = "Chicago"
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
        self.assertIsInstance(self.x.state_id, str)
        self.assertIsInstance(self.x.name, str)

    def test_attr_values(self):
        self.assertEqual(self.x.state_id, "state.id")
        self.assertEqual(self.x.name, "Chicago")

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
