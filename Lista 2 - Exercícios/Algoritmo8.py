idade = int(input("Insira sua idade, definida em dias: "))
anos = (idade//365)
meses = (idade%365)//12
dias = (idade%365)%12
print("Anos:",anos,'\n'"Meses:",meses,'\n',"Dias:",dias)