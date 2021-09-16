"""
O bloco Try/Except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previninido
assim que o programa para de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática

except:
    //o que deve ser feito em caso de problemas

# Exemplo 1 - Tratando um erro genérico:

try:
    funcao()

except:
    print('Deu problemas.')

# OBS: Tratar erro de forma genérica não é a melhor forma de se tratar um erro.

# Exemplo 2

try:
    funcao()

except NameError:
    print('Você está utilizando uma função inexistente.')

    # Trata um erro específico.

# Exemplo 3

try:
    len(5)

except NameError:
    print('Erro')

    # Tenta tratar apenas o erro específico, neste caso, NameError.

# Exemplo 4

try:
    len(5)

except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

    # Mensagem de erro extra explicando o que aconteceu, normalmente utiliza-se esta forma para armazenar
    # um tipo de erro em um banco de dados.

# Exemplo 5

try:
    #len(5)
    #f()
    #(1,2,3).sort()
    print('Eric'[10])

except NameError as erro:
    print(f'Ocorreu um NameError: {erro}')
except AttributeError as erro:
    print(f'Ocorreu um AttributeError: {erro}')
except:
    print('Ocorreu um erro não arquivado.')
"""

# Exemplo Prático

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = dict(Eric = 'Naiber')
print(pega_valor(dic, 'Nome'))
