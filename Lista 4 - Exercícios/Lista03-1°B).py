#No caso desse programa, tem 2 erros, um  na utilização de 2 "else(s)", que no caso seria indicado substituir pelo padrao "if", "elif" e "else". E também na utilização do print 3 vezes(indicado seria reduzir a 1. Segue o correto:#
altura = float(input("Insira sua altura:"))
if (altura <= 1.40):
    altura1 = "Estatura baixa"
elif (altura < 1.65):
    altura1 = "Estatura Mediana"
else:
    altura1 = "Estatura Alta"
print(altura1)