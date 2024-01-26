txt = "CONDICONAIS"#--------------------------------------------------------
x = txt.center(40,"-")
print(x)

list = ["apple", "banana", "uva","morango"]

list[1] = "uva"
#Verifique se “apple” está presente na lista:

if "uva" in list:
    print("SIM, 'uva' esta na lista!.")
print(" ")

#outra forma em uma linha
novalist = [x for x in list if "a" in x]
print(novalist,"  outra forma.")
print(" ")

print("Iterável com condiconais: ")
newlista = [x for x in range(10) if x < 5]
print(newlista)
print(" ")

list[1] = "banana"
print("imprimindo a lista: ",list)
print(" ")

print("Retorne 'laranja' em vez de 'banana': ")
newlista = [x if x != "banana" else "laranja" for x in list]
print(newlista)