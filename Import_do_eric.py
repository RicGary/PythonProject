"""

Somatório de inteiros, floats e strings.

"""

string = ['Eric', 'Lúcio', 'Paulo']
inteiro = [5, 5, 5, 5]
flutuante = [1.0, 2.0, 7.0]


def soma(arg, esp=''):
    tipo = type(arg)

    if tipo == type([]):
        lista = arg
        tipo = type(lista[0])

        if tipo == type('a'):
            resposta = esp.join(lista)

        if tipo == type(1):
            resposta = sum(lista)

        if tipo == type(1.0):
            resposta = sum(lista)

    return resposta


print(soma(string))
