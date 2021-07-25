"""
Conjuntos

- Conjuntos em qualquer linguagem de programação estamos fazendo referência
à Teoria dos Conjuntos da Matemática (intersecção, união, etc da probabilidade).

- Aqui no Python os Conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados.
- Sets (conjuntos) não possuem valores ordenados.
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles.Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos (sets) são referênciados em Python com {}.

Deferença entre Conjuntos (Sets) e Mapas (Dicionários).
    - Um dicionário tem chave/valor;
    - Um conjunto tem valor, apenas valor;

# Definindo um Conjunto

# Forma 1

s = set({1, 2, 3, 7, 5, 3, 5, 2, 6, 8})  # Repare que tamos valores repetidos
print(s)
print(type(s))

# OBS: Ao criar um conjunto cajo seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar erros e não fará parte do conjunto.

# Forma 2 - Mais Comum

s = {1, 2, 3, 6, 8, 6, 2, 5}
print(s)
print(type(s))

# Exemplos e testes.

s = set('Geek University')
print(s)

lista = {1, 2, 4, 6, 8, 7, 2, 1}
print(set(lista))

tupla = (1,3,6,2,6,8)
print(set(tupla))

if 3 in s:
    print('Tem o 3.')
else:
    print('Não tem o 3.Já que é string.')

# Importante lembrar que além de não termos valores duplicados, NÃO
# temos ordem.

dicionario = {}.fromkeys([12, 1, 4, 53, 100, 23, 1], 'dict')
print(f'Dicionário: {dicionario}, com {len(dicionario)} elementos')

lista = [12, 1, 4, 53, 100, 23, 1]
print(f'Lista: {lista}, com {len(lista)} elementos')

tupla = (12, 1, 4, 53, 100, 23, 1)
print(f'Tupla: {tupla}, com {len(tupla)} elementos')

conjunto = {12, 1, 4, 53, 100, 23, 1}
print(f'Conjunto: {conjunto}, com {len(conjunto)} elementos')


# Assim como todo outro conjunto Python, podemos colocar todos os tipos
# de dados misturados em sets.

# Usos interessantes com sets.

# - Imagine que fizemos um formulário de cadastro de visitantes em uma feira
#   ou museu e os visitantes informam manualmente a cidade de onde vieram.

# - Nós adicionamos cada cidade em uma lista Python, já que uma lista podemos adicionar
#   novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'Porto Alegre', 'São Paulo', 'Cuiabá', 'Belo Horizonte', 'São Paulo', 'Porto Alegre']

# Agora precisamos saber quantas cidades distintas temos.

print(f'Temos um total de {len(cidades)} pessoas, sendo um total de {len(set(cidades))} cidades diferentes.')
print(f'Lista: {cidades}')
print(f'Set: {set(cidades)}')

# Adicionando elementos em um conjunto

s = {1, 2, 3}
s.add(4)
s.add(4)    # Duplicidade não gera erro.
print(s)

# Remover elementos em um conjunto
s = {1, 2, 3}

# Forma 1

s.remove(2)     # NÃO É ÍNDICE, Conjuntos não são indexados.

print(s)

# OBS: Ao tentar remover um valor não encontrado será gerado um KeyError.

# Forma 2

s.discard(1)

print(s)
print(s.discard(23))

# OBS: Ao tentar remover um valor não encontrado NÃO será gerado um KeyError.


# Copiando um conjunto para o outro
s = {1, 2, 3, 4}

# Forma 1 - Deep Copy

novo = s.copy()
novo.add(5)
print('Conjunto: ',s)
print('Novo: ',novo)

# Forma 2 - Shallow Copy

novo = s
novo.add(5)
print('Conjunto: ',s)
print('Novo: ',novo)


# Podemos remover todos os itens de um conjunto.

s = {1,2,3,4,5}
print(s)

s.clear()
print(s)


# Métodos Matemáticos de Conjuntos  (Resumido)

# Imagine que temos dois conjuntos, um contendo estudantes do curso Python
# e um contendo estudantes do curso de Java.

estudantes_python = {'Eric', 'Felipe', 'Júlia', 'Pedro', 'Patrícia', 'Amenadiel', 'Castiel'}

estudantes_java = {'Gustavo', 'Ana', 'Rafaela', 'Júlia', 'Patrícia'}

# Veja que alguns alunos que estudam Python também estudam Java.
# Precisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando .union (União entre conjuntos)

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe "|"

unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estudam Python e também Java.

# Forma 1 - Utilizando intersection (Intersecção)

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)


# Gerar um conjunto de estudantes que estão em um e não no outro.

so_python = estudantes_python.difference(estudantes_java)
print('Só estudam Python: ',so_python)

so_java = estudantes_java.difference(estudantes_python)
print('Só estudam Java: ',so_java)

# Soma, valor máximo, valor mínimo e tamanho.

s = {0, 1, 2, 3, 4, 5,}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
"""

s = {1,2,3}
print(help(s))
