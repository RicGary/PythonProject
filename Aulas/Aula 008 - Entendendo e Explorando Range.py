"""
Range

Tipo I:
range(3)
    0, 1, 2

Tipo II:
range(1,3)
    1, 2, 3

Tipo III:
range(1,7,2)    2 significa ir de 2 em dois
    1, 3, 5

Tipo IV:
range(10,1,-2)      Vai de trás p/frente de -2 em -2 (contagem regressiva)
    10, 8, 6, 4, 2

Obs:
Pode formar listas usando range da seguinte forma:

lista = list(range(1,11))
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

for i in range(10, 1, -2):
    print(i, sep=',', end=' ')

lista = list(range(1, 11))

print(lista)
