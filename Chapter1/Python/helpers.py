import math

MaxSteps = 30
Tolerance = 0.0001

def example_f(x):
    "3x + sin x - e^x"
    return (3*x) + math.sin(x) - math.exp(x)

def example_deriv(x):
    "3 + cos x - e^x"
    return 3 + math.cos(x) - math.exp(x)

def print_header(t, f):
    print "\n"
    print "-" * 50
    print "Using %s to solve %s" % (t,f)
    print "-" * 50
    print "\n"

def print_end():
    print "-" * 50
