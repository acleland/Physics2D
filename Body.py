# Copyright (c) 2014 Andrew Cleland
# Body.py - A body that is translatable

from Thing import *

class Body(Thing):
    # Constructor
    def __init__(self, x, y, vx=0, vy=0, ax=0, ay=0, mass=1):
        super(Body, self).__init__(x, y)

if __name__ == '__main__':
    body = Body(1,2)
    print(body.x, body.y)
