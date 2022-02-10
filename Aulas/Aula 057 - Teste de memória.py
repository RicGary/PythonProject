"""
Testando Generators

Fibonacci:

1, 1, 2, 3, 5, 8...


# Função usando listas

def __Fib_lista__(max):
    nums = []
    a, b = 0, 1
    for _ in range(max):
        nums.append(b)
        a, b = b, b + a
    return nums


# Teste 1: 450 Mb


for i in __Fib_lista__(100_000):
    print(i)
"""

# Função com gerador


def __Fib_gen__(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, b + a
        yield a
        contador += 1

# Teste 2: Generator -> 4,5 Mb


for i in __Fib_gen__(100_000):
    print(i)