"""
Módulo Collections - Ordered Dict

link: https://docs.python.org/3/library/collections.html#collections.OrderedDict

Em um dicionário normal a ordenação não é garantida, diferente do Ordered Dict.

"""
# Fazendo o import

from collections import OrderedDict

dicionario = OrderedDict(dict(a=1, b=2, c=3, d=4))
print(dicionario)

# Diferença dos dicionários comuns

dict1 = dict(a=1,b=2)
dict2 = dict(b=2,a=1)

print(dict1==dict2)

# Diferença do Ordered Dict

dict1 = OrderedDict(dict(a=1,b=2))
dict2 = OrderedDict(dict(b=2,a=1))

print(dict1==dict2)