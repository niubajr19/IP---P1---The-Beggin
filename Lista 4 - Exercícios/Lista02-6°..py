valorProduto = float(input("Digite o valor do produto:"))
formaDePagamento = str.lower(input("Digite a forma de pagamento:"))
if formaDePagamento=="cartão":
   a = str.lower(input("Digite a forma de pagamento do cartão:(débito) ou (crédito):"))
   if a =="crédito":
      quantidadeDeParcelas = int(input("Digite a quantidade de parcelas desejadas:"))
      if quantidadeDeParcelas==1:
        print("Preço Total:",valorProduto,"Reais")
        valorTotal=valorProduto
      elif quantidadeDeParcelas==2:
        print("Preço Total:2 parcelas de",valorProduto/2,"Reais")
        valorTotal=valorProduto
      elif quantidadeDeParcelas==3:
        print("Preço Total:3 parcelas de",valorProduto/3,"Reais")
        valorTotal=valorProduto
      else:
        print("Quantidade não autorizada de parcelas")
   elif a == "débito":
      valorTotal=valorProduto
elif formaDePagamento == "cheque":
    print("Preço Total:",valorProduto,"Reais")
elif formaDePagamento == "dinheiro" and valorProduto>=100:
    desconto = valorProduto*0.10
    valorTotal = (valorProduto)-(desconto)
elif formaDePagamento == "dinheiro" and valorProduto<100:
    valorTotal=(valorProduto)
else:
    print("Forma de Pagamento inválida")
print("Preço Total:",valorTotal,"Reais")

