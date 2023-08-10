# AirBnB Clone

The AirBnB clone project starts now until… the end of the first year. The goal of the project is to deploy on your server a simple copy of the AirBnB website.

You won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, you will have a complete web application composed by:

A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
A website (the front-end) that shows the final product to everybody: static and dynamic
A database or files that store data (data = objects)
An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)


# Command Interpreter

**How to Start**


Clone this repository to your local machine:


Navigate to the project directory:


To start the command interpreter, run the following command:


./console.py


Once the command interpreter starts, you will see a prompt (hbnb) indicating that it's ready to accept commands.


# Available Commands


**Here are the available commands and their usages:**


**quit or EOF:** Exit the program.
**help:** Display a list of available commands.
**create <class_name>:** Create a new instance of the specified class.
**show <class_name> <instance_id>:** Display the string representation of an instance.
**destroy <class_name> <instance_id>:** Delete an instance.
**all [<class_name>]:** Display all instances of the specified class or all instances.
**update <class_name> <instance_id> <attribute_name> "<attribute_value>":** Update an instance's attribute.


# Examples

**Creating a new instance:**


(hbnb) create BaseModel
<class_name>.<instance_id>


**Displaying an instance's details:**


(hbnb) show BaseModel <instance_id>
[<class_name>] (<instance_id>) {'attribute1': 'value1', 'attribute2': 'value2', ...}


**Deleting an instance:**


(hbnb) destroy BaseModel <instance_id>
Instance deleted


**Displaying all instances:**


(hbnb) all
[<class_name>] (<instance_id>) {'attribute1': 'value1', 'attribute2': 'value2', ...}
...


**Updating an instance's attribute:**



(hbnb) update BaseModel <instance_id> name "New Name"
