#!/usr/bin/python3
"""
    Thisepresents a Base.
"""
from models.base import Base
"""
    Represents a Base.
"""
class Rectangle(Base):
    """This class represents a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize attributes of the rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the Rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Display the Rectangle instance as a series of '#' characters
        representing its dimensions on the standard output.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a string representation of the Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Update attributes of the Rectangle instance based on given
        positional arguments and/or keyword arguments.
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for index, value in enumerate(args):
                setattr(self, attributes[index], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
