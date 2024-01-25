

# voltando a estudar Python!!!!

# this is a comment   
"""
x = 5
y = "lemao"
print(x)
print(y)
 
""" 

# descrever o tipo de var
""""""
"""
t = 4
print(f"\nA variavel t =\'{t}\' do tipo: ",type(t))
print("\talterando o tipo da varivel \'t\' para String")
t = 'Marcelo'
print(f"A variavel t =\'{t}\' agora eh do tipo: ",type(t))



# Nomes Variaveis

myVariableName = "Luiz"      #Estojo de Camelo
my_variable_name = "Marcelo" #Caso Cobra
MyVariableName = "Vinicius"      #Caso Pascal

print('')
print(myVariableName)
print(my_variable_name)
print(MyVariableName)
"""

'''
# atribuicao de valores
""""""
p,l,k ="Laranja","Banana","Cereja"
print(p,l,k)



#atribuir multiplas variaveis
""""""
h = v = c = "Pamonha"
print(f'\na variavel h = \"{h}\", a variavel v = \"{v}\" e c = \"{c}\"')



#descompactar uma colecao

Fruits = ["maca","banana","Cereja"]
x,y,z = Fruits

print("")
print(x)
print(y)
print(z)
'''


# Variaveis Globais
"""
x = "Awesome"

def myfunc():# criando minha func
    x = "fantastic"
    print("\'Interno\' Python is " + x)

myfunc()#chamando minha func

print("\'Externo\' Python is " + x)
print("")
"""


#Palavra-Chave Global
"""
y = " Fantastic" # global

def myfunc():
    global y  # alterando utilizando palavra chave
    y = "INCRIVEL"

myfunc()

print("Python is " + y)
"""

#convercao de tipos de Variaveis
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = 0.0
print(f"criando uma variavel \"x = {x}\" - {(type(x))}") 
print(f"e uma outra variavel \"a = {a}\" - {(type(a))}")

a = type(float(x))

print(f"\tApos a mudanca \"x = {x}\" - {(type(float(x)))}")

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)


print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
"""

"""
#numeros aleatorios
import random

#numeros aleatorios de 0 ate 9
print(random.randrange(0,10))

#fatiando uma Strings
b = "heloo , world!"
print(b[:])
print(b[-6:-1])

"""


#Verifique a sequência
''''''"""
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("YES, 'Free' is present")
if "expensive" not in txt:
  print("NO, 'expensive' is NOT present.")


""" 



#modificar strings
"""
a = " Marcelo Eduardo Menegheti "
print("variavel a = ",a)
print(" ")
print("variavel a com upper()  = ",a.upper())
print("variavel a com lower()  = ",a.lower())
print("variavel a com strip()  = ",a.strip())#remove os espaco do comeco/fim
print("variavel a com replace()= ",a.replace("M","N"))#Substituir
print("variavel a com split()  = ",a.split(" "))#divide a string em substrings
print(" ")
print(" ")
"""

# combinado strings e int 
"""
idade = 24 
txt = "\nMeu nome e marcelo, e eu tenho {}\n"
print(txt.format(idade))

quantidade = 5
item = 540
preco = 19.99
myOrder = "Eu quero {} pecas do item {} por {} Dollars\n"
print(myOrder.format(quantidade,item,preco))

myAnotherOrder = "Eu quero pagar {2} dolares por {0} pecas do item {1}\n"
print(myAnotherOrder.format(quantidade,preco,item))
"""
#------------------------------------------------------------------------------------------
#metodos
'''
#centralizar uma string
t = " ola mundo "
a = t.center(20,"-")
print(a)

#Returns True if the string is an identifier
txt = "felix"
b = t.isidentifier()
print(b)
'''
'''
#
t = "Python Booleans"
a = t.center(40,"-")
print(a)

print(10 > 9)
print(10 == 9)
print(10 < 9)

print(" ")
print(bool("Hello"))
print(bool(15))

print(" ")
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print("  ")
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#valores vazio ou func == false
print("  ")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print("  ")

#funcoes booleanas
def myFunction() :
  return False

print(myFunction())

if myFunction():
  print('sim')
else:
  print("não")
print("  ")

#verificando se um numero.
k = 200
print(isinstance(k, int))
'''
#------------------------------------------------------------
'''
z = 'Operadores Python'
h = z.center(40,"-")
print(h)


#Returns True if both variables are the same object
x = 5
y = 2

x1 = 4
y1 = 4

#Operadores de identidade Python
print(x is y)
print(x is not y)
print(" ")
print(x1 is y1)
print(x1 is not y1)
print(" ")

#Operadores Python
print(x)
print(x<<1)
print(x<<2)

print(" ")
print(x)
print(x>>1)
print(x>>2)

print(" ")
print(y)
print(y<<1)
print(y<<2)
print(" ")
'''
#------------------------------------------------------------
"""
xor = "XOR"
x = xor.center(40,"-")
print(x)

print('6 xor 2 + 1: ',6 ^ 2 + 1)#O calculo acima é  6 ^ 3 = 5
print('5 xor 4 - 2: ',5 ^ 4-2)#O calculo acima é  5 ^ 2 = 7 


O XOR bit a bit tem uma precedência menor que a adição e precisamos calcular a adição primeiro.
O calculo acima é  6 ^ 3 = 5
O calculo acima é  5 ^ 2 = 7 

More explanation:
The ^ operator compara cada bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110 ->[110]
3 = 0000000000000011 ->[011]

XOR = 101
--------------------
5 = 0000000000000101 
====================

5 = 0000000000000101 ->[101]
2 = 0000000000000010 ->[010]

XOR = 111
--------------------
7 = 0000000000000111
====================

Numeros Decimais e sues valores binari:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

"""
#------------------------------------------------------------
And = "AND"
x = And.center(40,"-")
print(x)

print('6 and 2 + 1: ',6 & 2 + 1)


O calculo acima é 6 & 3 = 2
Mais explicação:
O operador & compara cada bit e define-o como 1 se ambos forem 1, caso contrário, é definido como 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
"""
#------------------------------------------------------------
Or= "OR"
x = Or.center(40,"-")
print(x)
print('6 or 4: ',6 | 4)


More explanation:
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

O calculo acima é 6 | 3 = 7
6 = 0000000000000110 -> [1][1][0]
3 = 0000000000000011 -> [0][1][1]

OR = [1][1][1]
--------------------
7 = 0000000000000111
====================



O calculo acima é 6 | 4 = 6
6 = 0000000000000110 ->[1][1][0] 
4 = 0000000000000100 ->[1][0][0]

OR = [1][1][0]
--------------------
6 = 0000000000000110
====================


Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""

#-----------------------------------------------------------------------------------
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