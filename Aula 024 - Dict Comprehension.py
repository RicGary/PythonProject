"""
Dict Comprehension

Sintaxe:

{chave:valor for valor in iterável}

# Exemplos

# 1

numeros = dict(a=1,b=2,c=3,d=4)

quadrado = {chave : valor ** 2 for chave, valor in numeros.items()}   # numeros.items() devolve uma tupla do tipo
print(quadrado)                                                     # ([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

quadrado = {_ : valor ** 2 for _, valor in numeros.items()}     # _ descarta o valor, já que não será utilizado.
print(quadrado)

# 2

numero = list(range(1,6))

quadrado = {valor:valor**2 for valor in numero}
print(quadrado)

# OBS: Em dict não pode repetir chave, não gera erro porém não cria nova chave.

# 3

chaves = 'abcde'
valores = list(range(1,6))

mistura = {chaves[i] : valores[i] for i in range(len(chaves))}
print(mistura)

# Exemplos com lógica condicional

numeros = list(range(1,6))

res = {num : 'par' if num % 2 == 0 else 'impar' for num in numeros}
print(res)
"""

