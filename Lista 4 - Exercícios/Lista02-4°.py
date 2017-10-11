num1 = int(input("Insira um número:"))
if num1%2!=0:
    print(num1,"é impar.")
else:
    print(num1,"não é um número impar")
if num1%3==0:
    print(num1,"é um múltiplo de 3.")
else:
    print(num1,"não é múltiplo de 3.")
if num1%102 and 102%num1==0:
    print(num1,"é divisor de 102")
else:
    print(num1,"não é divisor de 102")