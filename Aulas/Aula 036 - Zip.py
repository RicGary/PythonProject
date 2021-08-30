"""
Zip

zip() -> Cria um iterável chamado zip object, que agrega elementos de cada um dos iteráveis passados como
entrada em pares.

from sys import getsizeof
# Exemplo

lista = [1,2,3]
lista2 = [4,5,6]

zip1 = zip(lista, lista2)
print(zip1)
print(type(zip1))

print(getsizeof(zip1))  # Mais leve.
print(getsizeof(lista))

# Podemos sempre gerar uma lista, tupla ou discionário.

print(list(zip1))
print(tuple(zip1))
print(dict(zip1))

# Aparece em branco pois depois de utilizado ele é apagado da memória.
zip1 = zip(lista, lista2)
print(list(zip1))

zip1 = zip(lista, lista2)
print(tuple(zip1))

zip1 = zip(lista, lista2)
print(dict(zip1))

lista1 = [1,2]
lista2 = [3,4]
lista3 = [5,6,7,8]

zip1 = zip(lista1,lista2,lista3)
print(list(zip1))

# OBS: O zip() utiliza como parâmetro o menor iterável. Isso significa que se estiver trabalhando
# com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor iterável acabar.

# Podemos utilizar diferentes iteráveis.

lista = [1,2,3]
tupla = 4,5,6

zip1 = zip(lista,tupla)
print(list(zip1))

# Lista de tuplas.

dados = [(1,2),(3,4),(5,6)]
print(list(zip(*dados)))

# Fazemos o desempacotamento dos dados utilizando *.


"""