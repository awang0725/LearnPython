#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:17:47 2018

@author: awang
"""

from math import sqrt,acos,pi,sin
from decimal import Decimal,getcontext

getcontext().prec = 6

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize a zero vector'
    #tolerance = 1e-10

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def plus(self,v):
        
        new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)
    
    def minus(self,v):
        
        new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)
    
    def times_scalar(self,c):
        
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)
    
    def magnitude(self):
        
        return Decimal(sqrt(sum([x**2 for x in self.coordinates])))
    
    def normalized(self):
        
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0')/magnitude)
        
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
    
    def dot(self,v):
                
        return sum([x*y for x,y in zip(self.coordinates,v.coordinates)])
    
    def angle(self,v,flag_degrees = False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angles_in_radians = acos(u1.dot(u2))
            
            if flag_degrees:
                return angles_in_radians * 180.0/pi
            else:
                return angles_in_radians
        
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot find angle with a zero vector!')
            else:
                raise e

    def is_parallel(self,v):
        return (self.is_zero() or
                v.is_zero() or
                self.angle(v) == 0 or
                self.angle(v) == pi)

    def orthogonal(self,v,tolerance=1e-10):
        return tolerance > abs(self.dot(v))

    def is_zero(self,tolerance=1e-10):
        return self.magnitude() < tolerance

    def projection_to(self,v):
        #return v.times_scalar(self.dot(v.normalized()))
        return v.normalized().times_scalar(self.dot(v.normalized()))

    def orthogonal_to(self,v):
        return self.minus(self.projection_to(v))

    def cross(self,v):
        x1,y1,z1 = self.coordinates
        x2,y2,z2 = v.coordinates

        return Vector([y1*z2-y2*z1,-x1*z2+x2*z1,x1*y2-x2*y1])

    def paralleogram_area(self,v):
        return Decimal(self.magnitude()) * Decimal(v.magnitude()) * Decimal(sin(self.angle(v)))

    def triangle_area(self,v):
        return Decimal(0.5)*Decimal(self.paralleogram_area(v))

    def __getitem__(self, item):
        return self.coordinates[item]

