"""
This module contains helper functions for the advanced questions
"""


import shlex
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

storage = models.storage._FileStorage__objects

validClasses = {'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review}

validClassStrings = {'BaseModel': 'BaseModel',
                     'User': 'User',
                     'State': 'State',
                     'City': 'City',
                     'Amenity': 'Amenity',
                     'Place': 'Place',
                     'Review': 'Review'}

validCommands = {'all()': 'all'}


def all(arg, empty):
    """
    A method that prints all string representation of amodels.storage.
    FileStorage__objects[key]))ll instances based
    on the class name or not.
    """

    if arg in validClasses:
        print("[", end="")
        for key in storage:
            if arg in key:
                print(storage[key], end=', ')
        print("]")

    else:
        return


def count(arg, empty):
    """Prints the number of instances in of a class"""

    count = 0
    if arg in validClasses:
        for key in storage:
            if arg in key:
                count = count + 1
    print(count)


def show(class_name, arg):
    """A method that shows instance information."""

    if class_name in validClasses:
        if arg == '':
            print("** instance id missing **")
        elif "{}.{}".format(class_name, arg) in storage:
            print(storage["{}.{}".format(class_name, arg)])
        else:
            print("** no instance found **")
    else:
        print("** class doesn't exist **")


def destroy(class_name, arg):
    """
    A method that deletes an instance based on the class name and id.
    """
    if class_name in validClasses:
        if arg == '':
            print("** instance id missing **")
        elif "{}.{}".format(class_name, arg) in storage:
            del(storage["{}.{}".format(class_name, arg)])
        else:
            print("** no instance found **")
    else:
        print("** class doesn't exist **")
        storage.save()
