"""
Módulo Collections - Default Dict

Link para mais info.: https://docs.python.org/3/library/collections.html?highlight=collections#collections.defaultdict

Collections -> High-performance Container Datetypes

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um
valor default, podendo utilizar um lambda para isso. Este valor será utilizado
sempre que não ouver um valor definido. Caso tentemos acessar uma chave que
não existe, essa chave será criada e o valor default será atribuido.

OBS: Lambdas são funções sem nome que podem ou não receber parâmetros
de entrada e retornar valores (Não se preocupe, ainda não teve aula de
funções e de lambdas).
"""

# Importando o Default Dict

from collections import defaultdict

dicionario = defaultdict(lambda : 0)

dicionario['curso'] = 'Programação em Python'

print(dicionario)

print(dicionario['outro'])  # Se fosse um dicionário normal seria gerado erro.

print(dicionario)