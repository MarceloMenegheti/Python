
txt = "TUPLA 2"#--------------------------------------------------------
x = txt.center(40,"-")
print(x)

'''
Mas há uma solução alternativa. Você pode converter a tupla em uma lista,
alterar a lista e converter a lista novamente em uma tupla.'''

tupla1 = ("apple", "banana", "cherry")

print("imprimindo a tupla: ",tupla1)
print("\talterando uma tupla \n1 - °passo Verificação: ",type(tupla1))

aux = list(tupla1)
print("\n2° - passo transformar em lista: ",type(aux))
aux[0] = "laranja"

print("\n3° - passo alterar na lista: ",type(aux))
print("\n\talterando 'apple' para 'laranja': ",aux)
print(" ")

tupla1 = tuple(aux)
print("4° - passo transformar em lista em tupla: ",type(tupla1))
print("\n\timprimir tupla modificada: ",tupla1)
print(" ")

#descompactar uma tupla
(primeira,segunda,terceira) = tupla1
print("imprimindo a tupla: ",tupla1)

print("\ndesconpactando uma tupla: ")
print(primeira)
print(segunda)
print(terceira)

print("")
print("laço de repetição na tupla: while")
#loop tupla
i = 0
while i < len(tupla1):
  print(i,tupla1[i])
  i = i + 1