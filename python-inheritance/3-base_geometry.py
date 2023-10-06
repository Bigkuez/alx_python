#!/usr/bin/python3

# Import the BaseGeometry class from the '3-base_geometry' module using __import__
BaseGeometry = __import__('3-base_geometry').BaseGeometry

# Create an instance of the BaseGeometry class and assign it to the 'bg' variable
bg = BaseGeometry()

# Print the instance 'bg' which is an object of the BaseGeometry class
print(bg)

# Print the list of attributes and methods available for the 'bg' object using the 'dir' function
print(dir(bg))

# Print the list of attributes and methods available for the BaseGeometry class itself
print(dir(BaseGeometry))
