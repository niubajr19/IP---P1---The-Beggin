distancia=float(input("Digite a distância a ser percorrida, em KM:"))
if distancia<=200:
    preco=(0.50*distancia)
    print("Preço da passagem: R$",'%.2f'%preco,"Reais")
else:
    preco1=(0.45*distancia)
    print("Preço da passagem: R$",'%.2f'%preco1,"Reais")
