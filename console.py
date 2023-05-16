#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
<<<<<<< HEAD

    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, line):
        """Catch commands if nothing else matches then."""
        # print("DEF:::", line)
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True

    def do_quit(self, line):
        """Exits the program.
        """
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass

    def do_create(self, line):
        """Creates an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """Prints the string representation of an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_count(self, line):
        """Counts the instances of a class.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """Updates an instance by adding or updating attribute.
        """
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
            print("** instance id missing **")
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
                if not re.search('^".*"$', value):
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
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


=======
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
                  
          elif not issubclass(storage.classes()[line], BaseModel):
            print("** class is not subclass of BaseModel **")

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
                     print("** class name doesn't exist **")
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
                      except ValueError:
                        pass
                  setattr(storage.all()[key], attribute, value)
                  storage.all()[key].save()
>>>>>>> db1012d106cd8d854f688561469e996a1de085b7
if __name__ == '__main__':
    HBNBCommand().cmdloop()
