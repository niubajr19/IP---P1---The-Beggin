a = float(input("Insira o valor da casa:"))
b = float(input("Insira seu salário:"))
c = int(input("Insira a quantidade de anos a pagar:"))
prestação = (a//c)//12
if (b*30/100)< prestação:
    print("O valor da prestação mensal nao pode ser superior a 30% de seu salário.")
else:
    print("A prestação mensal, será no valor de:R$",prestação,"Reais")
