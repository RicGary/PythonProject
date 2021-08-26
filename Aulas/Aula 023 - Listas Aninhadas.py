"""
Listas Aninhadas (Nested Lists)

- Algumas liguagens de programação (C/Java/PHP) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

- Em Python nós conhecemos as Listas

# Exemplos

# 1

livro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
print(livro, type(livro))

# Como fazemos para acessar os dados

# Iterando com loops em uma lista aninhada
for lista in range(len(livro)):
    for valor in range(len(livro)):
        print(f'{livro[lista][valor]:5}')

# List Comprehension

# Para cada valor em uma lista dentro do livro imprime o valor
[[print(f'{valor:3}') for valor in lista] for lista in livro]

# 2

# Gerando um tabuleiro (matrix) 3x3

# Cria uma matriz de 3x3
tabuleiro = [[valor for valor in range(1,4)]for valor in range(1,4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['X' if valor % 2 == 0 else 'O' for valor in range(1,4)]for valor in range(1,4)]
print(velha)

# Gerando valores iniciais

print([['*' for i in range(1,4)]for j in range(1,4)])
"""

