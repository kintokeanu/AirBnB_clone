#!/usr/bin/python3

"""This module contains a File Storage class for the AirBnB"""

import json
import os


class FileStorage():
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """
        This method setts in __objects the give
        obj with key <obj class name>.id
        """
        for key, value in obj.items():
            self.__class__.__objects[key] = value

    def save(self):
        """This method serializes __objects to a JSON file"""
        with open(self.__file_path, 'w+') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """This method deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as f:
                json.loads(f.read())
