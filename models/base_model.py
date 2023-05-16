#!/usr/bin/python3
"""This script is the base model"""


import uuid
from datetime import datetime
from models import storage

class BaseModel:
   """This is the base class that all other classses inherit from"""

   def __init__(self, *args, **kwargs):
       """Initializes instance attributes"""

       if kwargs:
          for key, value in kwargs.items():
              if key != '__class__':
                   if key in ['created_at', 'updated_at']:
                      value  = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                   setattr(self, key, value)
       else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new()

   def __str__(self):
       """returns human-readable string representation of an instance"""

       class_name = self.__class__.__name__
       return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

   def save(self):
       """updates the public instance attribute updated_at
          with the current datetime
       """

       self.updated_at = datetime.now()
       return storage.save()

   def to_dict(self):
       """Returns a dictionary containing all keys/values of __dict__
          of the instance
       """

       my_dict = self.__dict__.copy()
       my_dict['__class__'] = self.__class__.__name__
       my_dict['created_at'] = my_dict["created_at"].isoformat()
       my_dict['updated_at'] = my_dict["updated_at"].isoformat()

       return my_dict
