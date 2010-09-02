#!/usr/bin/env python

from helpers import *

def regula_falsi(func, a, b, max_steps=MaxSteps, tolerance=Tolerance):
    print "Using Regula Falsi (false position) to solve %s\n" % func.__doc__
    p = 0.0
    for loopCount in range(max_steps):
        p = b - (func(b) * ((a-b)/(func(a)-func(b))))
        print "Current approximation is %.9f" % p
        if math.copysign(func(a), func(b)) != func(a):
            b = p
        else:
            a = p
        if abs(func(p)) < tolerance:
            print "Root is %.9f (%d iterations)" % (p,int(loopCount))
            return
    print "Root find cancelled at %.9f" % p

if __name__ == '__main__':
    regula_falsi(example_f, 0, 1)
