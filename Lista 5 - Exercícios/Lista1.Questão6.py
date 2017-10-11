x = 0
while x==0:
    pergunta=str.lower(input("Gostaria de executar o programa?\n(Sim,Não):"))
    if pergunta == 'sim':
      a = int(input("Digite um número:"))
      b = int(input("Digite outro número:"))

      if a>0 and b>0:
        resultado = a + b
        valor = a * b
        print("Valor da soma:",resultado,"\nValor da multiplicação:",valor)

      else:
        valordiv = (a + b) // 2
        print("Valor da média:",valordiv)

    else:
        print("Obrigado por usar este programa!*--*")
        break

