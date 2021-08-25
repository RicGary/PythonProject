"""
Generator Expression

Em aulas anteriores nós estudamos:
- List Comprehension
- Dict Comprehension
- Set Comprehension

Não vimos:
- Tuple Comprehension... pois se chamam Generators.

# Vimos:

nomes = ['Carlos','Carla','Cassio']
print(any([nome[0] == 'C' for nome in nomes]))

# Podemos utilizar Generators:

print(any(nome[0] == 'C' for nome in nomes))

print(tuple(nome[0] == 'C' for nome in nomes))


Diferença entre:

nomes = ['Carlos','Carla','Cassio','Vanessa','Eric','Caka']

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)  # Já da o valor

# Generators
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)  # Retorna um objeto mais leve que a lista

    - Generator ocupa menos recurso em memória, então é preferível utilizá-lo.


# Qual a utilidade de GetSizeOf?
# Retorna a quantidade de bytes em memória do elemento passado como parâmetro.

from sys import getsizeof

# List Comprehension
lista_comp = getsizeof([x * 10 for x in range(1000)])   # 8856 bytes
print(lista_comp)

# Set Comprehension
lista_comp = getsizeof({x * 10 for x in range(1000)})   # 32984 bytes
print(lista_comp)

# Dict Comprehension
lista_comp = getsizeof({x: x * 10 for x in range(1000)})    # 36960 bytes
print(lista_comp)

# Generator
lista_comp = getsizeof((x * 10 for x in range(1000)))   # 112 bytes
print(lista_comp)
"""

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))

for i in gen:
    print(i)
