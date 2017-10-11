#O programa estava passando das 20 execuções. O if não estava especificando o valor do resto, para que assim pudesse ser efetuado o comando. Além do programa não somar. Segue o correto:#
cont = 0
while (cont<=20):
 numero = int (input())
 if (numero % 2 == 0):
  soma = soma + numero
 cont = cont + 1
print(soma)
