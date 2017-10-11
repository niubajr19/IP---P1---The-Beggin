a = float(input("Digite um número:"))
b = float(input("Digite outro número:"))
c = int(input("Qual operação deseja realizar(1 a 4)?\n(Soma=1, multiplicação=2, divisão=3 ou subtração=4):"))
if c>4:
    print("Impossível calcular, insira um número de 1 a 4.")
elif c==1:
    resultado1=(a+b)
    print("Resultado:",resultado1)
elif c==4:
    resultado2=(a-b)
    print("Resultado:",resultado2)
elif c==3:
    resultado3=(a/b)
    print("Resultado:",resultado3)
else:
    resultado4=(a*b)
    print("Resultado:",resultado4)


