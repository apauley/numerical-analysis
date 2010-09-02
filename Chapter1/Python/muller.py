#!/usr/bin/env python

from helpers import *

def mullers_method(func, a, b, r, max_steps=MaxSteps):
    print_header("Muller's method", func)
    x = [a,b,r]
    for loopCount in range(max_steps):
        x = swap_points(x)
        y = evaluate(func,float(x[0])),evaluate(func,float(x[1])),evaluate(func,float(x[2]))
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

if __name__ == '__main__':
    mullers_method(example_f, 0.0, 0.5, 1.0)
