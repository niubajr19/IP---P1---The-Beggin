a = 12345
notasde100 = (a//100)
notasde50 = ((a%100)//50)
notasde10 = (a%100%50)//10
notasde5 = (a%100%50%10)//5
notasde1 = (a%100%50%10%5)//1
print("Notas de cem:",notasde100,'\n', "Notas de cinquenta: ",notasde50,'\n', "Notas de cinco:",notasde5,'\n', "Notas de um: ", notasde1)
