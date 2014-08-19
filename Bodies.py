# Copyright (c) 2014 Andrew Cleland
# Bodies.py - a family of classes of physical objects

# Import vector class
from vector import *

class Thing():
    # Parent class representing anything that has a position in 2D space
    def __init__(self, x, y):
        self.pos = vector(x, y)

class Body(Thing):
    # A physical body that allows for translational motion
    def __init__(self, x, y, vx=0, vy=0, mass=1):
        super(Body, self).__init__(x, y)
        self.mass = mass
        self.vel = vector(vx, vy)
        self.acc = vector(0, 0)  # Things start off with no acceleration

    def update(self, force=vector(0,0)):
        self.acc = force / self.mass   # Newton's 2nd law
         
    
class Ball(Body):
    # A body whose shape is a circle.
    def __init__(self, x, y, vx=0, vy=0, ax=0, ay=0, mass=1, radius)


if __name__ == '__main__':
    body = Body(1,2)
    body.pos.print()

    thing = Thing(3,4)
    thing.pos.print()
