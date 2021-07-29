"""
Módulo Collections - Deque

Podemos dizer que o Deque é uma lista de alta performance.

link: https://docs.python.org/3/library/collections.html#collections.deque

"""

# Importando

from collections import deque

# Criando deques

deq = deque('geek')
print(deq)

# Adicionando elementos no deque

deq.append('y')
print(deq)

deq.appendleft('y')
print(deq)

# Removendo elementos

deq.remove('k')
print(deq)

print(deq.pop())
print(deq)

print(deq.popleft())
print(deq)