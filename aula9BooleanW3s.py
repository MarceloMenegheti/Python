
#centralizar uma string
t = " Boleanos"
a = t.center(40,"-")
print(a)

#Returns True if the string is an identifier
txt = "felix"
b = txt.isidentifier()
print(b)

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