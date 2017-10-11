divida = float(input("Insira o valor da dívida:"))
juros = float(input("Insira o juros mensal:"))
valorpago = float(input("Insira o valor a ser pago mensalmente:"))
mes = 1
saldo = divida
jurosp = 0
while saldo > valorpago:
    juros = saldo * juros / 100
    saldo = saldo + juros - valorpago
    jurosp = jurosp + juros
    print("Saldo(dívida)",mes,"é de :",saldo)
    mes += 1

