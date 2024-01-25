And = "AND"
x = And.center(40,"-")
print(x)

print('6 and 2 + 1: ',6 & 2 + 1)

"""
O calculo acima é 6 & 3 = 2
Mais explicação:
O operador & compara cada bit e define-o como 1 se ambos forem 1, caso contrário, é definido como 0:
"""

x = """
6 = 0000000000000110 ->[1][1][0]
3 = 0000000000000011 ->[0][1][1]
AND = [0][1][0]
--------------------
2 = 0000000000000010
====================
"""
print(x)

"""

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
