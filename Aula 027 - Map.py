"""
Map.

Com map fazemos o mapeamento de valores para função.
import math


def area(r):
    '''Calcula a área de um círculo com raio r.'''
    return math.pi * r ** 2


print(area(2))
print(area(5.3))

raios = [4, 7, 1.2, 8, 9.4]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 Map

# Map é uma função que recebe dois valores: O primeiro a função, o segundo um iterável.

areas = map(area, raios)
print(list(areas))

# Forma 3 Map com Lambda

print(list(map(lambda r:math.pi * r ** 2, raios)))
# OBS: Após utilizar a função map, depois da primeira utilização do resultado, ele zera.
"""

"""
Para fixar:
    - Temos dados iteráveis;
         dados: a1, a2, a3, ..., an
    
    - Temos uma funcao;
         função: f(x)
         
    - Utilizams map;
         map(f ,dados)
            O map object: f(a1), f(a2), f(a3), ..., f(an)


nome = 'Eric Naiber'

troca = map(lambda x: x.replace('E','EEEE'), nome)
print(troca)
print(list(troca))
"""
