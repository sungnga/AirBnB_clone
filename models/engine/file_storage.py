#!/usr/bin/python3
"""
This module contains the FileStorage class
"""
import json
from ..base_model import BaseModel

class FileStorage():
    """Class used for file storage actions"""

    __file_path = ""
    __objects = {}

    def all(self):
        return(self.__objects)

    def new(self, obj):
        obj_key = "{}.{}".format(obj['__class__'], obj['id'])
        self.__objects[obj_key] = BaseModel(**obj)

    def save(self):
        with open(self.__file_path, 'w', encoding="utf-8") as fp:
            for k, v in self.__objects.items():
                dict_ = obj.to_dict(k)
                json_ = json.dumps(dict_)
            fp.write(json_)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as fp:
                json_str = fp.read()
                for item in json_str:
                    dict_ = json.loads(item)
                    self.new(dict_)
        except Exception:
            pass
