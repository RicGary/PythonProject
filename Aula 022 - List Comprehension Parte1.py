"""
List Comprehension - Parte 1

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir outro
iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável ]


# Exemplos 1

numeros = list(range(1,6))
# Dado um valor para cada valor em um iterável (neste caso lista).
res = [valor * 10 for valor in numeros]

print(res)


"""
"""
[x for x in iterável]

Para entendermos melhor o que está acontencendo devemos dividí-las em duas partas:

- A primeira parte: for valor in numeros
- A segunda parte: numero * 10

# Exemplo 2

def expressao(valor):
    return valor**2/2**valor

res = [expressao(valor) for valor in numeros]

print(res)

# List Comprehension vs Loop

# Loop
numeros = list(range(1,6))

numeros_dobrados = []
for valor in numeros:
    numeros_dobrados.append(valor*2)
print(numeros_dobrados)

# List Comprehension
numeros = list(range(1,6))

print([valor * 2 for valor in numeros])

# Outros Exemplos

# 1

nome = 'eric naiber'

print([letra.upper() for letra in nome])

# 2

amigos = ['ricardo','jeferson','rafaela','maria']

print([amigo.title() for amigo in amigos])

# 3

print([numero*3 for numero in range(1,11)])

# 4

# São considerados False em Python:
# Zero (0)
# Lista vazia []
# '' String vazia

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5

print([str(numero) for numero in range(1,6)])
"""

