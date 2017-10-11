#O programa não está correto, mas também não está certo. A opção de utilizar 2 ifs é errada. O certo seria a utilização do padrão:If,Elif,Else. Segue o correto:#
rendaAnual = float(input("Insira sua renda anual:"))
if(rendaAnual <= 12000):
    imposto=0
elif(rendaAnual > 60000):
    imposto = rendaAnual*0.07
else:
    imposto = rendaAnual*0.03
print(imposto)
