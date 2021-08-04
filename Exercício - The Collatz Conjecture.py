"""
The Collatz Conjecture.

O simples problema da matemática que ninguém consegue resolver.
    - O problema diz basicamente:
        - Todo número colocado em f(x) eventualmente dará 1, inclusive todos os números até 2**68 já
            foram verificados, isso da aproximadamente 300 quintilhões.
        - O método é; "n/2" se "n" for par e "3*n+1" se for ímpar.

No final sempre terá um valor do tipo:
    10 → 5 →  6 → 3 → 4 → 2 → 1 → 2 → 1 → 2 → …
    11 → 12 → 6 → 3 → 4 → 2 → 1 → 2 → 1 → 2 → …

Este exercício é uma prova desse problema.
"""
from collections import Counter
import matplotlib.pyplot as plt

def infamous_number(x):
    lista_numeros_passados = []
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = 3*x + 1
        lista_numeros_passados.append(x)
    return lista_numeros_passados

"""
print(
    f'Value: 10  {infamous_number(10)} Len: {len(infamous_number(10))}',
    f'Value: 25  {infamous_number(25)} Len: {len(infamous_number(25))}',
    f'Value: 50  {infamous_number(50)} Len: {len(infamous_number(50))}',
    f'Value: 100 {infamous_number(100)} Len: {len(infamous_number(100))}',
    f'Value: 150 {infamous_number(150)} Len: {len(infamous_number(150))}',
    sep='\n'
)
"""

"""
# Interessante pois parece que nenhum número repete...

for chave, valor in Counter(infamous_number(10000000000)).items():
    if valor != 1:
        print(chave)

# Nenhum valor é repetido
"""

# Plotando The Collatz Conjecture

x = []
y = []

for i in range(1,10000):
    a = infamous_number(i)
    x.append(i)
    y.append(len(a)-1)
plt.plot(x,y, '.',color = 'crimson')
plt.title("The Collatz Conjecture - Infamous Number")
plt.show()