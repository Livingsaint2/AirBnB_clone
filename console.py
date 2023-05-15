#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""


import cmd
from models.base_model import BaseModel
from models import storage
import json
import re

class HBNBCommand(cmd.Cmd):
      """This is the class of the command interptreter"""

      prompt = "(hbnb) "

      def do_EOF(self, line):
          """This is the end-of-file marker"""

          return True

      def do_quit(self, line):
          """Quit command to exit the program"""

          return True

      def emptyline(self):
          """This shouldn't do anything"""

          pass

      def do_create(self, line):
          """Creates a new instance of BaseModel"""

          if line is None:
             print("** class name missing **")

          elif line not in storage.classes():
              print("** class doesn't exist **")

          else:
              instance = storage.classes()[line]()
              instance.save()
              print(instance.id)

      def do_show(self, line):
          """Prints the string representation of an instance"""

          args = line.split()
          if not args:
              print("** class name missing **")
          else:
             try:
                 class_name = args[0]
                 obj_id = args[1]
                 obj_key = "{}.{}".format(class_name, obj_id)
                 obj_dict = storage.all()
                 if class_name not in storage.classes():
                     print("** class name doesn't exist**")
                 elif len(args) < 2:
                     print("** instance id is missing **")
                 elif obj_key not in obj_dict:
                     print("** no instance found**")
                 else:
                     obj = obj_dict[obj_key]
                     print(obj)
             except IndexError:
                 print("** instance id missing **")

      def do_destroy(self, line):
          """Deletes an instance based on the class name and id"""

          args = line.split()
          if not args:
              print("** class name missing **")
          else:
             try:
                 class_name = args[0]
                 obj_id = args[1]
                 obj_key = "{}.{}".format(class_name, obj_id)
                 obj_dict = storage.all()
                 if class_name not in storage.classes():
                     print("** class name doesn't exist**")
                 elif len(args) < 2:
                     print("** instance id is missing **")
                 elif obj_key not in obj_dict:
                     print("** no instance found**")
                 else:
                     obj = obj_dict[obj_key]
                     del obj_dict[obj_key]
                     storage.save()
             except IndexError:
                 print("** instance id missing **")

      def do_all(self, line):
          """Prints all string representation of instance"""

          if not line:
              print([str(obj) for obj in storage.all().values()])
          else:
              class_name = line.split()[0]
              if class_name not in storage.classes():
                  print("** class doesn't exist **")
              else:
                  print([str(obj) for obj in storage.all().values() if type(obj).__name__ == class_name])


      def do_update(self, line):
          """Updates an instance based on the class name and id"""

          if line == "" or line is None:
              print("** class name missing **")
              return

          rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
          match = re.search(rex, line)
          classname = match.group(1)
          uid = match.group(2)
          attribute = match.group(3)
          value = match.group(4)

          if not match:
              print("** class name missing **")
          elif classname not in storage.classes():
              print("** class doesn't exist **")
          elif uid is None:
              print ("** instance id is missing **")
          else:
              key = "{}.{}".format(classname, uid)
              if key not in storage.all():
                  print("** no instance found **")
              elif not attribute:
                  print("** attribute name missing **")
              elif not value:
                  print("** value missing **")
              else:
                  cast = None
                  if not re.search('^"."$', value):
                      if '.' in value:
                          cast = float
                      else:
                          cast = int
                  else:
                      value = value.replace('"', '')
                  attributes = storage.attributes()[classname]
                  if attribute in attributes:
                      value = attributes[attribute](value)
                  elif cast:
                      try:
                         value = cast(value)
                      except VAlueError:
                        pass
                  setattr(storage.all()[key], attribute, value)
                  storage.all()[key].save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
