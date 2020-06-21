# Vector class
# Spring 2020

import math

class Vector:
    """ Vector class """

    def __init__(self, x=0, y=0):
        # x = 0, y = 0 are default values.  This allows us to either pass in 
        # values or to use v = Vector() and this will automatically set the 
        # x- and y-coordinates to 0.
        
        self.x = x
        self.y = y

    def __repr__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def magnitude(self):
        """Returns magnitude of vector"""
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalize(self):
        """Sets vector magnitude to 1"""
        mag = self.magnitude()
        self.x = self.x/mag
        self.y = self.y/mag

    def __neg__(self):
        """Returns new Vector -x""" 
        return Vector(-self.x, -self.y)

    def __add__(self, other):
        """Returns new Vector x + y"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Returns new Vector x - y"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        '''
        INPUT: inputs the object, and then an integer to be multiplied.
        OUTPUT: outputs vector multipled by the scalar.
        '''
        return Vector(self.x * float(number), self.y * float(number))