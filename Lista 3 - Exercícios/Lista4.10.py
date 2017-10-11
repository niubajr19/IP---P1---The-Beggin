a = float(input("Insira a quantidade de kWh consumida:"))
b = str.lower(input("Insira a letra que corresponde ao seu tipo de instalação.\n(R-Residências, I-Indústrias e C-Comércios."))
if b != "r" or "i" or "c":
    print("Instalação desconhecida, digite corretamente.(R,I ou C)")
if b=="c":
    if a>1000:
        custo=0.60
    else:
        custo=0.55
    custo_total=(a*custo)
elif b=="i":
    if a>5000:
        custo=0.60
    else:
        custo=0.55
    custo_total=(a*custo)
elif b=="r":
    if a>500:
        custo=0.65
    else:
        custo=0.40
    custo_total=(a*custo)
print("Preço total:R$",custo_total,"Reais")



