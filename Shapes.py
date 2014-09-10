# Copyright (c) 2014 Andrew Cleland 
# Shape classes for Physics 2D 

from vector import *

class Rect():
    def __init__(self, pos, width, height):
        self.x = pos.x
        self.y = pos.y
        self.width = width
        self.height = height

    def intersectsRect(self, other):
        # Conditions for intersecting rectangles (axis aligned)
        if (self.x < other.x + other.width) and \
        (self.x + self.width > other.x) and \
        (self.y < other.y + other.height) and \
        (self.y + self.height > other.y):
            return True

        # Otherwise 
        return False

if __name__ == '__main__':
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
