import math

k = 0
x = 0

def f(x):
    return 1.001 * math.pow(x, 5) + 2.993 * math.pow(x,2) - 1.007 * x + 0.98

def df(x):
    return 1.001 * 5 * math.pow(x, 4) + 2.993 * 2 * x - 1.007

def alpha(x):
    return -1 / df(x)

def phi(x):
    return x + alpha(x) * f(x)

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

while truncate(x, 8) != truncate(phi(x), 8):
    x = phi(x)
    k += 1
    print(x, phi(x))
print(k)