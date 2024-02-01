txt = "FUNCÕES"
x = txt.center(40,"-")
print(x)

#criando uma funcao
def myfunction():
    print("hello world!!")


def minhaFunction(nome):
    print(nome + " menegheti")

#chamando a funcao
myfunction()

#As informações podem ser passadas para funções como argumentos.
minhaFunction("marcelo")#args
minhaFunction("marcia")
minhaFunction("melo")


'''informações que são passadas para uma função:
Um parâmetro é a variável listada entre parênteses na definição da função.
Um argumento é o valor enviado à função quando ela é chamada.'''


#Número de argumentos
def minhaFunction2(firstName,lastName):
    print(firstName +" "+ lastName)


x = input("\nqual o seu nome? ")
y = input("qual o seu sobrenome nome? ")
#chamando a func
minhaFunction2(x,y)

#Argumentos Arbitrários, *args
def minhaFunction3(*args):
    
    print("seu nome é ",*args)


x = input("\nqual o seu nome? ")
y = input("qual o seu sobrenome nome? ")

minhaFunction3(x,y)


#Argumentos de palavras-chave
def minhaFunction(*arg):
    
    if "marcelo" in arg:
        print("caçula")
    elif "diego" in arg:
        print("filho mais velho")
    elif "ana" in arg:
        print("mae")
    else:
        print("pai")

child = input("\nprimeiro filho: ")
child2 = input("segundo filho: ")
child3 = input("terceiro filho: ")

minhaFunction(child,child2,child3)
print()


#Argumentos de palavras-chave arbitrárias, **kwargs
def my_function(**kid):
  print("seu sobrenome é: " + kid["lname"])

#passando uma variavel desconhecida
my_function(fname = "marcelo", lname = "Menegheti")
print()


#Passando uma lista como argumento
def my_function(food):
  for x in food:
    print(x)

fruits = ["morango", "banana", "cereja"]
#passando um array.
my_function(fruits)


#Valores de retorno
def my_function(x):
  return 5 * x
print()
print(my_function(3))
print(my_function(5))
print(my_function(9))

#A declaração de aprovação
def myfunction():
  pass

my_function(10)

#Argumentos apenas posicionais
def my_function(x, /):
  print(x)
my_function(3)#chamando a func

#Argumentos somente de palavras-chave
def my_function(*, x):
   print(x)
my_function(x = 3)#chamando a func
