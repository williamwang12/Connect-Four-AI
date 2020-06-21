# Matrix class
# Spring 2020

from Vector import *

class Matrix:
    """ 2x2 Matrix class """

    def __init__(self, a11=0, a12=0, a21=0, a22=0):
        self.array = [[a11, a12], [a21, a22]]

    def __repr__(self):
        return str(self.array[0][0]) + " " + str(self.array[0][1]) + "\n" + \
            str(self.array[1][0]) + " " + str(self.array[1][1])

    def get(self, row, col):
        """Get value at given row and column"""
        return self.array[row][col]

    def set(self, row, col, value):
        """Set element at row and column to given value"""
        self.array[row][col] = value

    def __mul__(self, other):
        """If other is a Matrix, returns a Matrix X*Y.  If other is a Vector, returns a Vector X*y."""
        if isinstance(other, Matrix):
            result = Matrix()
            for row in range(0, 2):
                for col in range(0, 2):
                    # compute result matrix in the given row and col
                    entry = 0
                    for i in range(0, 2):
                        entry += self.get(row, i) * other.get(i, col)
                    result.set(row, col, entry)
            return result
        elif isinstance(other, Vector):
            x = self.get(0, 0) * other.x + self.get(0, 1) * other.y
            y = self.get(1, 0) * other.x + self.get(1, 1) * other.y
            return Vector(x, y)
        else:
            print("Can't multiply a matrix by a ", other.__class__.__name__, "!!!")  # !!! is a nice touch

    def __add__(self, other):        

        '''
        INPUT: inputs the object, and then another matrix to be added.
        OUTPUT: outputs matrices added together.
        '''
        a = self.array[0][0] + other.get(0,0)
        b = self.array[0][1] + other.get(0,1)
        c = self.array[1][0] + other.get(1,0)
        d = self.array[1][1] + other.get(1,1)

        newMatrix = Matrix(a,b,c,d)
        return newMatrix