"""
Dicionários.

Dicionários são coleções do tipo chave/valor representados por {}.
print(type({}))


OBS: Sobre Dicionários.
    - Chave e valor são separados por ":".
    - Tanto chave quanto valor podem ser de qualquer tipo de dado.
    - Podemos misturar tipos de dados.

# Criação de Dicionários.

# Forma 1 (Mais comum)

#       chave : valor   chave : valor          chave : valor
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ca': 'Canadá'}
print(paises)

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', ca='Canadá')

# Acessando elementos

# Forma 1 - Acessando pela chave.

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ca': 'Canadá'}

print(paises['br'])
print(paises['ca'])

# Forma 2 - Acessando via get (Recomendado) pois retorna None e
# não erro como o de cima.

print(paises.get('br'))
print(paises.get('caa'))    # Retorna o tipo None.Um tipo sem tipo.

# Por que usar o .get()

# Não da erro.

paises = dict(br='Brasil', eua='Estados Unidos', ca='Canadá')

canada = paises.get('ca')

if canada:
    print('Encontrei o Canadá.')
else:
    print('Não encontrei o país.')

# Por que usar o .get()

# Não da erro.

paises = dict(br='Brasil', eua='Estados Unidos', ca='Canadá')

canada = paises.get('ca')

if canada:
    print('Encontrei o Canadá.')
else:
    print('Não encontrei o país.')

# Outra forma melhor de fazer isto.

russia = paises.get('ru','Não encontrado') # Se não encontrar o valor 'ru'
                                           # printa o valor
print(russia)

# Verificando

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'ca': 'Canadá'}

# Ele pesquisa a Chave e não o valor.

print('br' in paises)
print('Brasil' in paises)
print('ru' in paises)

# Adicionar elemento ao dicionário.

receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Forma 1

receita['abr'] = 350
print(receita)

# Forma 2

novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 250
print(receita)

# Forma 2

receita.update({'abr': 100})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos e atualizar é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO  podemos ter chaves repetidas.

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Forma 1 - Mais comum

receita.pop('mar')
print(receita)

# OBS 1: Caso ele não encontre a chave um KeyError será retornado.
# OBS 2: O valor removido sempre será retornado.

# Forma 2

del receita['fev']
print(receita)

# OBS 1: Se a chave não existir será gerado um KeyError.
# OBS 2: Neste caso o valor não será retornado.

"""


# OBS 1: Se a chave não existir será gerado um KeyError.
# OBS 2: Neste caso o valor não será retornado.
