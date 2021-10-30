"""
Entendo Iteradores e Iteráveis


Iterador:
 -> Um objeto que pode sofrer iteração.
 -> Um objeto que retorna um dado, um por vez, quando uma func. next() é chamada.

Iterável:
-> Um objeto que irá retornar um iterador quando a função iter() for chamada.


name = 'Eric'   # Não é um iterador, é um ITERÁVEL

iterable1 = iter(name)

print(next(iterable1))
print(next(iterable1))
print(next(iterable1))
print(next(iterable1))
print(next(iterable1))  # Erro StopIteration
"""

