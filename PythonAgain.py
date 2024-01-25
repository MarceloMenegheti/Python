

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
""""""
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
