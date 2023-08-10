import math

a = -1.4
b = 2.8
n = 3
prev_n =2

def f(x):
    return math.e**(-x**2)

def S(n):
    h = (b-a)/(2*n)
    sum = f(a) + f(b)
    for i in range(1, 2*n):
        yi = 2 * f(a + (i * h))
        if i % 2 == 1:
            yi *= 2
        sum += yi
    return (h/3) * sum

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

while True:
    print(S(n))
    if truncate(S(n), 8) == truncate(S(prev_n), 8):
        print(S(n), n)
        break
    else:
        prev_n = n
        n += 1
        