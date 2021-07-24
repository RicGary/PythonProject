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

#Gerar um índice:
cores = ['verde','azul','amarelo','tanjerina']

for indice,cor in enumerate(cores):
    print(indice, cor)

    ou

cores = list(enumerate(cores))
print(cores)

# Encontrar o índice de determinado valor

#          0  1  2  3  4  5
numeros = [5, 4, 3, 2, 1 ,0]


print(numeros.index(2))

# Slicing de listas. (Copiar da aula)

uma_lista = ['a', 'b', 'c', 'd', 'e', 'f']
print(uma_lista[1:3])           # Vai do índice 1 até o índice 2 pois exclui o 3.
print(uma_lista[:4])            # Pega os 4 primeiros.
print(uma_lista[3:])            # Pega os 3 últimos

uma_lista = ['a', 'b', 'c', 'd', 'e', 'f']
uma_lista[1:3] = ['x', 'y']
print(uma_lista)            # Substitui  o índice 1 ao 3 excluido pelos indicados


uma_lista = ['a', 'b', 'c', 'd', 'e', 'f']
uma_lista[1:3] = []
print(uma_lista)            # Remove os índices do 1 ao 3 excluido.

uma_lista = ['a', 'd', 'f']
uma_lista[1:1] = ['b', 'c']
print(uma_lista)                # Adiciona os elementos no índice escolhido.
uma_lista[4:4] = ['e']
print(uma_lista)

a = ['um', 'dois', 'três']
del a[1]
print(a)            # Deleta o índice 1.

lista = ['a', 'b', 'c', 'd', 'e', 'f']
del lista[1:5]
print(lista)            # Deleta o índice 1 ao 5 excluido.
"""

lista1 = [99, 1, 3, 54, 234, 12, 2]
lista2 = ['lista2', 'E', 'r', 'i', 'c', ' ', 'N', 'a', 'i', 'b', 'e', 'r']
lista3 = ['lista3', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista6 = ['Programação', 'é', 'essencial', 'para', 'vida', 'moderna']

cores = ['verde', 'azul', 'amarelo', 'tanjerina']
