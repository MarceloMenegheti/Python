txt = "LOOPS"#--------------------------------------------------------
x = txt.center(40,"-")
print(x)

print("imprimindo cada elemento da lista: ")
list = ["apple", "banana", "cereja"]
for x in list:
  print(x)
print(" ")


#referindo-se ao seu número de índice
print("imprimindo cada elemento da lista com indice: ")
for i in range(len(list)):
  print("list[",i,"] - ",list[i])
print(" ")

#Usando um loop while
print("utilizando While Loop: ")
j = 0
while j < len(list):
    print(j,list[j])
    j+=1
print(" ")


#Loop usando compreensão de lista
print("Um pequeno for loop manual: ")
[print(x) for x in list]
print(" ")

#Compreensão de lista
print("se tiver a letra 'a' salva em outra lista vazia e imprime:")
newlist = []#nova lista

for x in list:
  if "a" in x:
    newlist.append(x)
print(newlist)

