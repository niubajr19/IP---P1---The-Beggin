
m = int(input("Digite o primeiro número:"))
n = int(input("Digite o segundo número:"))
cont = 0
a = m

while n <= a:
     if n!=0:
        a -= n
        cont +=1
        print("Resultado:",cont,"Resto:",a)
     else:
       print("Divisão impossível de realizar.")



