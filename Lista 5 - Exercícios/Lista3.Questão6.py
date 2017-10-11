filhos = int(input("Digite a quantidade de filhos:"))
cont = 0
soma = 1
while filhos >= 0:
    cont+=1
    soma = soma + filhos
    media = soma//cont
    filhos = int(input("Digite a quantidade de filhos:"))
print(media)