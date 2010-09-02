#!/usr/bin/env python

from helpers import *

def newton_raphson(func, derFunc, initialApproximation, max_steps=MaxSteps, tolerance=Tolerance):
    print "Using Newton/Raphson to solve %s" % func.__doc__
    print "Derivative used: %s\n" % func.__doc__

    for loopCounter in range(max_steps):
        p = initialApproximation - func(initialApproximation)/derFunc(initialApproximation)
        if (abs(p - initialApproximation) < tolerance):
            print "Approximate root is %.9f (found in %i steps)" %(p,loopCounter)
            break
        print "Current approximation %.9f" % initialApproximation
        initialApproximation = p

if __name__ == '__main__':
    newton_raphson(example_f, example_deriv, 0)
