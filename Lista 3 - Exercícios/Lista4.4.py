num1 = float(input("Insira seu salário:"))
if num1 > 1250:
    salario = num1 + (num1 * 10 / 100)
    print("Você obteve um aumento de 10%, seu salário total é:R$", salario)
else:
    salario1 = num1 + (num1 * 15 / 100)
    print("Você obteve um aumento de 15%, seu saalário total é:R$", salario1)

