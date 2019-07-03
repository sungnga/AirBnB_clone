#!/usr/bin/python3
"""
Module for unittests for the Place class
"""
import unittest
import os
import json
import datetime
import models
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestPlaceCreation(unittest.TestCase):
    """Test class for instantiating amenity"""

    def setUp(self):
        self.file = 'file.json'
        try:
            os.remove(self.file)
        except:
            pass
        self.x = Place()
        self.validAttributes = {
            'city_id': str,
            'user_id': str,
            'name': str,
            'description': str,
            'number_rooms': int,
            'max_guest': int,
            'price_by_night': int,
            'latitude': float,
            'longitude': float,
            'amenity_ids': list,
            }
        self.storage = models.storage

    def tearDown(self):
        try:
            os.remove(self.file)
        except:
            pass

    def createPlace(self):
        self.ex = Place()
        self.ex.city_id = "23asdk"
        self.ex.user_id = "asdfoie"
        self.ex.name = "John"
        self.ex.description = "Nice"
        self.ex.number_rooms = 32
        self.ex.number_bathrooms = 3
        self.ex.max_guest = 4
        self.ex.price_by_night = 199
        self.ex.latitude = 13.2323
        self.ex.longitude = 165.2323
        self.ex.amenity_ids = ['amenity1',
                               'amenity2',
                               'amenity3']

    def test_place_has_correct_class_name(self):
        self.assertEqual('Place', self.x.__class__.__name__)

    def test_empty_place_has_attrs(self):
        for k in self.validAttributes:
            self.assertTrue(hasattr(self.x, k))

    def test_empty_place_attrs_type(self):
        for k, v in self.validAttributes.items():
            test_type = type(getattr(self.x, k))
            self.assertEqual(test_type, v)

    def test_place_added_attrs(self):
        self.createPlace()
        self.assertEqual(self.ex.city_id, "23asdk")
        self.assertEqual(self.ex.user_id, "asdfoie")
        self.assertEqual(self.ex.name, "John")
        self.assertEqual(self.ex.description, "Nice")
        self.assertEqual(self.ex.number_rooms, 32)
        self.assertEqual(self.ex.number_bathrooms, 3)
        self.assertEqual(self.ex.max_guest, 4)

        # self.assertEqual(
        # for k, v in self.validAttributes.items():
        #     test_attr = getattr(self.ex, k)
        #     self.assertEqual(test_attr, v)

    def test_check_custom_attrs(self):
        self.x.custom_attr = "Nga"
        self.assertEqual(self.x.custom_attr, "Nga")
        self.assertIsInstance(self.x.custom_attr, str)

    # #TODO: This fails occasionally
    def test_save_time_change(self):
        old_time = self.x.updated_at
        self.x.save()
        self.assertNotEqual(self.x.updated_at, old_time)

    def test_new_place_dict(self):
        self.createPlace()
        dict_ = self.ex.to_dict()
        self.y = Place(**dict_)
        self.assertEqual(self.ex.name, self.y.name)

    def test_new_place_dict_attr_types(self):
        self.createPlace()
        dict_ = self.ex.to_dict()
        self.y = Place(**dict_)
        for k, v in self.validAttributes.items():
            test_type = type(getattr(self.y, k))
            self.assertEqual(test_type, v)

    def test_save_place(self):
        self.assertIsInstance(self.storage._FileStorage__objects, dict)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file))
        self.assertTrue(os.stat(self.file).st_size != 0)

    def test_reload_place(self):
        x_id = self.x.id
        x_id_key = "{}.{}".format(self.x.__class__.__name__, self.x.id)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(x_id,
                         self.storage._FileStorage__objects[x_id_key].id)

# class TestPlaceClassCreation(unittest.TestCase):
#     """Test class for Place class instantiation tests"""
#     def setUp(self):
#         """Set"""
#         self.x = BaseModel()

#     def test_state_creation(self):
#         self.assertIsInstance(self.x, BaseModel)


# class TestPlaceModelObjectCreation(unittest.TestCase):
#     """Test class for Place Model instantiation with kwargs."""
#     def setUp(self):
#         self.x = Place()
#         self.x.city_id = "City.id"
#         self.x.user_id = "User.id"
#         self.x.name = "Four Season"
#         self.x.description = "Luxury Hotel"
#         self.x.number_rooms = 2
#         self.x.number_bathrooms = 1
#         self.x.max_guest = 6
#         self.x.price_by_night = 200
#         self.x.latitude = 111.11
#         self.x.longitude = 222.22
#         self.x.amenity_ids = ['amenity.id1', 'amenity.id2', 'amenity.id3']
#         self.x.save()
#         self.fp = open('file.json', 'r', encoding="utf-8")
#         self.dict_ = json.load(self.fp)

#     def tearDown(self):
#         try:
#             self.fp.close()
#         except:
#             pass

#     def test_attr_type(self):
#         self.assertIsInstance(self.x.city_id, str)
#         self.assertIsInstance(self.x.user_id, str)
#         self.assertIsInstance(self.x.name, str)
#         self.assertIsInstance(self.x.description, str)
#         self.assertIsInstance(self.x.number_rooms, int)
#         self.assertIsInstance(self.x.number_bathrooms, int)
#         self.assertIsInstance(self.x.max_guest, int)
#         self.assertIsInstance(self.x.price_by_night, int)
#         self.assertIsInstance(self.x.latitude, float)
#         self.assertIsInstance(self.x.longitude, float)
#         self.assertIsInstance(self.x.amenity_ids, list)

#     def test_attr_values(self):
#         self.assertEqual(self.x.city_id, "City.id")
#         self.assertEqual(self.x.user_id, "User.id")
#         self.assertEqual(self.x.name, "Four Season")
#         self.assertEqual(self.x.description, "Luxury Hotel")
#         self.assertEqual(self.x.number_rooms, 2)
#         self.assertEqual(self.x.number_bathrooms, 1)
#         self.assertEqual(self.x.max_guest, 6)
#         self.assertEqual(self.x.price_by_night, 200)
#         self.assertEqual(self.x.latitude, 111.11)
#         self.assertEqual(self.x.longitude, 222.22)
#         self.assertEqual(self.x.amenity_ids,
#                          ['amenity.id1', 'amenity.id2', 'amenity.id3'])

#     def test_attr_is_saved(self):
#         old_updated_at = self.x.updated_at
#         self.x.save()
#         self.assertNotEqual(old_updated_at, self.x.updated_at)

#     def test_instance_is_in_storage(self):
#         key = "{}.{}".format(self.x.__class__.__name__, self.x.id)
#         self.assertTrue(key in self.dict_)

#     def test_str_method(self):
#         string = "[{}] ({}) {}".format(self.x.__class__.__name__,
#                                        self.x.id,
#                                        self.x.__dict__)
#         self.assertEqual(string, str(self.x))
