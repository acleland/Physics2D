# Copyright (c) 2014 Andrew Cleland
# Bodies.py - a family of classes of physical objects


# thing.py - Thing() class for Physics 2D 
#   -Represents anything that has a position on the screen.

# Import vector class
from vector import *

class Thing():
    # Parent class representing anything that has a position in 2D space
    def __init__(self, x, y):
        self.pos = vector(x, y)

class Body(Thing):
    # A physical body that allows for translational motion
    def __init__(self, x, y, vx=0, vy=0, ax=0, ay=0, mass=1):
        super(Body, self).__init__(x, y)

if __name__ == '__main__':
    body = Body(1,2)
    body.pos.print()

    thing = Thing(3,4)
    thing.pos.print()
