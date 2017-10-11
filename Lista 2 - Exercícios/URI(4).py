import math
A = float(input("Digite um número: "))
B = float(input("Digite outro número: "))
C = float(input("Digite mais outro número: "))
delta = B**2-4*A*C
if (A==0)or delta<0:
    print("Impossível Calcular")
else:
    Rdelta=math.sqrt(delta)
    x1 = (-B+Rdelta)/(2*A)
    x2 = (-B-Rdelta)/(2*A)
    print("X':{}, X'':{}".format("%0.5f" % x1, "%0.5f" % x2))
