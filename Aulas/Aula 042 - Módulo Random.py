"""
Módulo Random e o que são Módulos.

- Em Python, nada mais são que outros arquivos Python.

Módulo Random: Possui várias funções para geração de números pseudo-aleatórios.


# OBS: Existem duas formas de utilizar um módulo deste.

# Forma 1 - Importando todo o módulo (Não recomendado)

import random

#     pacote  função
print(random.random()) # Gera um valor pseudo-aleatório entre [0,1)

# OBS**: Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis (Ficarão em memória). Caso você saiba quais funções você precisa utilizar
# deste módulo, então esta não seria a forma ideal de utilização. Veremos uma forma melhor na forma 2.

# Lembre-se de utilizar o dir() para ver os comandos possíveis e o help() para saber o que cada comando faz.


# Forma 2 - Importando uma função específica do módulo. Forma recomendada.

from random import random

print(random())

# Importa apenas a função do módulo que queremos utilizar

for i in range(10):
    print(random())


# Utilizando uniform()
from random import uniform
from collections import Counter

dado = []
for i in range(21):
    # Valores entre [1, 10) Nunca vai ter 10
    dado.append(int((uniform(1, 21))))

print(sorted(dado))
print(Counter(dado))


# randint() -> Gera valores pseudo-aleatórios entre os valores estabelecidos.

from random import randint
# Gerdor de apostas para mega-sena

final = ', '
for i in range(6):
    if i == 5:
        final = ' '

    print(randint(1,61), end=final)


from random import choice

# choice -> Mostra um valor aleatório entre um iterável.

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
"""
from random import shuffle
# shuffle() -> Embaralha os dados.

cartas = [1,2,3,4,5,6,7]

shuffle(cartas)

print(cartas)