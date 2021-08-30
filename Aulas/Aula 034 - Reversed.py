"""
Reversed

Não confunda com a função reverse().

Função reverse():
    - Só funciona em listas.
    - Altera a lista original.

Função reversed():
    - Inverte qualquer iterável.
    - Retorna um objeto.
    - Podemos tornar o reversed() em uma tupla, lista etc.
"""
lista = [5,4,3,2,1]
print(tuple(reversed(lista)))