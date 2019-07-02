#!/usr/bin/python3
"""
Module for unittests for the Place class
"""
import unittest
import os
import json
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestPlaceClassCreation(unittest.TestCase):
    """Test class for Place class instantiation tests"""
    def setUp(self):
        """Set"""
        self.x = BaseModel()

    def test_state_creation(self):
        self.assertIsInstance(self.x, BaseModel)


class TestPlaceModelObjectCreation(unittest.TestCase):
    """Test class for Place Model instantiation with kwargs."""
    def setUp(self):
        self.x = Place()
        self.x.city_id = "City.id"
        self.x.user_id = "User.id"
        self.x.name = "Four Season"
        self.x.description = "Luxury Hotel"
        self.x.number_rooms = 2
        self.x.number_bathrooms = 1
        self.x.max_guest = 6
        self.x.price_by_night = 200
        self.x.latitude = 111.11
        self.x.longitude = 222.22
        self.x.amenity_ids = ['amenity.id1', 'amenity.id2', 'amenity.id3']
        self.x.save()
        self.fp = open('file.json', 'r', encoding="utf-8")
        self.dict_ = json.load(self.fp)

    def tearDown(self):
        try:
            self.fp.close()
        except:
            pass

    def test_attr_type(self):
        self.assertIsInstance(self.x.city_id, str)
        self.assertIsInstance(self.x.user_id, str)
        self.assertIsInstance(self.x.name, str)
        self.assertIsInstance(self.x.description, str)
        self.assertIsInstance(self.x.number_rooms, int)
        self.assertIsInstance(self.x.number_bathrooms, int)
        self.assertIsInstance(self.x.max_guest, int)
        self.assertIsInstance(self.x.price_by_night, int)
        self.assertIsInstance(self.x.latitude, float)
        self.assertIsInstance(self.x.longitude, float)
        self.assertIsInstance(self.x.amenity_ids, list)

    def test_attr_values(self):
        self.assertEqual(self.x.city_id, "City.id")
        self.assertEqual(self.x.user_id, "User.id")
        self.assertEqual(self.x.name, "Four Season")
        self.assertEqual(self.x.description, "Luxury Hotel")
        self.assertEqual(self.x.number_rooms, 2)
        self.assertEqual(self.x.number_bathrooms, 1)
        self.assertEqual(self.x.max_guest, 6)
        self.assertEqual(self.x.price_by_night, 200)
        self.assertEqual(self.x.latitude, 111.11)
        self.assertEqual(self.x.longitude, 222.22)
        self.assertEqual(self.x.amenity_ids,
                         ['amenity.id1', 'amenity.id2', 'amenity.id3'])

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
