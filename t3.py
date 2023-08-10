import math

alpha = -0.39887
k = 0
a = 0
b = math.pi / 2
x = (a + b)/2

def f(x):
    return math.pow(x, 2) - math.cos(x)

def phi(x):
    return x + alpha * f(x)

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

if phi(x) > x:
    x = b
else:
    x = a

while truncate(x, 8) != truncate(phi(x), 8):
    x = phi(x)
    k += 1
    print(x, phi(x))
print(k)