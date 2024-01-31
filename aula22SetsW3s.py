
'''Um conjunto (SET) é uma coleção não ordenada , imutável* e não indexada, os itens do conjunto não podem ser alterados, mas você pode remover itens e adicionar novos itens.

Definição de itens:
Os itens definidos são desordenados, imutáveis ​​e não permitem valores duplicados.

Não ordenado: 
Os itens do conjunto podem aparecer em uma ordem diferente sempre que você os utiliza e não podem ser referenciados por índice ou chave..'''

t = "SET"
x = t.center(40,"-")
print(x)

set1 = {"morango","abacaxi","manga","morango"}
set2 = {"melancia","uva",True,1,2}#Os valores True e 1 são considerados o mesmo valor

print("um Set não permite duplicatas 'std': ",set1)
print("um Set não permite duplicatas 'bool': ",set2)
print("tamanho set1: ",len(set1)," - ",type(set1))
print("tamanho set2: ",len(set2)," - ",type(set1))
print("")

'''Acessar itens
Você não pode acessar itens de um conjunto consultando um índice ou uma chave. Mas você pode percorrer os itens do conjunto usando um for loop ou perguntar se um valor especificado está presente em um conjunto usando a inpalavra-chave.'''

#imprimindo itens:
for x in set1:
    print(x)
print("")

for y in set2:
    print(y)
print("")


#acessando itens:
print("Verifique se 'abacaxi' está presente no conjunto:")
print('abacaxi' in set1)
print("")

#add() método.
set2.add("laranja")
print("adicionando set2 ='laranja': \n",set2)
print("")

#update() método.
conjunto = {"lol","ola","alo"}
set1.update(conjunto)
print("adicionando conjunto ao set1:\n",set1)
print("")

# método remove(), ou discard().
set1.remove("alo")#Se o item a ser removido não existir, remove()gerará um erro.

set1.discard("hello")#Se o item a ser removido não existir, discard() NÃO gerará um erro.


# pop() método
x = set1.pop()#esse método removerá um item aleatório
print("removendo um item aleatorio:",set1)
print("")

# clear() método
set1.clear()
set2.clear()
print("esvaziando o set1: ",set1)
print("esvaziando o set2: ",set2)
print("")

#A palavra-chave del excluirá o conjunto completamente:
del set1
del set2

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
print('novo set1:',set1,"\nnovo set2:",set2)
print("")

# union()método
set3 = set1.union(set2)#Ambos union()e update() excluirão quaisquer itens duplicados.
print("Juntando dois SET: ",set3)
print("")

#novo set
set4 = {"bateria","bola"}


# intersection() método 
z = set3.intersection(set4)
print("intersection: ",z)

#symmetric_difference_update() método
set4.symmetric_difference_update(set3)#Mantenha tudo, mas NÃO as duplicatas
print(set4)