#É recomendavel a redução do comando "print" para um só. Também, a substituição dos 3 "if's" por if, elif e else. Segue o correto:#
a=int(input())
b=int(input())
c=int(input())
if (a>b) and (a>c):
    resultado=a
elif(b>a) and (b>c):
    resultado=b
else:
    resultado=c
print(resultado)