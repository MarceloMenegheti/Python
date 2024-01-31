#Condições Python e instruções If

'''
Igual a: a == b
Não é igual: a! = b
Menor que: a <b
Menor ou igual a: a <= b
Maior que: a > b
Maior ou igual a: a >= b'''

txt = "IF-ELIF-ELSE"
x = txt.center(40,"-")
print(x)


#condiconal - IF
a = 33
b = 200
if b > a:
  print("b is greater than a")


#condiconal - ELIF
'''A palavra-chave elif é a maneira do Python dizer "se as condições anteriores não eram verdadeiras, tente esta condição".'''
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# condiconal - ELSE
'''A palavra-chave else captura qualquer coisa que não seja capturada pelas condições anteriores.'''
 

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
print()

print("Declaração if de uma linha: ")
if a < b: print("a is greater than b")
print()

print("Declaração if de uma linha: ")
print("A") if a > b else print("B")
print()


print("Instrução if else de uma linha, com 3 condições:")
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
print()


#aninhado:
print("Você pode ter if instruções dentro if de instruções:")

x = 11

if x > 10:
  print("acima de 10,")
  if x > 20:
    print("e tambem esta acima 20!")
  else:
    print("mas não acima 20.")
print()

a = 33
b = 200


#A declaração de aprovação
'''if as instruções não podem estar vazias, mas se por algum motivo você tiver uma if instrução sem conteúdo, coloque-a na 'pass' instrução para evitar erros.'''

if b > a:
  pass
