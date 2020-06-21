# Shapes
# Spring 2020

import math
import turtle

from Vector import *
from Matrix import *

#turtle.hideturtle()

class Shape:
    """Shape class"""

    def __init__(self):
        self.points = []

    def render(self):
        """Use turtle graphics to render shape"""
        turtle.hideturtle()  # don't show the turtle
        turtle.penup()
        turtle.setposition(self.points[0].x, self.points[0].y)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.pencolor(self.color)
        turtle.begin_fill()
        for vector in self.points[1:]:
            turtle.setposition(vector.x, vector.y)
        turtle.end_fill()

    def erase(self):
        """ Draw shape in white to effectively erase it from screen """
        temp = self.color
        self.color = "white"
        self.render()
        self.color = temp

    def rotate(self, theta, about=Vector(0,0)):
        """ Rotate shape by theta degrees """
        '''
        INPUT: inputs the object, integer theta, and then the Vector to be rotated about.
        OUTPUT: Rotates the object by theta about the Vector input.
        '''

        # Python's trig functions expect input in radians,
        # so this function converts from degrees into radians.
        theta = math.radians(theta)
        rotation_matrix = Matrix(math.cos(theta), -math.sin(theta), math.sin(theta), math.cos(theta))
        new_points = []
        self.translate(-about)
        for vector in self.points:
            new_vector = rotation_matrix * vector    
            new_points.append(new_vector)
        self.points = new_points
        self.translate(about)
        self.center = self.find_center()

    def find_center(self):
        '''
        INPUT: inputs the object.
        OUTPUT: finds the center of the object and returns it.
        '''
        total = 0
        for i in range(len(self.points)):
            total = total + self.points[i].x
        xAvg = total / len(self.points)

        total = 0
        for i in range(len(self.points)):
            total = total + self.points[i].y
        yAvg = total / len(self.points)     

        center = Vector(xAvg, yAvg)
        return center   

    def translate(self, shift):
        '''
        INPUT: inputs the object, and then an integer to be translated by.
        OUTPUT: translates the object by the shift integer.
        '''

        new_points = []
        for vector in self.points:
            new_vector = vector + shift
            new_points.append(new_vector)
        self.points = new_points
        self.center = self.find_center()

    def scale(self, stretch):
        '''
        INPUT: inputs the object, and an integer to be stretched by.
        OUTPUT: stretches the object by stretch.
        '''
        center = self.find_center()
        self.translate(-center)

        scaleMatrix = Matrix(stretch,0,0,stretch)
        new_points = []
        for vector in self.points:
            newVector = scaleMatrix * vector
            new_points.append(newVector)
        
        
        self.points = new_points
        self.translate(center)


class Rectangle(Shape):
    """ A rectangle """
    def __init__(self, width, height, center=Vector(0, 0), color="black"):
        SW = Vector(center.x - width/2.0, center.y - height/2.0)
        NW = Vector(center.x - width/2.0, center.y + height/2.0)
        NE = Vector(center.x + width/2.0, center.y + height/2.0)
        SE = Vector(center.x + width/2.0, center.y - height/2.0)
        self.points = [SW, NW, NE, SE]
        self.color = color
        self.center = self.find_center()


class Square(Rectangle):
    """ A square """
    def __init__(self, width, center=Vector(0, 0), color="black"):
        Rectangle.__init__(self, width, width, center, color)
        self.center = self.find_center()


class Circle(Shape):
    """ A circle """
    def __init__(self, center=Vector(0, 0), radius=10, color="black"):
        self.center = center
        self.radius = radius
        self.color = color

    def render(self):
        turtle.penup()
        turtle.setposition(self.center.x, self.center.y - self.radius)
        turtle.pendown()
        turtle.fillcolor(self.color)
        turtle.pencolor(self.color)
        turtle.begin_fill()
        
        turtle.circle(self.radius)
        turtle.end_fill()

    def translate(self, shift):
        '''
        INPUT: inputs the object, and then an integer to be translated by.
        OUTPUT: translates the object by the shift integer.
        '''
        self.center.x = self.center.x + shift.x
        self.center.y = self.center.y + shift.y

    def rotate(self, theta, about=Vector(0,0)):
        '''
        INPUT: inputs the object, integer theta, and then the Vector to be rotated about.
        OUTPUT: Rotates the object by theta about the Vector input.
        '''
        theta = math.radians(theta)
        rotation_matrix = Matrix(math.cos(theta), -math.sin(theta), math.sin(theta), math.cos(theta))
        new_center = rotation_matrix * self.center
        self.center = new_center

    def scale(self, stretch):
        '''
        INPUT: inputs the object, and an integer to be stretched by.
        OUTPUT: stretches the object by stretch.
        '''
        self.radius = self.radius * stretch

    def find_center(self):
        '''
        INPUT: inputs the object.
        OUTPUT: finds the center of the object and returns it.
        '''
        return self.center

class LineSegment(Shape):
    def __init__(self, v1, v2):
        '''
        INPUT: inputs the object, and two vectors.
        OUTPUT: creates a line segment between the two points.
        '''
        self.v1 = v1
        self.v2 = v2
        self.points = [v1,v2]
        self.center = self.find_center()

class Compound(Shape):
    def __init__(self, center=Vector(0,0), shape_list=[]):
        '''
        INPUT: inputs the object, center, and shape_list.
        OUTPUT: creates a compound with center and shapes in shape_list specified.
        '''
        self.center = center
        self.shape_list = shape_list

    def render(self):
        '''
        INPUT: inputs the object.
        OUTPUT: renders every shape in the compound.
        '''
        for shape in self.shape_list:
            shape.render()
    
    def rotate(self, theta, about=Vector(0,0)):
        '''
        INPUT: inputs the object, integer theta, and then the Vector to be rotated about.
        OUTPUT: Rotates the shape objects by theta about the Vector input.
        '''
        for shape in self.shape_list:
            shape.rotate(theta,about)

    def scale(self, stretch):
        '''
        INPUT: inputs the object, and an integer to be stretched by.
        OUTPUT: stretches the object by stretch.
        '''
        for shape in self.shape_list:
            shape.scale(stretch)       
    
    def append(self, shape):
        '''
        INPUT: inputs the object, and the shape to be added.
        OUTPUT: adds the shape to the compound.
        '''
        self.shape_list.append(shape)
    
    def __add__(self, other):
        '''
        INPUT: inputs the object, and another compound to be added.
        OUTPUT: returns a singular compound with the shapes of both in it.
        '''
        copy = self.shape_list
        for shape in other.shape_list:
            copy.append(shape)

        midX = (other.center.x + self.center.x) * 0.5
        midY = (other.center.y + self.center.y) * 0.5
        mid = Vector(midX,midY)

        newCompound = Compound(mid, copy)
        return newCompound

    
    