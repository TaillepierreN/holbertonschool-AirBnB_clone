#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj in self.__objects.items()}
        with open(self.__file_path, "w") as newfile:
            json.dump(obj_dict, newfile)


    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                obj_dicts = json.load(file)
                for obj in obj_dicts.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
