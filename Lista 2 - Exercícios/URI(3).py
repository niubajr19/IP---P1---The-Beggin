N = int(input("Insira a duração em segundos do evento: "))
horas = (N//3600)
minutos = (N%3600)//60
segundos = (N%3600)%60
print("Horas: ",horas,'\n',"Minutos: ",minutos,'\n', "Segundos: ",segundos,'\n')