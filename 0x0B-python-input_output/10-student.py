#!/usr/bin/python3

""" Class Student defining a student """


class Student:
    """ Defines a student """

    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Args:
            attrs (list): The attributes to represent.
        Returns:
            Dictionary representation of student
        """
        if (type(attrs) == list and
                all(type(stuff) == str for stuff in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
