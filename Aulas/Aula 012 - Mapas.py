"""
Mapas ou também como é conhecido em python...
...Dicionários

Representados por {}

print(receita)

# Iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi {receita[chave]}R$.')

print(receita.keys())   # Mostra as chaves.
print(receita.values()) # Mostra todos os valores.

for chave in receita.keys():
    print(chave)

for valor in receita.values():
    print(valor)

print(receita.items())

# Desempacotamento de Dicionários.
for chave, valor in receita.items():
    print(f'No mês de {chave} Eric recebeu {valor}R$.')

# Soma, valor máximo, valor mínimo, tamanho.
print('soma' , sum(receita.values()))
print('max', max(receita.values()))
print('min', min(receita.values()))
print('tamanho', len(receita))

"""

receita = dict(Janeiro=100, Fevereiro=250, Março=400)

# Soma, valor máximo, valor mínimo, tamanho.
print('soma' , sum(receita.values()))
print('max', max(receita.values()))
print('min', min(receita.values()))
print('tamanho', len(receita))
