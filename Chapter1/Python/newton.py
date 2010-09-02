#!/usr/bin/env python

import math
from helpers import *

def newton_raphson(func, derFunc, initialApproximation, max_steps=MaxSteps, tolerance=Tolerance):
    print_header("newton/raphson",func + " with " + defFunc + " as derivative")
    for loopCounter in range(max_steps):
        p = initialApproximation - (evaluate(func,float(initialApproximation))/evaluate(derFunc,float(initialApproximation)))
        if (abs(p - initialApproximation) < tolerance):
            print "Approximate root is %.9f (found in %i steps)" %(p,loopCounter)
            break
        print "Current approximation %.9f" % initialApproximation
        initialApproximation = p
    print_end()
