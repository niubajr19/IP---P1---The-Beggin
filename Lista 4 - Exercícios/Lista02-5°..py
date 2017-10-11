valorProduto = float(input("Digite o valor do produto:"))
formaDePagamento = str.lower(input("Digite a forma de pagamento:"))

if formaDePagamento == "cheque":
    print("Preço Total:",valorProduto,"Reais")
elif formaDePagamento == "dinheiro" and valorProduto>=100:
    desconto = valorProduto*0.10
    valorTotal = (desconto)+(valorProduto)
elif formaDePagamento == "dinheiro" and valorProduto<100:
    print("Preço Total:",valorProduto,"Reais")
else:
    print("Forma de Pagamento inválida")
print("Preço Total:",valorTotal,"Reais")

