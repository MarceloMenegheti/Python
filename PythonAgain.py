

# voltando a estudar Python!!!!

# this is a comment   
"""
x = 5
y = "jonh"
print(x)
print(y)
"""  


# descrever o tipo de var
"""
t = 4
t = 'Sally'
print(type(t))
"""


# Nomes Variaveis
"""
myVariableName = "John"      #Estojo de Camelo
my_variable_name = "Marcelo" #Caso Cobra
MyVariableName = "Luiz"      #Caso Pascal

print(myVariableName)
print(my_variable_name)
print(MyVariableName)
"""


# atribuicao de valores
"""
p,l,k ="Laranja","Banana","Cereja"
print(p,l,k)
"""


#atribuir multiplas variaveis
"""
h = v = c = "\nPamonha\n"
print(h,v,c)
"""


#descompactar uma colecao
"""
Fruits = ["maca","banana","Cereja"]
x,y,z = Fruits
print(x)
print(y)
print(z)
"""


# Variaveis Globais
"""
x = "Awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python e " + x)
"""


#Palavra-Chave Global
"""
x = " Fantastic" # global

def myfunc():
    global x  # alterando utilizando palavra chave
    x = "INCRIVEL"

myfunc()

print("Python is "+x)
"""

#convercao de tipos de Variaveis
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
"""


#numeros aleatorios
"""
import random

print(random.randrange(1,11))
"""


#Verifique a sequência
'''
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("YES, 'Free' is present")
if "expensive" not in txt:
  print("NO, 'expensive' is NOT present.")
'''


#fatiando uma Strings
""" 
b = "heloo , world!"
print(b[:])
print(b[-6:-1])
"""


#modificar strings
"""
a = " Marcelo Eduardo Menegheti "
print(a.upper())
print(a.lower())
print(a.strip())#remove os espaco do comeco/fim
print(a.replace("M","N"))#Substituir
print(a.split(" "))#divide a string em substrings
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