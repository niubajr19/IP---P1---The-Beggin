x = 0
while x<3:
    a = int(input("Digite um número:"))
    b = int(input("Digite outro número:"))
    if a>0 and b>0:
     resultado = a + b
     valor = a * b
     print("Valor da soma:",resultado,"\nValor da multiplicação:",valor)

    else:
       valordiv = (a + b) // 2
       print("Valor da média:",valordiv)
    x+=1

