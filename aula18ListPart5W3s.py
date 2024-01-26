txt = "METODOS 2"#--------------------------------------------------------
x = txt.center(40,"-")
print(x)

list = ["apple", "banana", "uva","morango"]
lista = [100, 50, 65, 82, 23]

#sort().
list.sort()
print("sort(). ",list)
print(" ")
list.sort(reverse = True)
print("sort() decrecente: ",list)

#Personalizar função de classificação
print(" ")
def myfunc(n):
  return abs(n - 70)

print("nova lista: ",lista)
lista.sort(key = myfunc)
print("numeros proximos ao 70: ",lista)

#Copiar uma lista copy()
print("\nCopiar uma lista: copy(). ")
mylist = lista.copy()
print("nova lista copiada: ",mylist)
print(" ")

#juntar listas
list3 = list + mylist
print("juntar lista: ( + ) ->",list3)
print(" ")
