#!/usr/bin/python3
"""
This module contains the FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


validClasses = {'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review}


class FileStorage():
    """Class used for file storage actions"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return(self.__objects)

    def new(self, obj):
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        with open(self.__file_path, 'w', encoding="utf-8") as fp:
            jdict_ = {}
            for k, v in self.__objects.items():
                dict_ = self.__objects[k].to_dict()
                jdict_[k] = dict_
            fp.write(json.dumps(jdict_))

    def reload(self):
         dict_ = {}
         try:
             with open(self.__file_path, 'r', encoding="utf-8") as fp:
                 dict_ = json.load(fp)
                 for k, v in dict_.items():
                     class_ = v['__class__']
                     create_class = validClasses[class_]
                     self.__objects[k] = create_class(**v)
         except:
             pass
