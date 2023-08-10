#!/usr/bin/env python3
import uuid
from datetime import datetime

class BaseModel:
    """
    A base model class that provides common functionality for other classes.

    Attributes:
        id (str): The unique identifier of the object.
        created_at (datetime): The datetime when the object was created.
        updated_at (datetime): The datetime when the object was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Keyword Args:
            created_at (str): The string representation of the datetime when the object was created.
            updated_at (str): The string representation of the datetime when the object was last updated.
            Other attributes: Any other attributes to be set on the object.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: The string representation of the object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute of the object with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the object to a dictionary.

        Returns:
            dict: The dictionary representation of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


# data = {
#     "id": "123",
#     "created_at": "2023-07-19T15:30:00.000000",
#     "updated_at": "2023-07-19T16:45:00.000000",
#     "name": "John",
#     "age": 30
# }

# instance = BaseModel(**data)
# print(instance.id)
# print(instance.created_at)
# print(instance.updated_at)
# print(instance.name)
# print(instance.age)