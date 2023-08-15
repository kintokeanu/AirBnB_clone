#!/usr/bin/python3
"""This a Python made console command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand is a command-line interface that allows users to
    interact with a program by entering commands.
    It provides various commands such as creating, destroying,
    searching, modifying, and showing items.
    The class also supports importing data from a file and
    displaying a help message.
    """
    prompt = " (hbnb) "
    items = {}

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Do nothing for an empty line
        """
        pass

    def help(self):
        """Display a help message that lists the available commands
        """
        print("\nDocumented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit create  destroy search  modify show import")

    def do_list(self, arg):
        """List all the items
        """
        print("Items:")
        for item in self.items:
            print(item)

    def do_create(self, arg):
        """Create a new instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print('** class does not exist **')

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of instances
        """
        instances = []
        if not arg:
            for key, value in storage.all().items():
                instances.append(str(value))
            print(instances)
        else:
            try:
                class_name = arg
                if class_name not in storage.classes():
                    print("** class doesn't exist **")
                    return
                for key, value in storage.all().items():
                    if key.split('.')[0] == class_name:
                        instances.append(str(value))
                print(instances)
            except Exception as e:
                raise e

    def do_search(self, arg):
        """Search for items that contain the given search term in their names
        """
        search_term = arg
        matching_items = [item for item in self.items if search_term in item]
        if matching_items:
            print("Matching items:")
            for item in matching_items:
                print(item)
        else:
            print("No matching items found")

    def do_update(self, arg):
        """Updates an instance based on class name and id
        """
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        try:
            class_name = args[0].lower().capitalize()
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attribute_value = args[3]
            instance = storage.all()[key]

            if hasattr(instance, attribute_name):
                attr_type = type(getattr(instance, attribute_name))
                setattr(instance, attribute_name, attr_type(attribute_value))
                instance.save()
            else:
                print("** attribute doesn't exist **")
        except IndexError:
            print("** instance id missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = f"{class_name}.{instance_id}"
            all_instances = storage.all()
            if key in all_instances:
                print(all_instances[key])
            else:
                print("** no instance found **")
        except IndexError:
            if args[0] not in storage.classes():
                print("**  class doesn't exist **")
            else:
                print("** instance id missing **")

    def do_import(self, arg):
        """Import data from a file, where each line contains an item name
            and its details separated by a colon
        """
        filename = arg
        try:
            with open(filename, 'r') as file:
                for line in file:
                    item_name, details = line.strip().split(':', 1)
                    self.items[item_name] = {'details': details}
                print(f"Imported data from {filename}")
        except FileNotFoundError:
            print(f"file {filename} not found")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
