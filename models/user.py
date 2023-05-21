#!/usr/bin/python3
"""This module handles the user's"""

from models.base_model import BaseModel

class User(BaseModel):
   """This is the user class managing user objects"""

   email = ""
   password = ""
   first_name = ""
   last_name = ""
