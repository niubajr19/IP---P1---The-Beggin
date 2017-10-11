x = 0
cont = 0
soma = 0
y = 0
while x!=100:
    x=int(input("Insira um número:"))
    if x%2 == 0 and x != 100:
        soma = soma+x
        cont+=1
        y = soma//cont
print(y)
