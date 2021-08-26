"""
 - Conforme aumenta o número da frente a dificuldade aumenta.

Dificuldade: 1/50.

1 - Faça um programa que possua um vetor denominado A que armazene 6 números
inteiros.O programa deve executar os seguintes passos:
a)Atribua os seguintes valores a esse vetor:
b)Armazene em uma variável inteira (simples) a soma entre os valores das
posições 0,1 e 5 do vetor.
c)Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
d)Mostre na tela cada valor do vetor A, um em cada linha

# Resposta 1

vetor = [1,0,5,-2,-5,7] # 1.a

variavel_inteira = vetor[0] + vetor[1] + vetor[5]   # 1.b
print('Variável inteira: ',variavel_inteira)

vetor[4] = 100  # 1.c

for valor in vetor:
    print(valor)


6 - Faça um programa que receba do usuário um vetor com 10 posições.
Em seguida deverá ser impresso o maior e o menor elemento do vetor.

# Resposta 6

vetor = list(range(10)) # Vetor qualquer
print(vetor)

print('Valor mínimo', min(vetor))
print('Valor máximo', max(vetor))


7 - Escreva um programa que leia 10 números inteiros e os armazene em
um vetor.Imprima o vetor, o maior elemento e a posição que ele se encontra.

# Resposta 7

numeros = 1,4,2,6,10,8,6,9,6,3
vetor = []
for valor in numeros:
    vetor.append(valor)
print(f'Vetor: {vetor}. Maior elemento e posição: {max(vetor)}, {vetor.index(max(vetor))}.')


13 - Fazer um programa para ler 5 valores e, em seguida, mostrar
a posição onde se entram o maior e o menor valor.

# Resposta 13

numeros = 1,5,2,8,4
print(f'Posição do maior número e do menor, respectivamente: {numeros.index(max(numeros))}, {numeros.index(min(numeros))}')


28 - Leia 10 números inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2.
Copie os valores ímpares de v para v1, e os valores pares de v para v2.Note que cada
um dos vetores v1 e v2 têm no máximo 10 elementos, mas nem todos os elementos sãoo utilizados.
No final escreva os elementos UTILIZADOS de v1 e v2.

# Resposta 28

numeros = list(range(10))
vetor = []
for valor in numeros:
    vetor.append(valor)
print(vetor)

v1 = [] # ìmpares
v2 = [] # pares

for valor in vetor:
    if valor % 2 == 0: # Resto de uma divisão
        v2.append(valor)
    else:
        v1.append(valor)

print('Ímpares: ',v1)
print('Pares: ', v2)


33 - Faça um programa que leia um vetor de 15 posições e o compacte, ou seja,
elimine as prosições com valor zero. Para isso, todos os elementos à frente do
valor zero, devem ser movidos uma posição para trás no vetor.

# Resposta 33

vetor = [1,0,2,4,0,13,8,0,12,43,0,34,87,45,0]
for valor in vetor:
    if valor == 0:
        vetor.remove(valor)

print(vetor)


DESAFIO 50 - Escreva um programa que leia um número inteiro positivo n e em seguida
imprima n linhas do chamado Triangulo de Pascal:
Ex:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
...
"""

# Resposta DESAFIO 50

n = int(input('Valor desejado da pirâmide de Pascal: '))

list1 = []

for l in range(n):  # Linha da pirâmide.
    temp_list = []  # Lista temporária para armazenar os valores.
    for c in range(l+1):    # Coluna da pirâmide.
        if c == 0 or c == l:    # Se for o primeiro ou o último elemento.
            temp_list.append(1)     # Adiciona 1 nas laterais da pirâmide.
        else:
            temp_list.append(list1[l-1][c-1]+list1[l-1][c])
    list1.append(temp_list)

for i in range(n):
    for j in range(n-i-1):
        print(format(' ','<2'),end='')
    for j in range(i+1):
        print(format(list1[i][j],'<3'),end=' ')
    print()


