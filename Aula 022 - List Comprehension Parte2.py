"""
List Comprehension - Parte 2

Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension.

# Exemplo 1

numeros = list(range(1,11))

pares = [valor for valor in numeros if valor % 2 == 0]
impares = [valor for valor in numeros if valor % 2 != 0]

print(
    pares,
    impares,
    sep='\n'
)

# Refatorando Exemplo 1

# Qualquer número par utilizando módulo de 2 é 0 e ZERO em python é False. not False = True
pares = [valor for valor in numeros if not valor % 2]
# Para cada valor em número salva esse valor se for TRUE
impares = [valor for valor in numeros if valor % 2]
# Para cada valor em número salva esse valor se for FALSE

print(
    pares,
    impares,
    sep='\n'
)

# Exemplo 2

# Se o valor for par faz vezes dois, se for ímpar divide por dois, para cada valor no range(1,6)
res = [valor * 2 if valor % 2 == 0 else valor / 2 for valor in range(1,6)]
print(res)
"""



