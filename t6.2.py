import math

T = 0.296
x0 = 1
t0 = 0
n = 1
prevx = 0

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def f(t, x):
    return t*math.exp(x**2)

def phi2(t, x, h):
    csi1 = f(t, x)
    csi2 = f(t + h, x + h * csi1)
    return (1/2) * csi1 + (1/2) * csi2

def phi3(t, x, h):
    csi1 = f(t, x)
    csi2 = f(t + 1/2 * h, x + 1/2 * h * csi1)
    csi3 = f(t + 3/4 * h, x + 3/4 * h * csi2)
    return 2/9*csi1 + 3/9*csi2 + 4/9*csi3

def phi4(t, x, h):
    csi1 = f(t, x)
    csi2 = f(t + 1/2 * h, x + 1/2 * h * csi1)
    csi3 = f(t + 1/2 * h, x + 1/2 * h * csi2)
    csi4 = f(t + h, x + h * csi3)
    return 1/6*csi1 + 2/6*csi2 + 2/6*csi3 + 1/6*csi4

def rungeKutta(t, x, n, phiR):
    h = T/n
    for _ in range(n):
        x = x + h * phiR(t, x, h)
        t += h
    return x

while True:
    h = T/n
    nextx = rungeKutta(t0, x0, n, phi2)
    n += 1
    if truncate(prevx, 8) == truncate(nextx, 8):
        print(truncate(prevx, 8), n)
        break
    prevx = nextx
    
n = 1

while True:
    h = T/n
    nextx = rungeKutta(t0, x0, n, phi3)
    n += 1
    if truncate(prevx, 8) == truncate(nextx, 8):
        print(truncate(prevx, 8), n)
        break
    prevx = nextx
    
n = 1

while True:
    h = T/n
    nextx = rungeKutta(t0, x0, n, phi4)
    n += 1
    if truncate(prevx, 8) == truncate(nextx, 8):
        print(truncate(prevx, 8), n)
        break
    prevx = nextx