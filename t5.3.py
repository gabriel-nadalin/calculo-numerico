import math

g0g0 = 2
g1g1 = 2/3
g2g2 = 8/45
g3g3 = 8/175
g4g4 = 128/11025

def fg0x(x):
    return math.exp(-x**2) * 1

def fg1x(x):
    return math.exp(-x**2) * x

def fg2x(x):
    return math.exp(-x**2) * (x**2 - 1/3)

def fg3x(x):
    return math.exp(-x**2) * (x**3 - 3/5 * x)

def fg4x(x):
    return math.exp(-x**2) * (x**4 - 6/7 * x**2 + 3/35)

def simpson(a, b, f, lim):
    # a = limite inferior
    # b = limite superior
    # f = função
    # lim = limite de iterações
    # r = resultado

    # print("Método de Simpson")
    r = 0
    for i in range(1, lim+1):
        n2 = 2 * i
        h = (b - a) / (n2)

        t = []
        for j in range (1,n2+2):
          t.append(a + (j-1)*h)

        s = 0
        for k in range(1, n2):
            if k % 2 == 0:
                s = 2 * f(t[k]) + s
            else:
                s = 4 * f(t[k]) + s

        #print(len(t))
        #print(n2)
        soma1 = f(t[0])
        soma2 = f(t[n2])
        soma = soma1 + s + soma2

        #r = (h / 3) * soma
        r = (h*soma) / 3

    return r


a = -1
b = 1

limite = 38

fg0 = simpson(a, b, fg0x, limite)
#fg1 = simpson(a, b, fg1x, limite)
fg2 = simpson(a, b, fg2x, limite)
#fg3 = simpson(a, b, fg3x, limite)
fg4 = simpson(a, b, fg4x, limite)
print("<f,g0> = {:.24f}, <f,g2> = {:.24f}, <f,g4> = {:.24f}".format(fg0, fg2, fg4))

# Cálculo dos coeficientes b0, b2 e b4
b0 = fg0 / g0g0
b2 = fg2 / g2g2
b4 = fg4 / g4g4

# Cálculo dos coeficientes a0, a2 e a4
a0 = b0 - (b2 * (1/3)) + (b4 * (3/35))
a2 = b2 - ((6/7) * b4)
a4 = b4


print("<f,g0> = {:.24f}, <f,g2> = {:.24f}, <f,g4> = {:.24f}".format(a0, a2, a4))


