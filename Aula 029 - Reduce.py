"""
Reduce

OBS: A partir da versão 3, a função reduce não é mais uma função integrada (não é uma built-in). Agora temos
que importar e utilizar esta função a partir do módulo 'functools'.

Guido van Rossum (criador do python): Utilize a função reduce se você realmente precisa dela, em todo caso
99% das vezes um loop for é mais legível.

Para entender o reduce():

    - Imagine que você tem uma coleção de dados;

        dados = [a1,a2,a3,...,an]

    - Você tem uma função que recebe dois parâmetros;

def func(x,y):
    return x*y

Assim como map() e filter() recebe a função e o iterável.
A função reduce() funciona da seguinte forma;
Passo 1:
    res1 = func(a1,a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.

Passo 2:
    res2 = func(res1,a3)

.
.
.

Passo n:
    resn = func(resm, resn)


Podemos ver a função reduce() da seguinte forma:

func(func(func(a1,a2),a3),a4),...),an)
"""
from functools import reduce

# Como funciona na prática?

# Vamos utilizar a função para multiplicar todos os números da lista.

dado = [1, 2, 3, 4, 5]

res = reduce(lambda x, y: x * y, dado)
print(res)

# Utilizando um loop normal

res = 1
for i in range(len(dado)):
    res *= dado[i]

print(res)