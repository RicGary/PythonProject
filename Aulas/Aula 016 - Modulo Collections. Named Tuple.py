"""
Módulo Collections - Named Tuple

Link para mais info.: https://docs.python.org/3/library/collections.html?highlight=collections#collections.namedtuple

Collections -> High-performance Container Datetypes

Named Tuple -> São tuplas diferênciadas, onde, especificamos um nome para
a mesma e também, parâmetros.
"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

# Acessando os dados

# Forma 1

print(ray[0])   # idade
print(ray[1])   # raça
print(ray[2])   # nome

# Forma 2

print(ray.idade)   # idade
print(ray.raca)   # raça
print(ray.nome)   # nome

# Outras coisas que podemos fazer

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))