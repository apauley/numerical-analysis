#!/usr/bin/env python

from helpers import *

def bisection(func, a, b, max_steps=MaxSteps):
    print_header("Bisection Method", func)
    initial = evaluate(func,float(a))
    for loopCounter in range(max_steps):
        midPoint = a + (b-a)/2.0
        result = evaluate(func,float(midPoint))
        print "Accuracy is within %.9f " % (abs(b-a)/2.0)
        if (result == 0 or ( (abs(b-a)/2.0) > 0)):
            a = midPoint
            initial = result
        else:
            b = midPoint
    print_end()

if __name__ == '__main__':
    bisection(example_f, 0, 1)