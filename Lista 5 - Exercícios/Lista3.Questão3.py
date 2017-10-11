cont = 0
soma = 0
while cont<30:
    numero = int(input("Digite um número:"))
    if numero%3==0:
        soma = soma+numero
    cont+=1
print("Soma total dos números multiplos de 3:",soma)