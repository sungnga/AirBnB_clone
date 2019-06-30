#!/usr/bin/python3
"""
This is a module for HBNBCommand class.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class representing the HBNBcommand class"""
    prompt = '(hbnb) '

    def do_quit(self, s):
        return True
    def help_quit(self):
        print ("Quit command to exit the program")
    def emptyline(self):
        pass
    do_EOF = do_quit
    help_EOF = help_quit








if __name__ == '__main__':
    HBNBCommand().cmdloop()
