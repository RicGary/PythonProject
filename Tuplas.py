"""
Tuplas

As tuplas são muito parecidas com listas.

Existem basicamente duas diferenças:

1 - Tuplas são representadas por parênteses.

2 - As tuplas são imutáveis: Assim que for criada uma tupla
ela não muda.Toda operação feita em cima de uma tupla gera
uma nova tupla.
===============================================================
# CUIDADO 1: Tuplas são representadas por parenteses, mas veja:

tuple1 = (1,2,3,4,5)
print(tuple1)
print(type(tuple1))

tuple2 = 1,2,3,4,5
print(tuple2)
print(type(tuple2))

# CUIDADO 2: Tuplas com 1 elemento.

tuple3 = (4)        # Isso NÃO é uma tupla.
print(tuple3)
print(type(tuple3))

tuple4 = (4,)       # Isso é uma tupla.
print(tuple4)
print(type(tuple4))

# CONCLUSÃO: Tuplas são definidas pela vírgula e não pelos parênteses.
======================================================================

tupla = tuple(range(1,11))
print(tupla)

tupla = ('Geek University','Programação em Python: Essencial')
escola, curso = tupla
print(escola)
print(curso)

# Podemos fazer soma, pegar valor máximo, valor mínimo, etc.

tupla = (1,2,3,4,5)
print(sum(tupla))
print(min(tupla))

# Concatenação de tuplas.

tupla1 = (1,2,3)
tupla2 = (4,5,6)

print(tupla1+tupla2)

# Tuplas são imutáveis porém podemos sobrescrever seus valores.

tupla1 = (1,2,3)
tupla2 = (4,5,6)

print(tupla1)

tupla1 = tupla1+tupla2

print(tupla1)

# Assim como na lista podemos ver se determinado valor está na tupla.

tupla = (1,2,3)

print(3 in tupla)

# Dicas na utilização de tuplas.
# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados em uma coleção.
# Exemplo:

meses = ('Janeiro','Fevereiro','Março','...')

# O acesso de uma tupla é semelhante ao de uma lista.

print(meses[2])

# Iterar com o while
i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# Verificamos em qual índice está o valor.

print(meses.index('Março'))

# Por que utilizar Tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas são mais seguras.
"""