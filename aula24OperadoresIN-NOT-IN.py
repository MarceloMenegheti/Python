# Operadores in e not in
# Strings são iteráveis
#  0  1  2  3  4  5  6
#  m  a  r  c  e  l  o
# -7 -6 -5 -4 -3 -2 -1
nome1 = 'marcelo'
print(nome1[2])
print(nome1[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = input("Digite o seu nome: ")

find = input("Digite a palavra que deseja encontar: ")

if find in nome:
    print(f'{find} esta em {nome}')
else:
    print(f'{find} nao esta em {nome}')

if find not in nome:
    print(f'{find} nao esta em {nome}')
else:
    print(f'{find}  esta em {nome}')