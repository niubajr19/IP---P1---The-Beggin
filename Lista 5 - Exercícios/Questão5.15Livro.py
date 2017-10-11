total = 0
codigo = int(input("Digite o código do produto:"))
while codigo > 0 and codigo <=5:
    quantidade = int(input("Digite a quantidade comprada:"))
    if codigo ==1:
        valor = quantidade * 0.50
    elif codigo ==2:
        valor = quantidade * 1.00
    elif codigo ==3:
        valor = quantidade * 4.00
    elif codigo ==4:
        valor = quantidade * 7.00
    elif codigo ==5:
        valor = quantidade * 8.00
    total = total + (valor)
    print("Valor:", total, "Reais")
    codigo = int(input("Digite o código do produto:"))
else:
    print("Código inválido")




