txt = "TUPLA"#--------------------------------------------------------
x = txt.center(40,"-")
print(x)

#Tuplas são usadas para armazenar vários itens em uma única variável.
mytuple = ("apple", "banana", "cherry")
print("minha tupla: ",mytuple)

#Encomendado
'''Quando dizemos que as tuplas são ordenadas, significa que os itens 
têm uma ordem definida e essa ordem não mudará.'''

#imutaveis
''' As tuplas são imutáveis, o que significa que não podemos alterar,
adicionar ou remover itens após a criação da tupla. '''

print("o tamanho da tupla: ",len(mytuple))
print(" ")

#Crie tupla com um item
'''Para criar uma tupla com apenas um item, você deve adicionar uma 
vírgula após o item, caso contrário o Python não o reconhecerá como
uma tupla.'''

#uma tupla
thistuple = ("apple",)
print(thistuple,type(thistuple)," -\t Uma tupla")


#NOT a tuple
thisNottuple = ("apple")
print(thisNottuple,type(thisNottuple)," -\t\t Não é uma tupla")
print(" ")

#Itens de tupla
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print("tipos de tupla 'string': ",tuple1)
print("tipos de tupla 'int': ",tuple2)
print("tipos de tupla 'bolean': ",tuple3)
print(" ")

#Uma tupla com strings, números inteiros e valores booleanos:
tuple4 = ("abc", 34, True, 40, "male")
print("tupla com str, int, bool:",tuple4)

#O construtor tupla()
print("\ncriando uma nova tupla: ")
novatupla = tuple(("relogio","bolsa","tenis"))
print(type(novatupla))

