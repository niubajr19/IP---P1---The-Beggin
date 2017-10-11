a = int(input("Insira a quantidade de cigarros fumados por dia:"))
b = int(input("Insira a quantidade de anos em que já fumou:"))

cigarrt = (a*30*12)*b
minutosporc = cigarrt*10

segundos = (minutosporc*60)
dias = (segundos/86400)
print("O total de vida perdida é de:",dias,"Dias.")