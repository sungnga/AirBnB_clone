#!/usr/bin/python3
"""
This is a module for HBNBCommand class.
"""
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Class representing the HBNBcommand class"""
    prompt = '(hbnb) '
    validClasses = {'BaseModel': BaseModel}

    def do_quit(self, s):
        """A method that allows users to quit."""
        return True
    def help_quit(self):
        """A method that allows users to get documentation on quit."""
        print ("Quit command to exit the program")
    def emptyline(self):
        """A method that overwrites the default when no command is given."""
        pass
    do_EOF = do_quit
    help_EOF = help_quit

    def do_create(self, arg):
        """A method that creates an instance of a class."""
        if not arg:
            print("** class name missing **")
        elif arg in self.validClasses:
            x = self.validClasses[arg]
            y = x()
            models.storage.save()
            print(y.id)
        else:
            print("** class doesn't exist **")
    def help_create(self):
        """A method that allows users to get documentation on create."""
        print("A commend that creates an instance of a class")

    def do_show(self, arg):
        """A method that shows instance information."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] in self.validClasses:
            if len(args) != 2:
                print("** instance id missing **")
            elif "{}.{}".format(args[0], args[1]) in models.storage._FileStorage__objects:
                print(models.storage._FileStorage__objects["{}.{}".format(args[0], args[1])])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")
    def help_show(self):
        """A method that allows users to get documentation on show."""
        print("A command that shows the information of an instance")

    def do_destroy(self, arg):
        """A method that deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] in self.validClasses:
            if len(args) != 2:
                print("** instance id missing **")
            elif "{}.{}".format(args[0], args[1]) in models.storage._FileStorage__objects:
                del(models.storage._FileStorage__objects["{}.{}".format(args[0], args[1])])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")
    def help_destroy(self):
        """A method that allows users to get documentation on destroy."""
        print("A command that destroys an instance based on the class name
        and id")

    def do_all(self, arg):
        """A method that prints all string representation of all instances based
        on the class name or not."""
        if not arg:
            for class_name in validClasses:
                for instance in validClasses[class_name]:
                print(models.storage._FileStorage__objects["{}.{}".format(args[0], args[1])])



    def help_all(self):
        """A method that allows users to get documentation on all."""
        print("A command that prints all string representation of all instances")





if __name__ == '__main__':
    HBNBCommand().cmdloop()
