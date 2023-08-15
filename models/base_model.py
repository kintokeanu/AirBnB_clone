#!/usr/bin/python3
"""Docstring for the Basemodel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    This is the base model class that provides common attributes
     and methods for other classes.

    Attributes:
        id (str): The unique identifier of the instance.
        created_at (datetime): The date and time when the instance was created.
        updated_at (datetime): The date and time when the instance was last
        updated.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key != "created_at" and key != "updated_at":
                    self.__dict__[key] = value
                else:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """
        Returns a string representation of the instance.

        Returns:
            str: The string representation of the instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Saves the instance and updates the updated_at attribute.

        This method saves the instance using the models.storage.save()
        method and updates the updated_at attribute
        to the current date and time.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance to a dictionary.

        Returns:
            dict: The dictionary representation of the instance.
        """
        copy = self.__dict__.copy()
        copy["__class__"] = self.__class__.__name__
        copy["created_at"] = self.created_at.isoformat()
        copy["updated_at"] = self.updated_at.isoformat()
        return copy
