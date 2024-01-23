# codigo com funcao

Fluxo_Caixa = []

print("--------")
print("Fluxo de Caixa")
print("--------")
print("1 - adicionar receita")
print("2 - adicionar despesa")
print("\n Digite outro numero para encerrar\n")

def adicionar_transacao():
    nome = input("nome: ")
    valor = float(input("valor: "))

    Fluxo_Caixa.append({
         "nome": nome,
         "valor": valor
    })


while True:
    opcao = int(input("\ndigite a opcao: "))
    if opcao == 1:
        adicionar_transacao()        
    elif opcao == 2:
        adicionar_transacao()         
    else:
        break

#nota fiscal
total = 0
for fc in Fluxo_Caixa:
        print("nome:",fc['nome'], "valor: RS",fc['valor'])
        total = total + fc['valor']
print("Saldo Atual :",total)   
