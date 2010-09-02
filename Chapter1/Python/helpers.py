import math

MaxSteps = 30
Tolerance = 0.0001

example_f = "(3*x) + math.sin(x) - math.exp(x)"

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

def evaluate(func, x):
    safe_list = ['math','acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'de grees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh'] #use the list to filter the local namespace
    safe_dict = sub_dict(locals(),safe_list)
    safe_dict['abs'] = abs
    safe_dict['x']=x
    return eval(compile(func,"",'eval'),{"__builtins__":{}},safe_dict)

def print_header(t, f):
    print "\n"
    print "-" * 50
    print "Using %s to solve %s" % (t,f)
    print "-" * 50
    print "\n"

def print_end():
    print "-" * 50
