"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros, ou se o iterável está vazio.

# Exemplo

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros?

print(all([1, 2, 3, 4, 5])) # Sabemos que 0 é False e os outros são True

print(all([]))  # Todos os números são verdadeiros? True

print(all(['Eric']))    # Todos os números são verdadeiros? True

nomes = ['Carlos', 'Camila', 'Carlaio']
print(all([nome[0] == 'C' for nome in nomes]))

nomes = ['Carlos', 'Camila', 'Carlaio', 'Eric']
print(all([nome[0] == 'C' for nome in nomes]))

any() -> Retorna True se qualquer elemento do iterável for verdadeiro, se o iterável estiver vazio, retorna false.
"""

print(any([0, 1, 2, 3, 4]))  # Retorna True se um elemento for True

print(any([0, 0, 0, 0]))    # Retorna False pois todos são False

