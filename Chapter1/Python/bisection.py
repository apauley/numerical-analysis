#!/usr/bin/env python

from helpers import *

def bisection(func, a, b, max_steps=MaxSteps):
    print "Using Bisection Method to solve %s\n" % func.__doc__
    initial = func(a)
    for loopCounter in range(max_steps):
        midPoint = a + (b-a)/2
        result = func(midPoint)
        print "Accuracy is within %.9f " % (abs(b-a)/2.0)
        if (result == 0 or ( (abs(b-a)/2.0) > 0)):
            a = midPoint
            initial = result
        else:
            b = midPoint

if __name__ == '__main__':
    bisection(example_f, 0, 1)
