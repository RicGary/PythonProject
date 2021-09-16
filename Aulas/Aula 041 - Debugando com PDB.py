"""
Debuggando com PDB

PDB -> Python Debugger
Bug -> Inseto

Uma vez quando os computadores eram enormes, do tamanho de salas, aconteceu um erro com o código que ninguém sabia o que
era até que resolveram abrir o computador. Uma mariposa havia entrado pela janela e acabou ficando presa em uma das
válvulas ocasionando um erro, e assim foi feita uma das primeiras correções de BUG.


# OBS: A utilização do print() é uma prática ruim.

def dividir(a, b):
    print(a, b)
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as erro:
        return f'Ocorreu um problema: {erro}'


print(dividir(4, 7))


# Existem formas melhores para fazer o debug.
# Em Python podemos fazer em diferentes IDEs ou utilizando o PDB.

# Exemplo PyCharm: Clique nas linhas que deseja debuggar e aperte Shift+F9


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as erro:
        return f'Ocorreu um problema: {erro}'


print(dividir(4,0))
"""

# Exemplo com PDB (eu particularmente acho meio uga buga fazer assim, mas se quiser pode)
# Para utilizar o PDB precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
# http://pythonclub.com.br/debugging-em-python-sem-ide.html

import pdb

nome = 'Eric'
sobrenome = 'Naiber'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
import pdb; pdb.set_trace()
final = nome_completo + ' ' + 'é legal.'
print(final)

# Fazer o import somente na linha em que for utilizá-lo.