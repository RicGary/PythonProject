"""
Try, Except, Else, Finally

Dica de quando e onde tratar código:

TODA ENTRADA DE USUÁRIO DEVE SER TRATADA!

OBS: A função do usuário é destruir seu sistema.
OBS*: Else e Finally não são tão comuns.


# Exemplo 1

# Não é a melhor forma.
num = 'um valor inválido'

try:
    num = int(input('Informe o valor: '))

except ValueError:
    None

print(f'Você digitou {num}.')


# Else -> Só é executado se não ocorrer o erro.
try:
    num = int(input('Informe o valor: '))

except ValueError:
    print('Valor inválido.')

else:
    print(f'Você digitou {num}.')
"""

# Finally

try:
    num = int(input('Informe o valor: '))

except ValueError:
    print('Valor inválido.')

else:
    print(f'Você digitou {num}.')

finally:
    print('Executando o Finally.')

# OBS: O finally é sempre executado.
# Geralmente é utilizado para fechar ou desalocar recursos.