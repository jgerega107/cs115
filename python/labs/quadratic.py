import math
'''
Created on Jacob Gerega
@author:   11/12/19
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 11
'''

class QuadraticEquation:
    '''Represents a quadratic equation and each value within it'''
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def discriminant(self):
        return pow(self.b, 2) - 4*self.a*self.c

    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            return ((self.b*-1) + math.sqrt(self.discriminant()))/(2*self.a)

    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            return ((self.b*-1) - math.sqrt(self.discriminant()))/(2*self.a)

    def __str__(self):
        apos = abs(self.a)
        bpos = abs(self.b)
        cpos = abs(self.c)

        aterm = ""
        bterm = ""
        cterm = ""

        firstop = " + "
        secondop = " + "

        #add negatives if needed
        if self.a < 0:
            aterm += "-"
        if self.b < 0:
            firstop = " - "
        if self.c < 0:
            secondop = " - "

        #finalize terms
        if apos == 1:
            aterm += "x^2"
        else:
            aterm += str(apos) + "x^2"
        if bpos == 1:
            bterm += "x"
        else:
            bterm += str(bpos) + "x"

        cterm += str(cpos)
        if cpos == 0 and bpos == 0:
            return aterm + " = 0"
        if cpos == 0:
            return aterm + firstop + bterm + " = 0"
        if bpos == 0:
            return aterm + secondop + cterm + " = 0"

        return aterm + firstop + bterm + secondop + cterm + " = 0"



