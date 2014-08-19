# Copyright (c) 2014 Andrew Cleland
# A 2D vector class to be used in my physics module

import math

class vector():
    # Initialize x and y components
    def __init__(self, vx, vy):
        self.x = vx
        self.y = vy
    
    # Setter method
    def setVector(self, vx, vy):
        self.x = vx
        self.y = vy

    # Print the vector neatly
    def print(self):
        print('(' + str(self.x) + ', ' + str(self.y) + ')') 

    # Vector addition - Use regular '+' syntax. E.g. v1 + v2
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    # Vector subtraction
    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y)

    # Dot product
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    # Magnitude
    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    # Return angle between two vectors
    def ang(self, other, unit='r'):
        angle = acos(self.dot(other) / (self.mag() * other.mag()))
        if unit == 'r':    # default is radians
            return angle
        elif unit == 'd':     # convert to degrees if specified
            return 360 / (2*math.pi)
    
    # Scalar multiplication - Use '*' syntax with scalar after vector E.g. v*3
    def __mul__(self, scalar):
        return vector(scalar * self.x, scalar * self.y)

    # Scalar division - Use v/scalar
    def __truediv__(self, scalar):
        return  vector(self.x / scalar, self.y / scalar)

    # Increment by (dx, dy)
    def inc(self, dx, dy):
        self.x += dx
        self.y += dy
    
