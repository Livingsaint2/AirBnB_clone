#!/usr/bin/python3
"""This module handle the reviews"""

from models.base_model import BaseModel

class Review(BaseModel):
   """This class handles the reviews objects"""

   place_id = ""
   user_id = ""
   text = ""
