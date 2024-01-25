
#declarando uma variavel String
txt = "hoje o dia esta estranho!"
print("frase do dia: ",txt)
print(" ")


#Verifique a sequência no print.
print("se \'perfeito\' estiver em \"txt\": ","perfeito" in txt)
print(" ")


#condiconais

#primeiro bloco if-else
if "perfeito" in txt:
    print("YES, 'perfeito' esta no arquivo no txt")
else:
   print("'perfeito' Não encontrado no arquivo no txt")
print(" ")

#segundo bloco if-else
if "hoje" not in txt:
  print("NO, 'hoje' is NOT present.")
else:
   print("SIM, 'hoje' esta presente no arquivo txt")
print(" ")