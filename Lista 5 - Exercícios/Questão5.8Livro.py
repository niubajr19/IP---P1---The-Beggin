m = int(input("Digite o primeiro número:"))
n = int(input("Digite o segundo número:"))
cont = 0
a = 0

while(cont != n):
     a+=m
     cont=cont+1
print("{}x{}:{}".format(m,n,a))