#!/usr/bin/env python

from helpers import *

def regula_falsi(func, a, b, max_steps=MaxSteps, tolerance=Tolerance):
    print_header("regula falsi (false position)",func)
    p = 0.0
    for loopCount in range(max_steps):
        p = b - (evaluate(func,float(b)) * ((a-b)/(evaluate(func,float(a))-evaluate(func,float(b)))))
        print "Current approximation is %.9f" % p
        if (math.copysign(evaluate(func,float(a)),evaluate(func,float(b))) != evaluate(func,float(a))):
            b = p
        else:
            a = p
        if (abs(evaluate(func,float(p))) < tolerance):
            print "Root is %.9f (%d iterations)" % (p,int(loopCount))
            return
    print "Root find cancelled at %.9f" % p
    print_end()

if __name__ == '__main__':
    regula_falsi(example_f, 0, 1)
