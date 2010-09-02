#!/usr/bin/env python

# This code was originally written by Zahir Jacobs:
# http://zahirj.wordpress.com/2009/04/04/complete-listing-of-python-code-for-selected-root-finding-methods/

from helpers import *

def secant(func, a, b, max_steps=MaxSteps, tolerance=Tolerance):
	print_header("secant method",func)
	if (abs(evaluate(func,float(a))) < abs(evaluate(func,float(b)))):
		t = b
		b = a
		a = t
	print "a = %.9f b = %.9f" % (a,b)
	for loopCount in range(max_steps):
		p = b - (evaluate(func,float(a)) * ((a-b)/(evaluate(func,float(a))-evaluate(func,float(b)))))
		print "Current approximation is %.9f" % p
		if (abs(evaluate(func,float(p))) < tolerance):
			print "Root is %.9f (%d iterations)" % (p,loopCount+1)
			return
		a = b
		b = p
	print "Root find stopped at %.9f" % p
	print_end()

if __name__ == '__main__':
    secant(example_f, 1, 0)
