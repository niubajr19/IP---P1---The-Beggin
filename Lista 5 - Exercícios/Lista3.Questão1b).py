#O programa estava não estava executando mais de uma vez, deve-se colocar um limite de 30 vezes. O print não estava imprimindo o que deveria ser impresso(qtdePositivos). E o loop, para ser efetuado, a variavel número deve ser colocada depois do while. Segue o correto:#
cont = 0
qtdePositivos = 0
while (cont <= 30):
  numero = int(input())
  if (numero >= 0):
     qtdePositivos = qtdePositivos + 1
     cont = cont + 1
print(cont,qtdePositivos)