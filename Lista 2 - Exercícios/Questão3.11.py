a = float(input("Insira o preço da mercadoria:"))
b = float(input("Insira a porcentagem de desconto:"))
desc = (a*b/100)
prect = a-(desc)
print("O valor do desconto é:R$",'%0.2'%desc)
print("Você pagará:R$",'%0.2'%prect)
