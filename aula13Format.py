a = 'A'
b = 'B'
c = 1.1

string = 'a = {0}\nb = {1}\nc = {2:.2f}'

formato = string.format(
    nome1=a, nome2=b, nome3=c)#parametro nomeado

print(formato)