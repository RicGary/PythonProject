"""
Entendendo o **kwargs

Poderíamos chamar esse argumento de **(qualquer nome), mas utilizamos **kwargs  por convenção.

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que utilizemos os parâmetro nomeados, e transforma estes parâmetros extras em
um dicionário.

# Exemplo Básico

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita da {pessoa.title()} é {cor}.')

cores_favoritas(marcos = 'verde', julia = 'amarelo', fernanda = 'azul', eric = 'branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()   # Não gera erro.


# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythonico.'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]}, Geek!'
    return 'Não tenho certeza de quem você é.'


print(
    cumprimento_especial(),
    cumprimento_especial(geek='Python'),
    cumprimento_especial(geek='Oi'),
    cumprimento_especial(geek='Especial'),
    sep='\n'
)

# Nas funções podemos ter (nesta ordem):

- Parâmetros obrigatórios;
- *args;
- Parâmetros default;
- **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome.title()} tem {idade} anos.')
    print(args)
    if solteiro:
        print(f'{nome.title()} está solteir@.')
    else:
        print(f'{nome.title()} não está solteir@.')
    print(kwargs)

minha_funcao(18, 'julia')
minha_funcao(19, 'paula', 1,2,3,5, solteiro=False)
minha_funcao(34, 'felipe', eu = 'Não', voce = 'Está')
"""

