#Python tem dois comandos de loop primitivos:
#while loops
#for loops
txt = "WHILE"
x = txt.center(40,"-")
print(x)

'''Com o loop while podemos executar um conjunto de instruções, desde que uma condição seja verdadeira.'''

i = 1
while i < 6:
    print(i)
    i += 1#embre-se de incrementar i, caso contrário o loop continuará para sempre

#outra maneira
j = 1
print("\nA declaração de ruptura:")
while j < 6:
  print(j)
  if j == 3:
    break
  j += 1
print()

print("A declaração de continuação:")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


print()
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("eu não tenho menos que 6\n")