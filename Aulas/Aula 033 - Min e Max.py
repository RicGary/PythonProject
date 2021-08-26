"""
Min e Max

Podemos fazer inúmeras operações com o min e max:

dicionario = dict(a=5, b=2, c=12, d=10, e=45)

# Retorna a chave que contém o maior valor e o menor.
print(max(dicionario))
print(min(dicionario))

# Retorna o maior valor e o menor.
print(max(dicionario.values()))
print(min(dicionario.values()))

nomes = ['Arya', 'Tim', 'Olivander', 'Dora']

# Retorna na ordem alfabética o menor e o maior.
print(max(nomes))
print(min(nomes))

# Podemos utilizar uma função para ordenação.
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
"""



