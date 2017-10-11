N = int(input("Insira um valor: "))
if N>0 and N<1000000:
    notasde100 = (N//100)
    notasde50 = (N%100)//50
    notasde20 = (N%100)%50//20
    notasde10 = ((N%100)%50)%20//10
    notasde5 = ((N%100)%50)%20%10//5
    notasde2 = ((N%100)%50)%20%10%5//2
    notasde1 = ((N%100)%50)%20%10%5%2//1
print("Nota(s) de 100:",notasde100,'\n',"Nota(s) de 50:",notasde50,'\n',"Nota(s) de 20:",notasde20,'\n', "Nota(s) de 10:",notasde10,'\n', "Nota(s) de 5:",notasde5,'\n'"Nota(s) de 2:",notasde2,'\n',"Nota(s) de 1:",notasde1)