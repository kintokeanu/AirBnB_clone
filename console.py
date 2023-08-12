#!/usr/bin/python3
"""This a Python made console command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line=None):
        """This method exit the console when Ctrl-D (EOF) is pressed"""
        print()
        return True

    def do_quit(self, line=None):
        """This method exit the console at the given of quit command"""
        return True

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
