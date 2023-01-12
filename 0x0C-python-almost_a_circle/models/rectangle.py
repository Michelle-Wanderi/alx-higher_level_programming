#!/usr/bin/python3

import json
import csv
import turtle

"""
a class that inherits from Base
"""
    class Rectangle(Base):
        """
        Represent a rectangle
        """
        def __init__(self,width, height, x=0, y=0, id=None):
            """
            Initialize a new rectangle
            Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
            """
            self.width = width
            self.height = height
            self.x = x
            self.y = y
            super().__init__(id)



