# Testing git merge
# Copyright (c) 2014 Andrew Cleland 
# Shape classes for Physics 2D 

from vector import *
from Bodies import *

class Rect():
    def __init__(self, thing, width, height):
        self.thing = thing
        self.width = width
        self.height = height

    def intersectsRect(self, other):
        # Conditions for intersecting rectangles (axis aligned)
        if (self.thing.pos.x < other.thing.pos.x + other.width) and \
        (self.thing.pos.x + self.width > other.thing.pos.x) and \
        (self.thing.pos.y < other.thing.pos.y + other.height) and \
        (self.thing.pos.y + self.height > other.thing.pos.y):
            return True

        # Otherwise 
        return False

if __name__ == '__main__':
# Note: these tests need to updated to things as input, rather than vectors
    rect1 = Rect(vector(0,0), 3, 2)
    rect2 = Rect(vector(2,1), 2, 2)
    rect3 = Rect(vector(0,1), 1, 2)
    rect4 = Rect(vector(2,4), 1, 1)

    print(rect1.intersectsRect(rect2) == True) 
    print(rect2.intersectsRect(rect1) == True) 
    print(rect3.intersectsRect(rect1) == True) 
    print(rect3.intersectsRect(rect2) == False)
    print(rect3.intersectsRect(rect4) == False)
    print(rect1.intersectsRect(rect4) == False)
    print(rect2.intersectsRect(rect4) == False)
    
    rect5 = Rect(vector(4,3), 1, 1)
    print(rect5.intersectsRect(rect2))
