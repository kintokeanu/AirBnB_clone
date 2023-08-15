#!/usr/bin/env python3
"""Module for BaseModel class
"""
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
            *args: Variable length argument list.ls

            **kwargs: Arbitrary keyword arguments.

        Keyword Args:
            created_at (str): The string representation of the datetime
            when the object was created.
            updated_at (str): The string representation of the datetime
            when the object was last updated.
            Other attributes: Any other attributes to be set on the object.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value,
                            '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: The string representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute of the
        object with the current datetime.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Converts the object to a dictionary.

        Returns:
            dict: The dictionary representation of the object.
        """
        copy = self.__dict__.copy()
        copy["__class__"] = self.__class__.__name__
        copy["created_at"] = self.created_at.isoformat()
        copy["updated_at"] = self.updated_at.isoformat()
        return copy
