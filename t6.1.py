import math

a = 0
b = 0.6
h = 0.1
prev_y = 1

def y_prime(x, y):
    return 0.12*y**2-0.93*math.sin(x)

for i in range(a, int(10*b), int(10*h)):
    yi = prev_y + h*y_prime(a+i*h, prev_y)
    prev_y = yi
    print("{:.12f}".format(yi))