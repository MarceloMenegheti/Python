numero_1 = input('informe o primeiro numero: ')
numero_2 = input('informe o segundo numero: ')

if numero_1 > numero_2:
    print(f'o {numero_1=} eh maior que o numero {numero_2=}')
elif numero_1 == numero_2:
    print(f'o {numero_1=} eh IGUAL ao numero {numero_2=}')
else:
    print(f'o {numero_2=} eh maior que o numero {numero_1=}')