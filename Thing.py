# Copyright (c) 2014 Andrew Cleland
# thing.py - Thing() class for Physics 2D 
#   -Represents anything that has a position on the screen.

class Thing():
    def __init__(self, x, y):
        self.__pos = [x, y]

    @property
    def pos(self):
        return self.__pos

    @property
    def x(self):
        return self.__pos[0]

    @property
    def y(self):
        return self.__pos[1]

    def setPos(self, x, y):
        self.__pos = [x, y]


