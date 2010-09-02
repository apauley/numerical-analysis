#!/usr/bin/env python

from helpers import *

def fixed_point(func, initialApproximation, max_steps=MaxSteps, tolerance=Tolerance):
    print "Using fixed point iteration to solve %s\n" % func.__doc__
    p = initialApproximation
    loopCounter = 1
    for loopCounter in range(max_steps):
        oldP = func(p)
        print "Current approximation is %.9f" % oldP
        if (abs(p - oldP) < tolerance):
            print "Approximate root is %.9f (found in %d steps)" % (oldP,int(loopCounter))
            return
        p = oldP

if __name__ == '__main__':
    fixed_point(example_f, 1)
