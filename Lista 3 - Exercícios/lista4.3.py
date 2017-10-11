num1=int(input("Primeiro numero: "))
num2=int(input("Segundo numero: "))
num3=int(input("Terceiro numero: "))

if num1>num2>num3:
    print("Maior:",num1,"Menor:",num3)
elif num1>num3>num2:
    print("Maior:",num1,"Menor:",num2)
elif num2>num3>num1:
    print("Maior:",num2,"Menor:",num1)
elif num2>num1>num3:
    print("Maior:",num2,"Menor:",num3)
elif num3>num2>num1:
    print("Maior:",num3,"Menor:",num1)
elif num3>num1>num2:
    print("Maior:",num3,"Menor:",num2)

