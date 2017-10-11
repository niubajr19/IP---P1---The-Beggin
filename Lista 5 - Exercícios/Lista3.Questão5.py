x = 0
vacina = 0
while x == 0:
   quest = str.lower(input("Deseja informar uma idade(Sim,Não)?"))
   if quest == 'sim':
      idade = int(input("Insira a idade:"))
      if idade>=3 and idade<=6:
         vacina += 1

      else:
          print("Idade inválida")

   else:
       print("Obrigado por utilizar esse programa!<3")
       print("Quantidade de vacinas:",vacina)


