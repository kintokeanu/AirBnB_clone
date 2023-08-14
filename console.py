#!/usr/bin/python3
"""This a Python made console command interpreter"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    my_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_EOF(self, line=None):
        """This method exit the console when Ctrl-D (EOF) is pressed"""
        print()
        return True

    def do_quit(self, line=None):
        """This method exit the console at the given of quit command"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """This method create a new instance of a given object and save it"""
        if line == "":
            print("** class name missing **")
            return False

        command_list = line.split()
        command = command_list[0]
        if command not in self.my_classes.keys():
            print("** class doesn't exist **")
            return False

        new_obj = type(self).my_classes[command]()
        storage.new(new_obj)
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        """
        This method print string representation of an
        instance based on the class name and id
        """
        if line == "":
            print("** class name missing **")
            return False

        command_list = line.split()
        command = command_list[0]
        command_id = ""
        if len(command_list) > 1:
            command_id = command_list[1]
        if command not in self.my_classes.keys():
            print("** class doesn't exist **")
            return False

        if command_id == "":
            print("** instance id missing **")
            return False

        class_key = f"{command}.{command_id}"
        storage.reload()
        all_objs = storage.all()
        if class_key in all_objs:
            print(all_objs[class_key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        This method deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        if line == "":
            print("** class name missing **")
            return False

        command_list = line.split()
        command = command_list[0]
        command_id = ""
        if len(command_list) > 1:
            command_id = command_list[1]
        if command not in self.my_classes.keys():
            print("** class doesn't exist **")
            return False

        if command_id == "":
            print("** instance id missing **")
            return False

        class_key = f"{command}.{command_id}"
        storage.reload()
        all_objs = storage.all()
        if class_key in all_objs:
            del (all_objs[class_key])
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        This method prints all string representation of
        all instances based or not on the class name
        """
        class_name = f"{line}"
        storage.reload()
        all_objs = storage.all()
        if class_name:
            my_classes = [
                str(all_objs[k]) for k in all_objs.keys() if k.split(".")
                [0] == class_name
            ]
            if not my_classes:
                print("** class doesn't exist **")
                return
        else:
            my_classes = [str(all_objs[k]) for k in all_objs.keys()]

        print(my_classes)

    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def do_update(self, line):
        """
        This method updates an instance based on the class name
        and id by adding or updating attribute (save the change
        into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"

        Keyword arguments:
        line -- the given command line
        Return: void
        """
        args_list = re.findall(r'"[^"]*"|\S+', line)
        if len(args_list) < 1:
            print("** class name missing **")
            return
        elif args_list[0] not in self.my_classes:
            print("** class doesn't exist **")
            return
        elif len(args_list) == 1:
            print("** instance id missing **")
            return
        elif len(args_list) == 2:
            print("** attribute name missing **")
            return
        elif len(args_list) == 3:
            print("** value missing **")
            return
        elif len(args_list) > 4:
            args_list = args_list[:4]

        if args_list[0] not in self.my_classes:
            print("** class doesn't exist **")
            return

        class_key = f"{args_list[0]}.{args_list[1]}"
        class_attribute = args_list[2]
        class_value = args_list[3][1:-1]

        storage.reload()
        all_objs = storage.all()
        if class_key in all_objs:
            if class_value.isdigit():
                class_value = int(class_value)
            elif (self.isfloat(class_value)):
                class_value = float(class_value)
            all_objs[class_key].__setattr__(
                class_attribute, class_value)
            all_objs[class_key].save()
            return
        else:
            print("** no instance found **")
            return


if __name__ == "__main__":
    HBNBCommand().cmdloop()

