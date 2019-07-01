#!/usr/bin/python3
"""
This is a module for HBNBCommand class.
"""
import shlex
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
            y.save()
            print(y.id)
        else:
            print("** class doesn't exist **")
    def help_create(self):
        """A method that allows users to get documentation on create."""
        print("A commend that creates an instance of a class")

    def do_show(self, arg):
        """A method that shows instance information."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] in self.validClasses:
            if len(args) < 2:
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
        args = shlex.split(arg)
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
        print(("A command that destroys an instance based")
        + (" on the class name and id"))

    def do_all(self, arg):
        """A method that prints all string representation of amodels.storage._FileStorage__objects[key]))ll instances based
        on the class name or not."""
        args = shlex.split(arg)
        ret_list = []
        if not arg:
            for class_name_key in self.validClasses:
                for key in models.storage._FileStorage__objects:
                    if class_name_key in key:
                        ret_list.append(str(models.storage._FileStorage__objects[key]))
            print(ret_list)
        else:
            if args[0] in self.validClasses:
                for key in models.storage._FileStorage__objects:
                    if arg[0] in key:
                        ret_list.append(str(models.storage._FileStorage__objects[key]))
                print(ret_list)
            else:
                print("** class doesn't exist **")
    def help_all(self):
        """A method that allows users to get documentation on all."""
        print("A command that prints all string representation of all instances")

    def do_update(self, arg):
        """A method that updates an instance based on the class name and id
        by adding or updating attribute."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            # return
        elif args[0] not in self.validClasses:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(args[0], args[1])
            try:
                instance = models.storage._FileStorage__objects[key]
            except:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            else:
                if len(args) < 4:
                    print("** value missing **")
                    return
                else:
                    try:
                        type_ = type(getattr(instance, args[2]))
                        setattr(instance, args[2], type_(args[3]))
                    except:
                        setattr(instance, args[2], args[3])
    def help_update(self):
        """ """
        print(("A command that updates instances. Usage: update <class name>") +
              ("<id> <attribute name> \"<attribute value>\""))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
