import os

mensagens = []

nome = input("nome :")

while True:
    #limpando terminal 
    os.system('cls')

    if len(mensagens) > 0:
        for i in mensagens:
            print(i['nome'], "-", i['texto'])
    print("__________")
    # obentendo    texto
    texto = input("mensagens: ")
    if texto == "fim":
        break
    #adicionando mensagens na lista 
    mensagens.append({
        "nome": nome,
        "texto": texto
})



