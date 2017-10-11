deposito = float(input("Digitie o depósito inicial: "))
taxa = float(input("Digite a taxa de juros:"))
mensal = float(input("Digite seu depósito mensal:"))
mes = 1
saldo = deposito
while mes < 24:
    saldo = saldo + (saldo*(taxa/100))+mensal
    mes+=1
    print("Mes {}\nJuros:{}".format(mes,"%.2f"%saldo))
print("Ganho total:",deposito)