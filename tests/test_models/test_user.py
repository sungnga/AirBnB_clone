#!/usr/bin/python3
"""
Module for unittests for the User class
"""
import unittest
import os
import json
import datetime
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestUserCreation(unittest.TestCase):
    """Test class for User class instantiation tests"""

    def setUp(self):
        self.x = User()
        self.x.first_name = "Betty"
        self.x.last_name = "Holberton"
        self.x.email = "airbnb@holbertonshool.com"
        self.x.password = "root"
        self.x.save()
        self.fp = open('file.json', 'r', encoding="utf-8")
        self.dict_ = json.load(self.fp)

    def tearDown(self):
        try:
            self.fp.close()
        except:
            pass

    def test_user_creation(self):
        self.assertIsInstance(self.x, BaseModel)
        self.assertIsInstance(self.x, User)

    def test_attr_type(self):
        self.assertIsInstance(self.x.email, str)
        self.assertIsInstance(self.x.password, str)
        self.assertIsInstance(self.x.first_name, str)
        self.assertIsInstance(self.x.last_name, str)
        self.assertIsInstance(self.x.updated_at, datetime.datetime)
        self.assertIsInstance(self.x.created_at, datetime.datetime)
        self.assertIsInstance(self.x.id, str)

    def test_kwargs(self):
        a = User(password="psswd")
        self.assertEqual(a.password, "psswd")

    def test_attr_values(self):
        self.assertEqual(self.x.email,
                         "airbnb@holbertonshool.com")
        self.assertEqual(self.x.password, "root")
        self.assertEqual(self.x.first_name, "Betty")
        self.assertEqual(self.x.last_name, "Holberton")

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
