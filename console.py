#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
