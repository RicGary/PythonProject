def _razao(a, b):
    if a > b:
        return a/b
    else:
        return b/a


def _teste():
    return None

if __name__ == '__main__':
    print('O módulo principal é chamado de: AAmodule_teste')
else:
    print('O "AAmodule_teste" foi importado com sucesso! ')
    print(__name__)