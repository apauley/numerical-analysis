#!/usr/bin/env python

from helpers import *

def secant(func, a, b, max_steps=MaxSteps, tolerance=Tolerance):
    print "Using secant method to solve %s\n" % func.__doc__
    if abs(func(a)) < abs(func(b)):
        t = b
        b = a
        a = t
    print "a = %.9f b = %.9f" % (a,b)
    for loopCount in range(max_steps):
        p = b - (func(a) * ((a-b) / (func(a) - func(b))))
        print "Current approximation is %.9f" % p
        if (abs(func(p)) < tolerance):
            print "Root is %.9f (%d iterations)" % (p,loopCount+1)
            return
        a = b
        b = p
    print "Root find stopped at %.9f" % p

if __name__ == '__main__':
    secant(example_f, 1, 0)
