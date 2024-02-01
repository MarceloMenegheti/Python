'''Recursão
Python também aceita recursão de função, o que significa que uma função definida pode chamar a si mesma.

A recursão é um conceito matemático e de programação comum. Isso significa que uma 
função chama a si mesma. Isso tem a vantagem de significar que você pode percorrer os dados para chegar a um resultado.

O desenvolvedor deve ter muito cuidado com a recursão, pois pode ser muito fácil escrever uma função
que nunca termina ou que usa quantidades excessivas de memória ou potência do processador. No entanto, 
quando escrita corretamente, a recursão pode ser uma abordagem de programação muito eficiente e matematicamente elegante.'''

t = "Recursividade"
x = t.center(30,"-")
print(x)

def functionrecursão(k):
    
    if (k > 0):
        count = k + functionrecursão(k - 1)
        print(count)
    else:
        count = 0
    return count


x = int(input("exemplo recursivo: "))
functionrecursão(x)
print("")