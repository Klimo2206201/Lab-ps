import sys
from math import *
print("enter nomer")
nomer = int(input())
if nomer == 1:
    print(" Enter x: ")
    x = float(input())
    print(" Enter a: ")
    a = float(input())
    G = 5 * ((-9) * a * a + 11 * a * x + 14 * x * x) / (15 * a * a + 49 * a * x + 24 * x * x)
    if a == 0 and x == 0:
        print("Wrong G")
    else:
        print(G)

elif nomer == 2:
    print(" Enter x: ")
    x = float(input())
    print(" Enter a: ")
    a = float(input())
    F = tan(18 * a * a + 29 * a * x + 10 * x * x);
    if F == pi / 2:
        print("Wrong F")
    else:
        print(F)

elif nomer == 3:
    print(" Enter x: ")
    x = float(input())
    print(" Enter a: ")
    a = float(input())
    Y = acos(-7 * a * a - 10 * a * x + 8 * x * x + 1);
    if Y == 1 or Y == -1:
        print("Wrong Y")
    else:
        print(Y)
else:
    print("function error")
    sys.exit 
