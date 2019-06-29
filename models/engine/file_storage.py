#!/usr/bin/python3
"""
This module contains the FileStorage class
"""
import json
from models.base_model import BaseModel

class FileStorage():
    """Class used for file storage actions"""

    __file_path = "" + ".json"
    __objects = {}

    def all(self):
        return(self.__objects)

    def new(self, obj):
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        with open(self.__file_path, 'w', encoding="utf-8") as fp:
            for k, v in self.__objects.items():
                dict_ = self.__objects[k].to_dict()
                json_ = json.dumps(dict_)
            fp.write(json_)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as fp:
                json_str = fp.read()
                for k, v in json_str.items():
                    dict_ = json.loads(item)
                    self.new(dict_)
        except Exception:
            pass
