#!/usr/bin/python3
"""The module for filestorage class"""


import datetime
import json
import os


class FileStorage:
      """This class serializes instances to a JSON file
      and then deserializes JSON file to instances
      """

      __file_path= "file.json"
      __objects = {}


      def all(self):
          """Returns the dictionary __objects"""

          return FileStorage.__objects


      def new(self, obj):
          """sets in __objects the obj with key <obj class name>.id"""

          pass


       def save(self):
           """serializes __objects to the JSON file (path: __file_path)"""

           pass

       def reload(self):
           """deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists

            Otherwise: do nothing
                       If the file doesn’t exist, no exception should be raised)
            """
