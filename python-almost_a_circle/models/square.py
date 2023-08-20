"""
    Square a Rectangle.
"""
from models.rectangle import Rectangle
"""
    Square a Rectangle.
"""
class Square(Rectangle):
    """This class Square a Square."""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square's sides.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The unique identifier of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size of the square's sides.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square's sides.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
