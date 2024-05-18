#!/usr/bin/python3
"""
This Module Contains :-
-   FileStorage Class Which
    Manages The Process Of
    Storing Into JSON Format
"""


import json
import os


class FileStorage:
    """
    BaseModel Class Which Has
    All Attributes And Methods
    For Other Classes
    """

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """ Return The Objects Stored """
        return self.__objects

    def new(self, obj):
        """ Add New Object To Storage """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Save Objects Into JSON File """
        with open(self.__file_path, mode="w", encoding="utf-8") as rFile:
            json.dump({key: obj.to_dict() for key,
                      obj in self.__objects.items()}, rFile)

    def reload(self):
        """ Reload Objects From JSON File """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        class_mappings = {
            "BaseModel": BaseModel,
            "User": User,
            "Amenity": Amenity,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State
        }
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode="r", encoding="utf-8") as rFile:
                data = json.load(rFile)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name in class_mappings:
                        Class_ins = class_mappings[class_name]
                        self.__objects[key] = Class_ins(**value)
