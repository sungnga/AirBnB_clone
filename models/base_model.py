#!/usr/bin/python3
"""
This module contains the BaseModel Class
"""
import uuid
import copy
from datetime import datetime


class BaseModel():
    """Class representing the BaseModel Class"""

    def __init__(self, *args, **kwargs):
        # create uuid when instance is initialized and convert to string
        if kwargs:
            for key, value in kwargs.items():
                if (key == 'created_at' or key == 'updated_at'):
                    self.key = datetime.fromisoformat(value)
                self.key = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at 
    def __str__(self):
        """Method that returns a string representation of an instance"""
        return ("[{}] ({}) <{}>".format(self.__class__.__name__,
                                        self.id,
                                        self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_ = copy.deepcopy(self.__dict__)
        dict_['updated_at'] = dict_['updated_at'].isoformat()
        dict_['created_at'] = dict_['created_at'].isoformat()
        dict_['__class__'] = self.__class__.__name__
        return (dict_)
