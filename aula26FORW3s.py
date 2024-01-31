txt = "For Loops"
x = txt.center(40,"-")
print(x)

'''Um loop for é usado para iterar uma sequência (que é uma lista, uma tupla, um dicionário, um conjunto ou uma string).

Com o loop for podemos executar um conjunto de instruções, uma vez para cada item de uma lista, tupla, conjunto etc.'''


print("Imprima cada fruta em uma lista de frutas:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print()

print("Loop através de uma string 'uva': ")
for x in "uva":
  print(x)
print()


print("A declaração de ruptura:")
for x in fruits:
  print(x)
  if x == "banana":
    break
print()

#Sai do loop quando xfor "banana", mas dessa vez o break vem antes do print
print("A declaração de continuação")
for x in fruits:
  if x == "banana":
    continue
  print(x)  
print()

'''A função range()
Para percorrer um conjunto de códigos um determinado número de vezes, podemos usar a função range() , 

A função range() retorna uma sequência de números, começando em 0 por padrão, e incrementando em 1 (por padrão), e termina em um número especificado.'''

print("A função range(6):")
for i in range(6):
  print("index[",i,"]")

print("\nUsando o parâmetro inicial:")
for i in range(1,7):
  print("-[",i,"]")

'''A função range() tem como padrão incrementar a sequência em 1, porém é possível especificar o valor do incremento adicionando um terceiro parâmetro: range(2, 30, 3 ) :'''

print("\né possível especificar o valor do incremento adicionando um terceiro parâmetro:")
for x in range(1,11,2):
  print("[",x,"]")


print("\nMais em For Loop: ")
for x in range(6):
  print(x)
else:
  print("Finally finished!\n")


print("Loops aninhados:")
adj = ["red", "big", "tasty"]

for x in adj:
  for y in fruits:
    print(x," - ", y)
print()

print("A declaração de aprovação 'pass'")
for x in [0, 1, 2]:
  pass
print()