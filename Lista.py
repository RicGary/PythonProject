"""

Estudando listas e suas iterações.

# Ordenar a lista
lista1.sort()
print(lista1)
lista2.sort()
print(lista2)

# Podemos ver se tem determinado valor numa lista, pode ter lista dentro de lista
num = 'E'
if num in lista2:
    print(f'{num} está na lista.')
else:
    print(f'{num} não está na lista.')

# Podemos facilmente ver quantas vezes o valor se repete em determinada lista
print(lista2.count('i'))

# Podemos adicionar valor único com .append()
lista1.append(5)
print(lista1)

# Podemos adicionar múltiplos valores de uma lista em outra com .extend()
lista3.extend([11,12,13])
print(lista3)

# Podemos inverter a ordem
lista3.reverse()
print(lista3)
print(lista1[::-1])

# Copiar lista
lista4 = lista3.copy()
print(lista4)

# Tamanho da lista
print(len(lista1))

# Podemos remover facilmente o último elemento
# OBS: Não apenas remove o elemento mas também o retorna
print(lista4)
print(lista4.pop())
print(lista4)

# Podemos remover um elemento pelo índice
print(lista4.pop(3))

# Podemos facilmente repetir elementos em uma lista
lista5 = [1,2,3]
lista5 = lista5 * 3
print(lista5)

# Podemos transformar uma string em lista
# OBS: Por padrão o split separa os elementos da lista pelo espaço entre elas
curso = 'Programação é essencial para vida moderna'
print(curso)
curso = curso.split()
print(curso)

# Convertendo uma lista em uma string
# OBS: Pega a lista 6 e coloca um espaço em cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Iterando sobre listas
for elemento in lista1:
    print(elemento)
soma = 0
for elemento in lista1:
    soma = soma + elemento
    print(soma)
"""

lista1 = [99, 1, 3, 54, 234, 12, 2]
lista2 = ['lista2','E', 'r', 'i', 'c', ' ', 'N', 'a', 'i', 'b', 'e', 'r']
lista3 = ['lista3',0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista6 = ['Programação', 'é', 'essencial', 'para', 'vida','moderna']

# Utilizando o while

carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto na lista ou digite "sair" para sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

