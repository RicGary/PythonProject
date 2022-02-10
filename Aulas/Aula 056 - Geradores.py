"""
Geradores ou Generators

Info:
    - São iteradores.
    - Podem ser criados com funções geradoras.
    - Funções geradoras utilizam a palavra reservada yield.
    - Generators podem ser criados com expressões geradoras.

Dif. entre funções e generator functions:
------------------------------------------------------------------------------------------
| Funções:                                     |   Generator functions:                  |
------------------------------------------------------------------------------------------
| utilicam return                              |  utilizam yield                         |
------------------------------------------------------------------------------------------
| retorna uma vez                              | pode utilizar yield múltiplas vezes     |
------------------------------------------------------------------------------------------

"""

# Exemplo de Generator function


def Conta(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


# OBS: Uma Generator Function não é um GENERATOR, ela gera um Generator.

generator = Conta(5)

for n in generator:
    print(n)

print(list(Conta(10)))