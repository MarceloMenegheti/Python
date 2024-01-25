#convercao de tipos de Variaveis
""""""
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = 0.0
print(f"criando uma variavel \"x = {x}\" - {(type(x))}") 
print(f"e uma outra variavel \"a = {a}\" - {(type(a))}")

a = type(float(x))

print(f"\tApos a mudança \"x = {x}\" - {(type(float(x)))}")

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)


print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
