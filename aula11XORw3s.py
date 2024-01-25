xor = "XOR"
x = xor.center(40,"-")
print(x)

print('6 xor 2 + 1: ',6 ^ 2 + 1)#O calculo acima é  6 ^ 3 = 5
"""
O XOR bit a bit tem uma precedência menor que a adição e precisamos calcular a adição primeiro.
O calculo acima é  6 ^ 3 = 5
O calculo acima é  5 ^ 2 = 7 

More explanation:
The ^ operator compara cada bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
"""

x = """
6 = 0000000000000110 ->[110]
3 = 0000000000000011 ->[011]

XOR = 101
--------------------
5 = 0000000000000101 
====================
"""
print(x)
print('5 xor 4 - 2: ',5 ^ 4-2)#O calculo acima é  5 ^ 2 = 7 

y ="""
5 = 0000000000000101 ->[101]
2 = 0000000000000010 ->[010]

XOR = 111
--------------------
7 = 0000000000000111
====================
"""
print(y)

"""
Numeros Decimais e sues valores binari:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""




