"""
Escrevendo em arquivos

Passo:

    1 - Abrir com o formato de escrita.
    2 - Adicionar o que quiser.

with open('znovo_arquivo.txt', 'w', encoding='utf-8') as f:
    f.write('Escrevendo dados.\n')
    f.write('Adicionando linhas.\n')
    f.write('Ultima linha.')

with open('zznum.txt', 'w') as num:
    for i in range(20):
        num.write(f'{i : ^4} {i * 2 : ^4} {i * 3 : ^4} \n')

with open('zzpy.py', 'w') as py:
    py.write('def f(x):\n')
    py.write('    return x ** 2\n')
    py.write('print(f(2))')

# OBS: Não pode passar valor numérico.
"""

