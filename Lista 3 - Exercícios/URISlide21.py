a=float(input("Insira o número do item:"))
b=float(input("Insira a quantidade do item:"))

if a>5:
    print("Impossível calcular, insira um número de 1 a 5.")
elif a==5:
    preco=(b*1.50)
elif a==4:
    preco=(b*2.0)
elif a==3:
    preco=(b*5.00)
elif a==2:
    preco=(b*4.50)
else:
    preco=(b*4.00)
print("Preço total:",'%.2f'%preco,"Reais")
