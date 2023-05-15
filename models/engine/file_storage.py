#!/usr/bin/python3
"""Module for FileStorage class"""

import datetime
import json
import os

class FileStorage:
      """This class serializes instances to JSON file and
      deserializes JSON file to instances
      """

      __file_path = "file.json"
      __objects = {}

      def all(self):
          """returns the dictionary __objects"""

          return FileStorage.__objects


      def new(self, obj):
          """sets in __objects the obj with key
           <obj class name>.id
          """
          key = "{}.{}".format(type(obj).__name__, obj.id)
          FileStorage.__objects[key] = obj

      def save(self):
          """__objects to the JSON file (path: __file_path)"""

          with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
               d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
               json.dump(d, f)

      def reload(self):
          """deserializes the JSON file to __objects"""

          if not os.path.isfile(FileStorage.__file_path):
               return
          with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
              obj_dict = json.load(f)
              obj_dict = {k: self.classes()[v["__class__"]](**v)
                          for k, v in obj_dict.items()}
              FileStorage.__objects = obj_dict

      def classes(self):
          """returns the dict of valid classes"""

          from models.base_model import BaseModel

          classes = {"BaseModel": BaseModel}

          return classes
