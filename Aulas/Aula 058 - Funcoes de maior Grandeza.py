"""
Funções de maior grandeza - Higher Order Functions (HOF)

    Qunado uma linguagem suporta HOF, indica que podemos ter funções que retoram
    outras funções como resultado, ou mesmo que podemos passar funções como argumentos
    para outras funções. Podemos até mesmo criar variáveis do tipo de funções nos nossos
    programas.

OBS: Na aula de funções, utilizamos o HOF mas não em detalhes.



# Ex - definindo funções:


def soma(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(1, 2, soma))


# Nested functions
#Podemos ter funções dentro de funções

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Você é um gato '))
    return humor() + pessoa

print(cumprimento('Eric'))
"""

