
# Variaveis Globais
""""""
x = "Awesome"

def myfunc():# criando minha func
    x = "fantastic"
    print("\'Interno\' Python is " + x)

myfunc()#chamando minha func

print("\'Externo\' Python is " + x)
print("")



#Palavra-Chave Global
""""""
y = " Fantastic" # global

def myfunc():
    global y  # alterando utilizando palavra chave
    y = "INCRIVEL"

myfunc()

print("Python is " + y)
print("")
