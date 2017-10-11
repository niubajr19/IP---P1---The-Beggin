setor = str.lower(input("Digite o setor escolhido.\n(arquibancada,cadeira,plateia VIP:"))

if setor == "plateia vip":
    ingresso = str.lower(input("Digite o tipo de ingresso.\n(Inteira, meia):"))
    if ingresso == "inteira":
        preco = 350+(350*0.05)
    else:
        print("Tipo de ingresso inválido")
        preco=0
elif setor == "cadeira":
    ingresso = str.lower(input("Digite o tipo de ingresso.\n(Inteira, meia):"))
    if ingresso == "inteira":
        preco = 200+(200*0.05)
    elif ingresso == "meia":
        preco = (200/2) + (200*0.05)
    else:
        ("Tipo de ingresso inválido")
elif setor == "arquibancada":
    ingresso = str.lower(input("Digite o tipo de ingresso.\n(Inteira, meia):"))
    if ingresso == "inteira":
        preco = 100+(100*0.05)
    elif ingresso == "meia":
        preco = (100/2) + (100*0.05)
    else:
        print("Tipo de ingrasso inválido")
else:
    print("Setor Inválido")
    preco = 0
print("Preço total:",'%.2f'%preco,"Reais")





