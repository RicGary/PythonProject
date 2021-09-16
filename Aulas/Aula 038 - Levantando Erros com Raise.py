"""
Levantando os próprios erros com raise.

raise -> Lança exceções

OBS: raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagemns
de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')

"""

# Exemplo



# Exemplo mais correto, utilizável

def colore(texto, cor):
    cores = ('Verde', 'Vermelho', 'Azul', 'Branco', 'Amarelo')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma dessas: {cores}')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string.')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma palavra.')
    if cor[-1] == 'o':
        cor = cor.replace(cor[-1], 'a')

    print(f'{texto} será impresso na cor {cor.lower()}.')

colore('Eric', 'Amarelo')
colore('Eric', 'Preto')
colore('Eric', 1)