#!/usr/bin/python3
"""
This module contains the class FileStorage
that serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json
from os.path import exists
from models.base_model import BaseModel


class FileStorage():
    """
    Initializing all attributes and methods:

    __file_path : str - path to JSON file
    __objects : dict - empty but will store all objects by <class>.id

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to JSON file (path:__file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        if __file_path doesn't exist, nothing is done
        """
        if exists(self.__file_path) is False:
            return
        else:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
