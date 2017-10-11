num1=int(input("Insira o primeiro número:"))
num2=int(input("Insira o segundo número:"))
num3=int(input("Insira o terceiro número:"))
if num1>num2>num3:
    maior=num1
elif num2>num3>num1:
    maior=num2
else:
    maior=num3
print("O número maior é:",maior)