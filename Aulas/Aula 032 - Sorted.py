"""
Sorted

sorted(iterable, *, key=None, reverse=False)

OBS: Não confunda com a função sort() que já foi estudado em listas. O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, o sorted() serve para ordenar

# A função sort() altera a própia lista.

lista = [1,5,2,9,2,5,8]
lista.sort()
print(lista)

# A função sorted() não altera a lista original.

lista = [1,5,2,9,2,5,8]
sorted(lista)
print(lista)


from sys import getsizeof

# Funciona para tuplas, porém sempre retorna uma lista
numeros = 1,7,3,9,4,2,8,5,6
print(sorted(numeros))
print(tuple(sorted(numeros)))
print(set(sorted(numeros)))

print(
    getsizeof(sorted(numeros)),
    getsizeof(tuple(sorted(numeros))),
    getsizeof(set(sorted(numeros))),
    sep='\n'
)

# Note como uma tupla é mais leve

# Adicionando parâmetros ao sorted()

numeros = 1,7,3,9,4,2,8,5,6
print(sorted(numeros, reverse = True))

# Podemos utilizar o sorted() para coisas mais complexas.

usuarios = [
    dict(username='samuel', tweets=['Eu adoro bolos', 'Eu adoro pizzas.']),
    dict(username='carla', tweets=['Eu adoro gatos.']),
    dict(username='bob123', tweets=['Fora Bolsonaro!']),
    dict(username='dogo', tweets=['Auauau']),
    dict(username='gal', tweets=[]),
    dict(username='jeff', tweets=[]),
    dict(username='ellon_musk', tweets=['Bitcoin não vale nada!', 'Comprem bitcoin vale muito!'])
]

print(usuarios)
print(sorted(usuarios, key = len))  # Ordena por tamanho, porém todos tem duas chaves, então não mudou nada.

print(sorted(usuarios, key = lambda usuario: usuario['username']))  # Ordena os nomes.

"""


