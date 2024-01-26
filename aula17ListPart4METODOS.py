txt = "METODOS"#--------------------------------------------------------
x = txt.center(40,"-")
print(x)

list = ["apple", "banana", "uva","morango"]
list2 = ["acerola","laranja"]

#inserir itens metodo "insert()."
list.insert(3, "melancia")
print("inserindo novos itens: ",list)
print(" ")

#Anexar itens "append()."
list.append("laranja")
print("anexando um item: ",list)
print(" ")

#Adicione os elementos de list2 para list
list2 = ["banana","acerola"]
list.extend(list2)
print("estendendo a lista: ",list)
print(" ")

#remover itens
list.remove("acerola")
print("removendo 'acerola': ",list)
print(" ")

#Remover índice especificado
list.pop(1)#Se não especificar o índice, o método removerá o último item.
print("O método pop(). remove o índice especificado: ",list)
print(" ")


#Limpe a lista
print("A segunda lista: ",list2)
list2.clear()
print("limpando a list2: ",list2)
print(" ")

