

def minha_funcao(valor1,valor2):
    return valor1 + valor2
while True:
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))

    resposta = minha_funcao(a,b)

    print("Resposta: ",resposta)
    if a == 0:
        break