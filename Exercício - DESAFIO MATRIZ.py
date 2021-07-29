"""
DESAFIO MATRIZ PYTHON

Crie um programa que crie uma matriz da dimensão 3x3 e preencha com valores
lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-='*30)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')  # :^5 faz com que fique com 5 espaços centralizado
    print() # Toda vez que terminar uma linha ele quebra a identação de cima
            # fazendo com que cada linha seja listada de cada vez
