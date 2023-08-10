import math
from decimal import *

getcontext().prec = 4

def GaussJordan(M):
    nLin = len(M)
    nCol = len(M[0])
    if nCol != nLin + 1:
        return "dimensao da matriz incompativel"
    MM = []
    xx = []
    for i in range(nLin):
        xx.append(0)
        linha = []
        for j in range(nCol):
            linha.append(Decimal(M[i][j]) + 0)
        MM.append(linha)
        
    for i in range(nLin):
        pivo = i
        for j in range(i+1, nLin):
            if abs(MM[pivo][i]) < abs(MM[j][i]):
                pivo = j
        MM[i], MM[pivo] = MM[pivo], MM[i]
        
        for j in range(i+1, nLin):
            MM[j][i] = MM[j][i] / MM[i][i]
            for k in range(i+1, nCol):
                MM[j][k] -= MM[j][i]*MM[i][k]
                
    for i in range(nLin-1, -1, -1):
        xx[i] = MM[i][nCol-1]
        for j in range(nLin-1, i, -1):
            xx[i] -= MM[i][j] * xx[j]
        xx[i] /= MM[i][i]
    return xx

def combinar(A, b):
    Ab = []
    for i in A:
        Ab.append(i.copy())
        Ab[A.index(i)].append(b[A.index(i)])
    return Ab

def mult(A, B):
    res = []
    for i in A:
        res.append(0)
        for j in i:
            res[A.index(i)] += Decimal(j) * B[i.index(j)]
    return res

def refinar(A, b, X):
    r = []
    res = []
    for i in mult(A, X):
        r[A.index(i)] = b[A.index(i)] - i
    y = GaussJordan(combinar(A, r))
    for i in X:
        res[X.index(i)] = i + y[X.index(i)]
    return res

A = [[-7.857, -4.857, 6.571, -9.143, -0.1429, -9.429, -5.571, -12.14, -6.714, 15.71],
     [12, 11.14, 10.71, -2.429, -1.429, -4.857, -1, -0.8571, -3.143, 13.71],
     [-7.429, -10.43, 3.286, 6, 3.286, -10.86, -11.71, 1.714, -2.429, -9.143],
     [-9.571, 12.14, -6.857, 6.143, 6.143, 10.43, -11.71, -10.43, 8.286, -24.71],
     [10.71, -0.1429, -1.429, -13.29, -7.714, -13.14, -13, -2.286, -3.429, 26.29],
     [-0.2857, -3.714, -2.286, 8.714, -3.857, -4.571, 1.571, -2.714, -11, 18.86],
     [12.57, 8.714, 1.286, -9, -12, -3.857, -4.571, -7.571, -9.857, 24.71],
     [7.143, 4.286, 1.571, 2.857, -8, 12.57, -2.143, -1.429, 11.14, -0.5714],
     [11.57, -3.143, -1.429, 11.29, 10, 6.429, 3, 2.143, 9, 19.71]]

A = [[13.16,  4.305, 9.101, -1.171, 9.314, -7.397, 0.7217, 9.914, -3.042],
[12.40, 5.190, 8.383, -0.5461, 8.474, -6.693, -0.1723, 10.77, -3.876],
[13.25, 4.408, 9.166, -1.196, 9.218, -7.317, 0.7847, 9.964, -2.930],
[12.40, 5.109, 8.234, -0.4721, 8.509, -6.601, -0.1813, 10.74, -3.731],
[13.18, 4.407, 9.126, -1.270, 9.166, -7.401, 0.7307, 9.954, -2.951],
[12.47, 5.195, 8.284, -0.4121, 8.412, -6.654, -0.0553, 10.61, -3.740],
[13.20, 4.364, 9.044, -1.180, 9.331, -7.346, 0.7457, 9.835, -3.057],
[12.43, 5.180, 8.398, -0.4581, 8.544, -6.550, -0.0373, 10.78, -3.883],
[13.30, 4.277, 9.021, -1.165, 9.176, -7.359, 0.7057, 9.883, -3.036]]

b = [-3.457, -2.811, -3.637, -2.780, -3.621, -2.809, -3.453, -2.658, -3.623]

X = GaussJordan(combinar(A, b))
X1 = refinar(A, b, X)
for i in X1:
    print(i)