a=float(input("Digite seu Salário:"))
if a>1000:
    imposto1=(a*17/100)
    print("Você pagará 17% de imposto, que equivale a:R$ ",'%.2f'%imposto1)
else:
    imposto2=(a*8/100)
    print("Você pagará 8% de imposto, equivalente a:R$ ",'%.2f'%imposto2,"Reais")