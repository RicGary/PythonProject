"""
PyCharm, se segurar o Ctrl você consegue ver a documentação de certas funções, ex:
    print()

def print(self, *args, sep=' ', end='\n', file=None): # known special case of print

    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.


enumerate cria uma tupla com o seu valor, ex:
    enumerate('Eric')
        ((0, 'E'), (1, 'r'), (2, 'i'), (3, 'c')

for indice, letra in enumerate(nome):
    print(indice, letra)

0 E
1 r
2 i
3 c

Quando não precisamos de um valor descartamos ele utilizando '_'.

for _, letra in enumerate(nome):
    print(letra)

E
r
i
c

Printa sem pular para próxima linha.

for _, letra in enumerate(nome):
    print(letra, end='')

Eric
"""

nome = 'Eric'

for _, letra in enumerate(nome):
    print(letra, end='')
