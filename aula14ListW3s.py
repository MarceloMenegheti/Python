l = "List"
a = l.center(40,"-")
print(a)
print(" ")

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print("tamanho da lista: ",len(thislist))
print(" ")

#Itens de lista - Tipos de dados
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print("lista com diferentes tipos de dados strings: ",list)
print("lista com tipos de dados int: ",list2)
print("lista com tipos de dados boleanos: ",list3)
print(" ")

#lista pode conter diferentes tipos de dados:
list4 = ["abc", 34, True, 4.0, "male"]
print("lista com diferentes tipos de dados: ",list4)
print(" ")

#Da perspectiva do Python, as listas são definidas como objetos com o tipo de dados ‘lista’:
print(type(list1))
print(" ")
print("Usando o list() construtor para fazer uma lista: ")
list5 = list(("manga","abacaxi","acerola","uva"))
print(list5)
