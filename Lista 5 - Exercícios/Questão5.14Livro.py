x = 0
y = 0
while True:
    n = int(input("Digite um número maior que zero:"))
    if n==0:
        break
    x = x + n
    y = y + 1
print("Quantidade de números digitados:", y)
print("Soma dos números recebidos:", x)
print("Média:%.2f"% (x/y))