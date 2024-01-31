t = "Dicionários"
x = t.center(40,"-")
print(x)

'''Dicionário
Dicionários são usados ​para armazenar valores de dados em pares (chave: valor).
Um dicionário é uma coleção ordenada*, mutável e que não permite duplicatas.'''

#criando um dicionario, os dicionários são mutáveis, o que significa que podemos
#alterar, adicionar ou remover itens após a criação do dicionário.
dict3 = {
  "Marca": "Ford",
  "modelo": "Mustang",
  "Ano": 1964
}

print("imprimindo o dicionario\n",dict3)
print()
print("Imprima o valor da 'marca' do dicionário: ",dict3["Marca"])
print()

#Duplicatas não permitidas
dict2 = {
  "Marca": "Ford",
  "modelo": "Mustang",
  "electric": False,
  "Ano": 1964,
  "Ano": 2020
}

print("Duplicatas não permitidas:\n",dict2)

#método dict()
novoDict = dict(nome = "marcelo",idade = "24", pais = "Brasil")
print(novoDict)
print()

'''* Os itens do conjunto não podem ser alterados, mas você pode remover e/ou adicionar itens sempre que desejar.'''
#get() método
y = novoDict.get("idade")
print("método get('idade'): ",y)
print()

#Obtenha as chaves
x = novoDict.keys()
print("acessando as keys: ",x)

#values()método
y = novoDict.values()
print("acessando os valores: ",y)
print()

#items()método
x = novoDict.items()
print("acessando os itens: \n",x)

novoDict["pais"] = "URSS"
novoDict["color"] = "vermelho"

print("\nacessando os itens apos mudança: \n",x)
print()

#condicional
if "color" in novoDict:
    print("Sim, esta no dicionario!!")
print()


t1 = "Dicionários-metodos"
y = t1.center(38,"-")
print(y)
print()

#update()método 
novoDict.update({"idade": 20})#O update()método atualizará o dicionário com os itens do argumento fornecido.
print("imprimindo nova idade: ",novoDict["idade"])

#pop()método
novoDict.pop("color")
print("Removendo a 'color' = chave:valor -> ",novoDict.items())

# popitem() método
novoDict.popitem()#remove o ultimo item!
print("removendo o ultimo item popitem(): ",novoDict)
print()

#clear() método
print("imprimindo o dict3",dict3)
dict3.clear()
print("esvaziando o dict3",dict3)

#loops
print()
for x in novoDict:
  print( "imprimnd o novoDict[",x,"] ",novoDict[x])
print()

'''Copie um dicionário
Você não pode copiar um dicionário simplesmente digitando dict2 = dict1, porque: dict2será apenas uma referência a dict1,'''

#copy() método
newDict = novoDict.copy()
print("novo Dicionario copiado 'newDict': ",newDict)
print()


#Dicionários aninhados
#Um dicionário pode conter dicionários, isso é chamado de dicionários aninhados.
print("Dicionários aninhados: ")
minhaFamily = {
   "child1" : {
      "name" : "Marcelo",
      "Ano"  : 1999
   },
   "child2": {
      "name" : "Diego",
      "Ano"  : 1996
   },
   "child3" : {
      "name" : "Luiz",
      "Ano"  : 1999
   }
}
print(minhaFamily)
print()

print("outra forma de Dicionários aninhados")
child4 = {
  "name" : "Emil",
  "year" : 2004
}
child5 = {
  "name" : "Tobias",
  "year" : 2007
}
child6 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child4" : child4,
  "child5" : child5,
  "child6" : child6
}
print(myfamily)
print()

#Acessar itens em dicionários aninhados
print("acessar itens de Nested Dictionaries: ")
print(minhaFamily["child1"]["name"])
print(minhaFamily["child2"]["Ano"])
print(minhaFamily["child3"]["name"])
