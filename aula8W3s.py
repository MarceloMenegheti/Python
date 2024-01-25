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
