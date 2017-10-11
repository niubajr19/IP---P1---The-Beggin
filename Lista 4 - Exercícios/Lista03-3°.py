quantidade= (int(input("Digite a quantidade de pessoas = ")))
pessoas = quantidade

onibusP= 42
vanP= 20
onibusPreco= 350
vanPreco= 200
onibusT = pessoas // onibusP
numpessoas = pessoas % onibusP

vansT = numpessoas // vanP
numpessoas = numpessoas % vanP

if numpessoas > 0:
    vansT += 1
print("Quantidade total de veículos:",onibusT,"Onibus e",vansT,"Van(s)")
valortotal =(int)((onibusT*onibusPreco) + (vansT*vanPreco))/pessoas
print("Valor Total:",'%.2f'%valortotal,"Reais por pessoa.")
