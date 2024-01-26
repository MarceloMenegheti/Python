txt = "LISTA"#--------------------------------------------------------
x = txt.center(40,"-")
print(x)

#Acessar itens de uma lista
list = ["apple", "banana", "uva","morango"]
print("mostrando a lista: ",list)
print("\nmostarando o indice[1] da lista: ",list[1])

#Indexação Negativa
print("\nmostarando o indice[-2] da lista: ",list[-2])

#Gama de índices
print("\nmostarando uma gama indice[1:-1] da lista: ",list[1:-1])

#exemplo retorna os itens desde o início, mas NÃO incluindo, "goiaba":
print("\nmostarando uma todos os elementos menos o indice[:3] da lista: ",list[:3])
print(" ")

#retorna os itens de "uva" até o final:
print("mostarando os elementos depois do indice[:2] da lista: ",list[2:])
print(" ")

#alterando um valor
list[1] = "Jabuticaba"
print("Alterando um valor list",list)
print(" ")

#Alterar um intervalo de valores de itens
list[0:3] = ["cebola","flor"]
print("novos valores na lista: ",list)
print(" ")
