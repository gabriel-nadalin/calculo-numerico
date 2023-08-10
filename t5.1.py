import math

a = 1
b = 2.2
n = 3
prev_n =2

def f(x):
    return (math.e**x)/x

def T(n):
    h = (b-a)/n
    sum = f(a) + f(b)
    for i in range(1, n):
        sum += 2 * f(a + (i * h))
    return (h/2) * sum

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

while True:
    print(T(n))
    if truncate(T(n), 8) == truncate(T(prev_n), 8):
        print(T(n), n)
        break
    else:
        prev_n = n
        n += 1
        