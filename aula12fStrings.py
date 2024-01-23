nome = 'Marcelo Meneghti'
altura = 1.71
peso = 66
imc = peso//(altura*altura)

linha1 = f'{nome} tem {altura:.2f} de altura'
linha2 = f'pesa {peso} quilos e seu imc eh {imc:2.2f}'

print(linha1)
print(linha2)

if (imc > 18.5 and imc < 24.9):
    print("IMC NORMAL !")
elif(imc < 18.4):
    print("IMC ABAIXO DO PESO !")
else:
    print("IMC ACIMA DO PESO !")