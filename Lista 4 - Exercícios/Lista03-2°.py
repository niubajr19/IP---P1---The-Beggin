tipo = str.lower(input("Insira o combustível escolhido.\n(Gasolina, Etanol e Diesel):"))
quantidade = float(input("Insira o valor desejado:"))

if tipo == "diesel":
    total=(quantidade)/(1.92)
elif tipo == "gasolina":
    total=(quantidade)/(2.53)
elif tipo == "etanol":
    total=(quantidade)/(2.09)
    if quantidade>30:
        print("Você ganhou uma troca de Óleo.")
print("Quantidade Total:","%.2f"%total,"Litros")

