import math
a = float(input("Insura um número para A: "))
b = float(input("Insira um número para B: "))
c = float(input("Insira um número para C: "))
delta = (b**2) - (4*a*c)
delta = math.sqrt(delta)
x1 = (-b+delta)/ 2*a
x2 = (-b-delta) /2*a
print(x1)
print(x2)