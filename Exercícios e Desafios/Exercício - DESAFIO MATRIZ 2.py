"""
DESAFIO MATRIZ 2

Utilizar os valores:

| 2  3  4  |
| 5  10 11 |   = det = -34
| 3  9  1  |

| a  b  c | a  b |
| d  e  f | d  e |  = det
| g  h  i | g  h |

1 - Crie uma matriz (sem utilizar bibliotecas) 3 x 3 e encontre o determinante (com ou sem bibliotecas).
OBS: Utilize timer() para ver quantos .s leva para fazer o calculo 1000 vezes.
"""
import numpy as np

# 1 - Sem biblioteca

# OBS: A forma a seguir foi feita com o propósito de mostrar como seria uma matriz em python
# ,porém não é a forma mais recomendada.

def __Matriz_nobib__(change=False):

    """
    Cada lista dentro de variáveis representa uma linha e cada
    índice dentro desta linha representa uma coluna.
    """

    VARIAVEIS = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    if change:
        for linha in range(len(VARIAVEIS)):
            for coluna in range(len(VARIAVEIS)):

                # Essa é a forma de acessar cada elemento na matriz.
                VARIAVEIS[linha][coluna] = float(input(f'{VARIAVEIS[linha][coluna]}: '))

        # Forma básica para imprimir uma matriz
        for linha in VARIAVEIS:
            print(linha)

    else:
        VARIAVEIS = [[2, 3, 4], [5, 10, 11], [3, 9, 1]]

    # numpy.linalg(linear algebra).det(determinant)(array/list) para calcular det
    return np.linalg.det(VARIAVEIS)


__Matriz_nobib__(False)
