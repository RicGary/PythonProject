"""
Aula para criar um loop próprio.

Passamos um valor, transformamos ele em um iterável para poder finalmente
utilizá-lo na função.
"""


def NEW_FOR(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


NEW_FOR(list(range(10)))