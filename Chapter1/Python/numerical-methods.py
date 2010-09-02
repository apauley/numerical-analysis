#!/usr/bin/env python

# This code was written by Zahir Jacobs:
# http://zahirj.wordpress.com/2009/04/04/complete-listing-of-python-code-for-selected-root-finding-methods/

import math

def swap_points(x):
	s = []
	s = x
	s.sort()
	f = s[1]
	sn = s[2]
	t = s[0]
	s[0] = f
	s[1] = sn
	s[2] = t
	return s

def sub_dict(somedict, somekeys, default=math):
		return dict([ (k, somedict.get(k, default)) for k in somekeys ])

def evaluate(func,x):
	safe_list = ['math','acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'de grees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh'] #use the list to filter the local namespace
	safe_dict = sub_dict(locals(),safe_list)
	safe_dict['abs'] = abs
	safe_dict['x']=x
	return eval(compile(func,"",'eval'),{"__builtins__":{}},safe_dict)

def mullers_method(func,a,b,r, maxSteps = 30, tolerance = 0.0001):
	print_header("Muller's method",func)
	x = [a,b,r]
	for loopCount in range(maxSteps):
		x = swap_points(x)
		y = evaluate(func,float(x[0])),evaluate(func,float(x[1])),evaluate(func,float(x[2]))
		#y = map(func,x)
		h1 = x[1]-x[0]
		h2 = x[0]-x[2]
		lam = h2/h1
		c = y[0]
		a = (lam*y[1] - y[0]*((1.0+lam))+y[2])/(lam*h1**2.0*(1+lam))
		b = (y[1] - y[0] - a*((h1)**2.0))/(h1)
		if b > 0:
			root = x[0] - ((2.0*c)/(b+ (b**2 - 4.0*a*c)**0.5))
		else:
			root = x[0] - ((2.0*c)/(b- (b**2 - 4.0*a*c)**0.5))
		print "a = %.5f b = %.5f c = %.5f root = %.5f " % (a,b,c,root)
		print "Current approximation is %.9f" % root
		if abs(evaluate(func,float(root))) > x[0]:
			x = [x[1],x[0],root]
		else:
			x = [x[2],x[0],root]
		x = swap_points(x)
	print_end()

def bisection(func, a,b,maxSteps = 30, tolerance = 0.0001):
	print_header("Bisection Method", func)
	initial = evaluate(func,float(a))
	for loopCounter in range(maxSteps):
		midPoint = a + (b-a)/2.0
		result = evaluate(func,float(midPoint))
		print "Accuracy is within %.9f " % (abs(b-a)/2.0)
		if (result == 0 or ( (abs(b-a)/2.0) > 0)):
			a = midPoint
			initial = result
		else:
			b = midPoint
	print_end()

def secant(func,a,b,maxSteps=30, tolerance = 0.0001):
	print_header("secant method",func)
	if (abs(evaluate(func,float(a))) < abs(evaluate(func,float(b)))):
		t = b
		b = a
		a = t
	print "a = %.9f b = %.9f" % (a,b)
	for loopCount in range(maxSteps):
		p = b - (evaluate(func,float(a)) * ((a-b)/(evaluate(func,float(a))-evaluate(func,float(b)))))
		print "Current approximation is %.9f" % p
		if (abs(evaluate(func,float(p))) < tolerance):
			print "Root is %.9f (%d iterations)" % (p,loopCount+1)
			return
		a = b
		b = p
	print "Root find stopped at %.9f" % p
	print_end()

def regula_falsi(func, a,b, maxSteps = 30, tolerance = 0.0001):
	print_header("regula falsi (false position)",func)
	p = 0.0
	for loopCount in range(maxSteps):
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

def print_header(t,f):
	print "\n"
	print "-" * 50
	print "Using %s to solve %s" % (t,f)
	print "-" * 50
	print "\n"

def print_end():
	print "-" * 50

def fixed_point(func, initialApproximation, maxSteps=30, tolerance=0.0001):
	print_header("fixed point iteration",func)
	p = initialApproximation
	loopCounter = 1
	for loopCounter in range(maxSteps):
		oldP = evaluate(func,float(p))
		print "Current approximation is %.9f" % oldP
		if (abs(p - oldP) < tolerance):
			print "Approximate root is %.9f (found in %d steps)" % (oldP,int(loopCounter))
			return
		p = oldP
	print_end()

def newton_raphson(func, derFunc, initialApproximation, maxSteps = 30, tolerance= 0.0001):
	print_header("newton/raphson",func + " with " + defFunc + " as derivative")
	for loopCounter in range(maxSteps):
		p = initialApproximation - (evaluate(func,float(initialApproximation))/evaluate(derFunc,float(initialApproximation)))
		if (abs(p - initialApproximation) < tolerance):
			print "Approximate root is %.9f (found in %i steps)" %(p,loopCounter)
			break
		print "Current approximation %.9f" % initialApproximation
		initialApproximation = p
	print_end()

if __name__ == '__main__':
	try:
		print "in __main__"
		mullers_method("math.cos(x) - x",0.0,0.5,1.0)
	finally:
		print "Fully done."
