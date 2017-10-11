cont = 0
qtdeposit = 0
pares = 0
while cont<30:
    numero = int(input("Insira um número:"))
    if numero%2==0:
        pares+=1

    elif numero%2!=0 and numero>=0:
        qtdeposit+=1
    cont+=1
print(pares,"número(s)par(es)")
print(qtdeposit,"número(s)positivo(s)")
