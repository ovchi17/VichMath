import math
import numpy as np
import functools

def chebyshevNodes(n):
    ms = []
    for k in range(1, n + 1):
        zn = math.cos((2 * k - 1) * math.pi / (2 * n))
        ms.append(zn)
    return ms

def test():
    if (newtonInterpolation([0, 1, 2, 3, 4], [1, 2, 3, 4, 5], 2.5) == 3.5):
        print("test1 passed")
    else:
        print("test1 failed")
    if (newtonInterpolation([0, 1, 2, 3, 4], [0, 1, 4, 9, 16], 2.5) == 6.25):
        print("test2 passed")
    else:
        print("test2 failed")
    if (newtonInterpolation([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], 2.5) == 15.625):
        print("test3 passed")
    else:
        print("test3 failed")
    if (newtonInterpolation([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4], -1.5) == 2.25):
        print("test4 passed")
    else:
        print("test4 failed")
    if (newtonInterpolation([100, 200, 300, 400, 500], [1, 2, 3, 4, 5], 350) == 3.5):
        print("test5 passed")
    else:
        print("test5 failed")

def newtonInterpolation(x, y, xTarget):
    n = len(x)
    table = []
    for j in range(n):
        table.append([y[j]])
    for i in range(1, n):
        for j in range(n - i):
            table[j].append((table[j + 1][i - 1] - table[j][i - 1]) / (x[j + i] - x[j]))
    result = table[0][0]
    for i in range(1, n):
        p = 1
        for j in range(i):
            p *= (xTarget - x[j])
        result += table[0][i] * p

    return result

    
    
#xVal = chebyshevNodes(len(list(map(int, input().split(' ')))))
#yVal = list(map(int, input().split(' ')))
#x = int(input())

#toPrint = newtonInterpolation(xVal, yVal, x)
#print(toPrint)

test()